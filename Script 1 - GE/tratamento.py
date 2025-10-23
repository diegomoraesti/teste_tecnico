##################################
#                                #
# Tratamento de dados para o CSV #
#                                #
##################################

import pandas as pd
import pytz
from datetime import *

def tratar_partidas(dados_brutos: list[str]) -> pd.DataFrame:


    brasilia_tz = pytz.timezone("America/Sao_Paulo")

    # Limite: ontem (apenas data)
    limite_data = (datetime.now(brasilia_tz) - timedelta(days=1)).date()

    jogos_tratados = []

    for linha in dados_brutos:
        try:

            partes = linha.split(" / ")
            partida = partes[0].strip()
            data_hora_raw = partes[1].strip()

            # Converte para datetime e ajusta para Brasília
            dt_utc = datetime.fromisoformat(data_hora_raw)
            dt_br = dt_utc.astimezone(brasilia_tz)

            # Filtra apenas jogos cuja data é maior ou igual a ontem
            if dt_br.date() >= limite_data:
                jogos_tratados.append({
                    "Partida": partida,
                    "Data": dt_br.strftime("%d/%m/%Y"),
                    "Hora": dt_br.strftime("%H:%M")
            })
        except ValueError:
            continue

    return pd.DataFrame(jogos_tratados)