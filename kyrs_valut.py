import requests
from  bs4 import BeautifulSoup

def my_kyrs():
    url_kyrs = 'https://bank.gov.ua/ua/markets/exchangerates'
    html_minfin = requests.get(url_kyrs).text
    return html_minfin


def usd():
    soup = BeautifulSoup(my_kyrs(), 'html.parser')
    div = soup.findAll('tr')[8].text
    if div[64:71] == '0':
        value = '00.000'
    else:
        val = (div[64:71]).replace(',', '.')
        value = float(val) * 1.0337
    def key():
        key = 'USD'
        return key
    if div:
        return f'{key()}: {round(value, 2)} грн.'
    else:
        return 'Неможливо отримати дані. Очікування...'


def euro():
    soup = BeautifulSoup(my_kyrs(), 'html.parser')
    div = soup.findAll('tr')[9].text
    if div[64:71] == '0':
        value = '00.000'
    else:
        val = (div[59:66]).replace(',', '.')
        value = float(val) * 1.0318
    def key():
        key = 'EUR'
        return key
    if div:
        return f'{key()}: {round(value, 2)} грн.'
    else:
        return 'Неможливо отримати дані. Очікування...'


def pln():
    soup = BeautifulSoup(my_kyrs(), 'html.parser')
    div = soup.findAll('tr')[12].text
    if div[64:71] == '0':
        value = '00.000'
    else:
        val = (div[60:66]).replace(',', '.')
        value = float(val) * 1.0318
    def key():
        key = 'PLN'
        return key
    if div:
        return f'{key()}: {round(value, 2)} грн.'
    else:
        return 'Неможливо отримати дані. Очікування...'

def bitcoin():
    btc = 'https://www.binance.com/ru-UA/price/bitcoin'
    html = requests.get(btc).text
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.findAll('div', class_='css-zo19gu')
    key = 'BTC'
    if div:
        # y = str(div)[-17:-7]
        # x = increase(y)
        return f'{key}: {str(div)[-17:-7]}'
    else:
        return 'Неможливо отримати дані. Очікування...'

def ethereum():
    eth = 'https://www.binance.com/ru-UA/price/ethereum'
    html = requests.get(eth).text
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.findAll('div', class_='css-12ujz79')
    key = 'ETH'
    if div:
        # y = str(div)[-17:-7]
        # x = increase(y)
        return f'{key}: {str(div)[-17:-7]}'#   {x}'
    else:
        return 'Неможливо отримати дані. Очікування...'

    # def increase(self):
    #     c = open('kyrs_valyt.txt', 'r')
    #     y = [line.strip().replace('$', '').replace(',', '') for line in c]
    #     c.close()
    #     if len(y) < 6:
    #         x = open('kyrs_valyt.txt', 'a', encoding='utf-8')
    #         x.write(self.strip().replace('$', '').replace(',', '') + '\n')
    #         x.close()
    #     if len(y) >= 6:
    #         y.remove(y[0])
    #         w = open('kyrs_valyt.txt', 'w', encoding='utf-8')
    #         for i in y:
    #             w.write(str(i) + '\n')
    #         w.close()
    #     if float(y[-2]):
    #         q = float(y[-1]) - float(y[-2])
    #     else:
    #         q = 0
    #     if q >= 0:
    #         return ('+' + str(round(q, 3)))
    #     else:
    #         return (str(round(q, 3)))
