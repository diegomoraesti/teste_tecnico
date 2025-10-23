import pandas as pd


# Exporta para CSV
def exportar_csv(df: pd.DataFrame, arquivo: str = "Brasileirao_jogosAPI") -> None:
    df.to_csv('Brasileirao_JogosAPI.csv', index=False)