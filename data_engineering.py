import pandas as pd
import numpy as np
from config import EXCEL_NAME

def process_data(data):

    df = pd.DataFrame(data)

    # Fixing the types of the columns
    df["preco"] = pd.to_numeric(df["preco"], errors="coerce")
    df["area"] = pd.to_numeric(df["area"], errors="coerce")
    df["quartos"] = pd.to_numeric(df["quartos"], errors="coerce")
    df["banheiros"] = pd.to_numeric(df["banheiros"], errors="coerce")
    df["vagas"] = pd.to_numeric(df["vagas"], errors="coerce")

    df["preco"] = df["preco"].fillna(0)
    df = df[df["preco"] <= 10000]

    # Creating a new column for price per square meter
    df["preco_m2"] = np.where(
        df["area"] > 0,
        df["preco"] / df["area"],
        np.nan
    )

    # Extraction of neighborhood and city from the description
    df["bairro"] = (
        df["descricao"]
        .str.split(" em ")
        .str[-1]
        .str.split(",")
        .str[0]
    )

    df["cidade"] = (
        df["descricao"]
        .str.split(",")
        .str[-1]
        .str.strip()
    )

    # Extract the type of property from the description
    df['tipo de imóvel'] = df['descricao'].str.split(' ').str[0]

    df.to_excel(f"data/{EXCEL_NAME}", index=False )