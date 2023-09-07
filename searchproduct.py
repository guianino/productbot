import requests
from bs4 import BeautifulSoup
import gzip
import brotli
from io import BytesIO

#Requisação do site 
link = "https://www.americanas.com.br/busca/haskell?brand=acom"  

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

response = requests.get(link, headers=headers)

#Descomprimindo o conteúdo
if 'Content-Encoding' in response.headers and response.headers['Content-Encoding'] == 'gzip':
    try:
        content = gzip.decompress(response.content)
    except gzip.BadGzipFile:
        try:
            content = brotli.decompress(response.content)
        except brotli.error:
            content = response.text
else:
    content = response.text

#Transformando o HTML em dados legiveis com BeautifulSoup
site = BeautifulSoup(content, "html.parser")
searchproduct = site.find_all("h3", class_="product-name__Name-sc-1shovj0-0 gUjFDF")
searchprice = site.find_all("span", class_="src__Text-sc-154pg0p-0 price__PromotionalPrice-sc-h6xgft-1 ctBJlj price-info__ListPriceWithMargin-sc-1xm1xzb-2 liXDNM")
searchurl = site.find_all("a", class_="inStockCard__Link-sc-1ngt5zo-1 JOEpk")

#Tratando dados para serem utilizados
nameproduct = [i.text for i in searchproduct] 
priceproductstr = [i.text for i in searchprice]
url= [element.get("href") for element in searchurl]


def remove_simbolos(item):
    return float(item.replace("R$", "").replace(",","."))

pricefloat = [remove_simbolos(item) for item in priceproductstr]


dbex = {"Shampoo Cavalo Forte 500ml": 60, "Condicionador 0Murumuru 300ml": 30, "Mandioca": 300}
dbex_dict = dict(dbex)

#Algoritimo de verificação do preço
values = []
for i, product in enumerate(nameproduct):
    if 'Shampoo' in product and "Cavalo Forte" in product and "300ml" in product:
        if pricefloat[i] < 2000:
            values.append("americanas.com.br" + url[i])

    if 'Shampoo' in product and "Murumuru" in product and "300ml" in product:
        if pricefloat[i] < 2000:
            values.append("americanas.com.br" + url[i])

    if 'Condicionador' in product and "Cavalo Forte" in product and "300ml" in product:
        if pricefloat[i] < 2000:
            values.append("americanas.com.br" + url[i])



print(values)








