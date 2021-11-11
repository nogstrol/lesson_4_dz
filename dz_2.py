import requests


def currency_rates(val):
    site = requests.get('http://www.cbr.ru/scripts/XML_daily.asp.')
    content = site.content.decode(encoding=site.encoding)
    result = None
    if val not in content:
        return result
    else:
        for el in content.split(f'{val}')[1:]:
            for el_1 in el.split('</value>')[:1]:
                result = round(float(el_1.split('<Value>')[1].replace(',', '.')), 2)
                return f'Курс валюты: {result} руб.'


if __name__ == '__main__':
    code_val = str(input('Ведите валюту: '))
    print(currency_rates(code_val))
