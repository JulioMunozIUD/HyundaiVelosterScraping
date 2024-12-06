import pytest
from src.scraping import scrape_data
import sys
import os

# Agregar el directorio raíz del proyecto al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


def test_scrape_data():
    df = scrape_data()
    # Verificar que el DataFrame no esté vacío
    assert not df.empty, f"El DataFrame está vacío: {df}"
    # Verificar columnas esperadas
    expected_columns = ["Título", "Características", "Precio", "Urls"]
    assert list(df.columns) == expected_columns, f"Columnas incorrectas: {df.columns}"