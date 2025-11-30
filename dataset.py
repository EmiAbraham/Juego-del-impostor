import pandas as pd
from pathlib import Path

# Carpeta donde están todos los CSV de temáticas
DATA_FOLDER = Path(__file__).parent / "datasets"


def cargar_temas() -> list[str]:
    """
    Devuelve la lista de temáticas disponibles según los CSV encontrados.
    Solo incluye archivos que no estén vacíos.
    """
    temas = []
    for archivo in DATA_FOLDER.glob("*.csv"):
        # si el archivo está vacío, lo salteamos
        if archivo.stat().st_size == 0:
            continue
        temas.append(archivo.stem)  # nombre sin .csv
    return sorted(temas)


def cargar_palabras(tema: str) -> list[str]:
    """
    Carga el CSV de la temática indicada y devuelve una lista de palabras.
    - Si el CSV tiene columna 'nombre', usa esa.
    - Si no, usa la primera columna que encuentre.
    Lanza errores claros si el archivo está vacío o sin filas.
    """
    ruta_csv = DATA_FOLDER / f"{tema}.csv"

    if not ruta_csv.exists():
        raise FileNotFoundError(f"No encontré el archivo {ruta_csv}")

    # Archivo sin contenido
    if ruta_csv.stat().st_size == 0:
        raise ValueError(f"El archivo {ruta_csv.name} está vacío. Revisá su contenido.")

    df = pd.read_csv(ruta_csv)

    # CSV sin filas útiles
    if df.empty:
        raise ValueError(f"El archivo {ruta_csv.name} no tiene filas de datos.")

    if "nombre" in df.columns:
        serie = df["nombre"]
    else:
        # usa la primera columna que haya
        primera_columna = df.columns[0]
        serie = df[primera_columna]

    return serie.dropna().drop_duplicates().tolist()