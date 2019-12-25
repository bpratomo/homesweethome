def convert_currency_text_to_number(currency_text):
    currency_number = float(currency_text.replace('€','').replace(',',''))
    return currency_number

def convert_area_text_to_number(area_text):
    area_number = float(area_text.replace(' m²','').replace(',',''))
    return area_number