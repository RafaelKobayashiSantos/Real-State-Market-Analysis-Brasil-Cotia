def get_text(card, selector):

    locator = card.locator(selector)

    if locator.count() > 0:

        texto = locator.text_content()

        return texto.strip() if texto else "N/A"

    return "N/A"


def scrape_cards(cards, dataFrame):

    for i in range(cards.count()):

        card = cards.nth(i)

        descricao = get_text(
            card,
            '[data-cy="rp-cardProperty-location-txt"]'
        )

        preco = get_text(
            card,
            '[data-cy="rp-cardProperty-price-txt"]'
        )

        area = get_text(
            card,
            '[data-cy="rp-cardProperty-propertyArea-txt"]'
        )

        quartos = get_text(
            card,
            '[data-cy="rp-cardProperty-bedroomQuantity-txt"]'
        )

        banheiros = get_text(
            card,
            '[data-cy="rp-cardProperty-bathroomQuantity-txt"]'
        )

        vagas = get_text(
            card,
            '[data-cy="rp-cardProperty-parkingSpacesQuantity-txt"]'
        )

        dataFrame["descricao"].append(descricao)
        dataFrame["preco"].append(preco)
        dataFrame["area"].append(area)
        dataFrame["quartos"].append(quartos)
        dataFrame["banheiros"].append(banheiros)
        dataFrame["vagas"].append(vagas)

        print(f"Índice {i}")
        print(descricao)
        print(preco)
        print(area)
        print(quartos)
        print(banheiros)
        print(vagas)
        print("-" * 50)

    return dataFrame