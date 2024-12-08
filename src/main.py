import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from flask import Flask, render_template
from scraping import scrape_data
from src import app

app = Flask(__name__)

@app.route("/")
def home():
    # Ejecutar el scraping
    data = scrape_data()
    # Convertir DataFrame a diccionario para pasar a la plantilla
    results = data.to_dict(orient="records")
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)