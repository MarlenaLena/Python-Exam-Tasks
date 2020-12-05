productsWithPrices = {}
productsList = []
products: str
budget: float = 100

products = input('Podaj produkty oddzielając je przecinkiem: ')
productsList = set(products.split(','))

for product in productsList:
    try:
        price: float = float(
            input('Podaj cenę dla produktu ' + product + ' : '))
        productsWithPrices[product.upper()] = price
    except:
        productsWithPrices[product.upper()] = 0

if sum(productsWithPrices.values()) <= budget:
    print('Jesteś w stanie zakupić wszystkie produkty')
else:
    print('Niestety nie starczy ci pieniędzy na takie zakupy')
