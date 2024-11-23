import pytest
from src.main import scrape_data

def test_scrape_data():
    df = scrape_data()
    # Verificar que el DataFrame no está vacío
    assert not df.empty, "El DataFrame está vacío"
    # Verificar que las columnas esperadas existen
    assert all(col in df.columns for col in ["Título", "Características", "Precio", "Url"]), "Faltan columnas en el DataFrame"