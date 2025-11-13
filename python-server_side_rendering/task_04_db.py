from flask import Flask, render_template
from flask import request
import json
import os
import csv
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    path_json = os.path.join(app.root_path, 'items.json')
    try:
        with open(path_json, 'r', encoding="utf-8") as f:
            data = json.load(f)
            items = data.get('items', [])
    except (FileNotFoundError, KeyError):
        items = []
    return render_template('items.html', items=items)

def fetch_from_sqlite():
    items = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            items.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": float(row[3])
            })
        conn.close()
    except sqlite3.Error as e:
        print("Erreur SQLite :", e)
        items = []
    return items

@app.route('/products')
def products():
    source = request.args.get('source', 'sql')
    id = request.args.get('id')
    items = []
    message = None

    if source in ['json', 'csv', 'sql']:
        try:
            if source == 'json':
                filename = 'products.json'
                with open(filename, 'r', encoding="utf-8") as f:
                    items = json.loads(f.read())

            elif source == 'csv':
                filename = 'products.csv'
                with open(filename, 'r', encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    for item in reader:
                        item["id"] = int(item["id"])
                        item["price"] = float(item["price"])
                        items.append(item)

            elif source == 'sql':
                items = fetch_from_sqlite()

            if id:
                id = int(id)
                valid = []
                for item in items:
                    valid.append(item["id"])

                if id not in valid:
                    message = "Product not found"

        except Exception as e:
            print("Erreur :", e)
            message = "Error loading data"

    else:
        message = "Wrong source"

    return render_template('product_display.html', items=items, id=id, message=message)    

if __name__ == '__main__':
    app.run(debug=True, port=5000)
