from playwright.sync_api import sync_playwright
from scrapper import scrape_cards
from pipeline import clean_data

dataFrame = { "descricao": [], "preco": [], "area": [], "quartos": [], "banheiros": [], "vagas": [] }

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False  # importante para visualizar o que acontece
    )

    context = browser.new_context(
        viewport={"width": 1366, "height": 768},
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/137.0.0.0 Safari/537.36"
        )
    )

    page = context.new_page()

    url = (
        "https://www.zapimoveis.com.br/aluguel/casas/sp+barueri/"
        "?onde=%2CSão+Paulo%2CBarueri%2C%2C%2C%2C%2Ccity%2CBR>Sao+Paulo>NULL>Barueri%2C-23.503504%2C-46.878556%2C"
        "&tipos=casa_residencial"
    )

    page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=60000
        )

    page.wait_for_timeout(5000)

    for pagina in range(1, 4):

        print(f"\n===== PÁGINA {pagina} =====")

        print("URL atual:")
        print(page.url)

        print("\nTítulo:")
        print(page.title())

        total = page.locator(
            '[data-cy="rp-cardProperty-location-txt"]'
        ).count()

        print("\nTotal de anúncios encontrados:")
        print(total)

        if total > 0:
            print("\nPrimeiro anúncio:")

            texto = page.locator(
                '[data-cy="rp-cardProperty-location-txt"]'
            ).first.text_content()

            print(texto)
        
        page.mouse.wheel(0, 10000)

        page.wait_for_timeout(3000)

        cards = page.locator(
        '[data-cy="rp-property-cd"]'
        )

        scrape_cards(cards, dataFrame)

        page.locator(
            '[aria-label="próxima página"]'
        ).click()

        page.wait_for_timeout(5000)

    dados = clean_data(dataFrame) 
    dados.to_csv( "dados_imoveis.csv", index=False, encoding="utf-8-sig" )

    browser.close()