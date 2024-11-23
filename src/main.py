from bs4 import BeautifulSoup
import requests
import pandas as pd

def scrape_data():
    r = requests.get('https://listado.mercadolibre.com.co/hyundai-veloster#D[A:hyundai%20veloster]')
    soup = BeautifulSoup(r.content, 'html.parser')

    titulos = [i.text for i in soup.find_all('h2', attrs={"class": "ui-search-item__title"})]
    urls = [i.get('href') for i in soup.find_all('a', attrs={"class": "ui-search-link"})]
    precios = [i.text for i in soup.find_all('span', attrs={"class": "andes-money-amount__fraction"})]
    atributos_p = [i.text for i in soup.find_all('li', attrs={"class": "ui-search-card-attributes__attribute"})]
    atributos = [" - ".join(atributos_p[i:i+2]) for i in range(0, len(atributos_p), 2)]

    min_length = min(len(titulos), len(precios), len(urls), len(atributos))
    df = pd.DataFrame({
        "Título": titulos[:min_length],
        "Características": atributos[:min_length],
        "Precio": precios[:min_length],
        "Url": urls[:min_length],
    })
    return df

if __name__ == "__main__":
    data = scrape_data()
    print(data)