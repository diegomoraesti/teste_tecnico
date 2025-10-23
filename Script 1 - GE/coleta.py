"""
Coleta as partidas do Brasileirão da proxima rodada no site do GE
by: Diego - 21/10/2025

"""
from playwright.sync_api import sync_playwright

print('\n\nIniciando pesquisa, por favor aguarde...\n')
def coletar_partidas_brasileirao(headless=True)-> list[str]:
    
    resultados = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        page = browser.new_page()

        # Vai até a página
        page.goto("https://ge.globo.com/futebol/brasileirao-serie-a/")

        # Localização da tabela de jogos do brasileirão via XPath da lista
        lista_xpath = '//*[@id="classificacao__wrapper"]/section/ul'

        
        page.wait_for_selector(f'xpath={lista_xpath}')

       
        itens = page.locator(f'{lista_xpath}/li/div')

        total = itens.count()
        print(f"Realizando captura das informações\n")

        for i in range(total):
            div = itens.nth(i)

            # Localização da informação dos jogos via metadados <meta itemprop="name"> e <meta itemprop="startDate">
            metas = div.locator('meta[itemprop="name"], meta[itemprop="startDate"]')

            nomes = []
            for j in range(metas.count()):
                content = metas.nth(j).get_attribute("content")
                if content:
                    nomes.append(content.strip())

            # Criar linha de partidas
            if len(nomes) == 2:
                partida = f"{nomes[0]} x {nomes[1]}"
            else:
                partida = " / ".join(nomes)

            resultados.append(partida)

        browser.close()

    return resultados