"""
Coleta as partidas do Brasileirão da próxima rodada no site da ESPN.
Converte datas para horário de Brasília usando datetime puro.
"""
import requests
from datetime import *
import pandas as pd

def proximos_jogos_brasileirao(headless: bool = True) -> list[str]:

    
    # Fuso horário de Brasília (UTC-3)
    fuso = timezone(timedelta(hours=-3))
    
    apipath = "https://site.api.espn.com/apis/site/v2/sports/soccer/bra.1/scoreboard"
    response = requests.get(apipath)
    jogos = []

    if response.status_code == 200:
        data = response.json()

        for event in data.get("events", []):
            if event["status"]["type"]["name"] == "STATUS_SCHEDULED":
                competition = event["competitions"][0]
                teams = competition["competitors"]

                home = next(t for t in teams if t["homeAway"] == "home")
                away = next(t for t in teams if t["homeAway"] == "away")

                # Converte data UTC para datetime
                formatodata = datetime.fromisoformat(competition["date"].replace("Z", "+00:00"))

                # Converte para horário de Brasília
                date_br = formatodata.astimezone(fuso)

                jogos.append({
                    "Mandante": home['team']['displayName'],
                    "Visitante": away['team']['displayName'],
                    "Data/Hora": date_br.strftime('%d/%m/%Y %H:%M'),
                    "Estádio": competition['venue']['fullName']
                })
    else:
        print(f"Erro: {response.status_code}, impossível obter retorno")

    return jogos