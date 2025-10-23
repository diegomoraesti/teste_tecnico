"""
Responsável por exportar os dados tratados para CSV ou Excel.

"""

import pandas as pd
# Cria DataFrame final


# Exporte do dataframe para csv
def exportar_csv(df: pd.DataFrame, arquivo: str = 'Brasileira_JogosGE.csv') -> None:
    df.to_csv(arquivo, index=False)
      