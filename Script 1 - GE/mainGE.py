from coleta import coletar_partidas_brasileirao
from tratamento import tratar_partidas
from exportacao import exportar_csv

def main():
    print("Iniciando coleta dos jogos do Brasileirão...\n")
    dados = coletar_partidas_brasileirao(headless=True)
    df = tratar_partidas(dados)

    exportar_csv(df)
  

    print(f"\nProcesso finalizado! Próximos jogos:\n{df}")

if __name__ == "__main__":
    main()