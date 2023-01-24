def calculate_brutto(netto: float, vat: float) -> float:
    kwota_vat = netto * vat
    brutto = netto + kwota_vat
    return brutto

# Function that calculates brutto for netto and vat
# netto: value of netto
# vat: value of vat, like 0.23 for 23%
# return: value of brutto

netto = float(input('Jaka jest wartość netto?'))
vat = float(input('Jaka jest stawka vat?'))

brutto = calculate_brutto(netto, vat)
brutto = calculate_brutto(100, 0.23)
print(f'Wartość brutto wynosi {brutto}')


