from playwright.sync_api import sync_playwright

def scrape_cards(cards):

    for i in range(cards.count()):

        card = cards.nth(i)

        descricao = card.locator(
            '[data-cy="rp-cardProperty-location-txt"]'
        ).text_content()

        descricao = descricao.strip() if descricao else "N/A" #Remoção de espaços em branco e tratamento de valores nulos

        preco = card.locator(
            '[data-cy="rp-cardProperty-price-txt"]'
        ).text_content()

        preco = preco.strip() if preco else "N/A" #Remoção de espaços em branco e tratamento de valores nulos

        area = card.locator(
            '[data-cy="rp-cardProperty-propertyArea-txt"]'
        ).text_content()

        area = area.strip() if area else "N/A" #Remoção de espaços em branco e tratamento de valores nulos

        quartos = card.locator(
            '[data-cy="rp-cardProperty-bedroomQuantity-txt"]'
        ).text_content()

        quartos = quartos.strip() if quartos else "N/A" #Remoção de espaços em branco e tratamento de valores nulos

        banheiros = card.locator(
            '[data-cy="rp-cardProperty-bathroomQuantity-txt"]'
        ).text_content()

        banheiros = banheiros.strip() if banheiros else "N/A" #Remoção de espaços em branco e tratamento de valores nulos

        vagas = card.locator(
            '[data-cy="rp-cardProperty-parkingSpacesQuantity-txt"]'
        ).text_content()

        vagas = vagas.strip() if vagas else "N/A" #Remoção de espaços em branco e tratamento de valores nulos

        print(f"Índice {i}") #Exibição do índice para referência (início em 0)
        print(descricao)
        print(preco)
        print(area)
        print(quartos)
        print(banheiros)
        print(vagas)