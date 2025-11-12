from flask import Flask, render_template
from flask import request
import json
import os
import csv

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
    path_json = os.path.join(app.root_path, 'data', 'items.json')
    with open(path_json, 'r', encoding="utf-8") as f:
        data = json.load(f)
    item_list = data.get('items', [])

    return render_template('items.html', items=item_list)


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    data = []

    if source == "json":
        path = os.path.join(app.root_path, 'data', 'products.json')
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

    elif source == "csv":
        path = os.path.join(app.root_path, 'data', 'products.csv')
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                data.append(row)
    else:
        return render_template(
            'product_display.html',
            products=[],
            error="Wrong source")

    # filtrage si id donné
    if product_id is not None:
        data = [p for p in data if p['id'] == product_id]
        if not data:
            return render_template(
                'product_display.html',
                products=[],
                error="Product not found")

    return render_template(
        'product_display.html',
        products=data,
        error=None)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
