from playwright.sync_api import sync_playwright
from scrapper import scrape_cards

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(
        viewport={"width": 1366, "height": 768},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
    )

    page = context.new_page()

    page.goto( #Link copiado do navegador, com os filtros de busca já aplicados
        "https://www.zapimoveis.com.br/aluguel/apartamentos/sp+cotia/?onde=%2CSão+Paulo%2CCotia%2C%2C%2C%2C%2Ccity%2CBR>Sao+Paulo>NULL>Cotia%2C-23.602694%2C-46.919476%2C&tipos=apartamento_residencial%2Ccasa_residencial%2Ccondominio_residencial%2Ccasa-vila_residencial"
    )

    page.wait_for_selector(
        '[data-cy="rp-cardProperty-location-txt"]',
        timeout=15000
    )

    page.wait_for_timeout(3000) #Timeout para garantir que o conteúdo seja carregado completamente

    cards = page.locator(
        '[data-cy="rp-property-cd"]'
    )
    print("Cards:", cards.count())

    print(
        "Localizações:",
        page.locator(
            '[data-cy="rp-cardProperty-location-txt"]'
        ).count()
    )
    
    scrape_cards(cards)

    browser.close()