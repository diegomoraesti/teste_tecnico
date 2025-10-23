from coleta import proximos_jogos_brasileirao
from tratamento import tratar_partidas
from exportacao import exportar_csv

def main():
    print("Iniciando coleta dos jogos do Brasileirão...\n")
    dados = proximos_jogos_brasileirao(headless=True)
    df = tratar_partidas(dados)

    exportar_csv(df)
    # exportar_excel(df)  # descomente se quiser exportar Excel

    print(f"\nProcesso finalizado! Próximos jogos:\n{df}")

if __name__ == "__main__":
    main()







