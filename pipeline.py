import pandas as pd

def clean_data(dataFrame):

    df = pd.DataFrame(dataFrame)
    
    df["preco"] = (
        df["preco"]
        .str.replace("R$", "", regex=False)
        .str.replace(".", "", regex=False)
        .str.extract(r"(\d+)")
    )

    df["area"] = (
        df["area"]
        .str.replace("m²", "", regex=False)
        .str.extract(r"(\d+)")
    )

    df["area"] = df["area"].fillna(0)

    df["quartos"] = (
        df["quartos"]
        .str.replace("quarto", "", regex=False)
        .str.replace("quartos", "", regex=False)
        .str.extract(r"(\d+)")
    )
    df["banheiros"] = (
        df["banheiros"]
        .str.replace("banheiro", "", regex=False)
        .str.replace("banheiros", "", regex=False)
        .str.extract(r"(\d+)")
    )
    df["vagas"] = (
        df["vagas"]
        .str.replace("vaga", "", regex=False)
        .str.replace("vagas", "", regex=False)
        .str.extract(r"(\d+)")
    )

    df["vagas"] = df["vagas"].fillna(0)

    df['tipo de imóvel'] = df['descricao'].str.split(' ').str[0]
    # Limpeza e formatação dos dados, incluindo remoção de símbolos, extração de números e tratamento de valores nulos

    df.head() #Exibição dos primeiros registros para verificação
    return df

