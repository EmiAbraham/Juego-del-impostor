#Carga del dataset
import pandas as pd 
from pathlib import Path 

DATA_FILE = Path(__file__).parent / "final_data.csv"    

def cargar_equipos(ruta_csv: str | Path = DATA_FILE) -> list[str]: 
    #Lee el dataset y devuleve una lista con los equipos 

    dataset = pd.read_csv("final_data.csv")
    #Nos quedamos solo con la columna de equipos 

    df = dataset[["TEAM_NAME"]].drop_duplicates()

    return df["TEAM_NAME"].to_list()

