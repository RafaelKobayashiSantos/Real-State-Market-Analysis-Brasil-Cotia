import pandas as pd
import numpy as np

def process_data(data):

    df = pd.DataFrame(data)

    # Corrigit tipagem dos dados
    df["preco"] = pd.to_numeric(df["preco"], errors="coerce")
    df["area"] = pd.to_numeric(df["area"], errors="coerce")
    df["quartos"] = pd.to_numeric(df["quartos"], errors="coerce")
    df["banheiros"] = pd.to_numeric(df["banheiros"], errors="coerce")
    df["vagas"] = pd.to_numeric(df["vagas"], errors="coerce")

    df["preco"] = df["preco"].fillna(0)
    df = df[df["preco"] <= 10000]

    # Criação de nova coluna preço por metro quadrado
    df["preco_m2"] = np.where(
        df["area"] > 0,
        df["preco"] / df["area"],
        np.nan
    )

    # Extração de bairro e cidade da descrição
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
    

    df.to_excel( "dados_imoveis_pby.xlsx", index=False )