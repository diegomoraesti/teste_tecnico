# ===============================
# Tratamento dos dados
# ===============================

import requests
from datetime import *
import pandas as pd

def tratar_partidas(dados_brutos: list[str]) -> pd.DataFrame:

    # Cria uma lista de dicionários no formato desejado
    jogos_tratados = []
    for jogo in dados_brutos:
        data_hora = jogo["Data/Hora"].split(" ")
        jogos_tratados.append({
            "Jogo": f"{jogo['Mandante']} X {jogo['Visitante']}",
            "Data": data_hora[0],
            "Hora": data_hora[1]
        })

    return pd.DataFrame(jogos_tratados)