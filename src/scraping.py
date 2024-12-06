from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd

def scrape_data():
    r = requests.get('https://listado.mercadolibre.com.co/hyundai-veloster#D[A:hyundai%20veloster]')
    soup = BeautifulSoup(r.content, 'html.parser')

    titulos = soup.find_all('h2', attrs={"class":"poly-box poly-component__title"})
    titulos = [i.text for i in titulos]
    urls = soup.find_all('a', attrs={""})
    urls = [i.get('href') for i in urls]
    precio = soup.find_all('span', attrs={"class":"andes-money-amount andes-money-amount--cents-superscript"})
    precio = [i.text for i in precio]
    atributos_p = [i.text for i in soup.find_all('li', attrs={"class":"poly-attributes-list__item poly-attributes-list__separator"})]
    atributos = [" - ".join(atributos_p[i:i+2]) for i in range(0, len(atributos_p), 2)]

    min_length = min(len(titulos), len(precio), len(urls), len(atributos))
    titulos = titulos[:min_length]
    urls = urls[:min_length]
    precio = precio[:min_length]
    atributos = atributos[:min_length]

    df = pd.DataFrame({"Título":titulos,"Características":atributos, "Precio":precio,"Urls":urls})
    return df

if __name__ == "__main__":
    data = scrape_data()
    print(data)