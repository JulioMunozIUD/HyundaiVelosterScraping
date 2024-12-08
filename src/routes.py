from src import app
from flask import render_template
from src.scraping import scrape_data

@app.route("/")
def home():
    # Ejecutar el scraping
    data = scrape_data()
    # Convertir DataFrame a diccionario para pasar a la plantilla
    results = data.to_dict(orient="records")
    return render_template("index.html", results=results)