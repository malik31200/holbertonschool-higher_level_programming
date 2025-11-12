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
    source = request.args.get('source', 'json')
    product_id = request.args.get('id')
    items = []
    message = None

    if source in ['json', 'csv']:
        path = os.path.join(app.root_path, 'data', f'products.{source}')
        try:
            with open(path, 'r', encoding='utf-8') as f:
                if source == 'json':
                    items = json.load(f)
                else:
                    reader = csv.DictReader(f)
                    for row in reader:
                        row['id'] = int(row['id'])
                        row['price'] = float(row['price'])
                        items.append(row)
        except FileNotFoundError:
            message = "File not found"
        except json.JSONDecodeError:
            message = "Invalid JSON file"
    else:
        message = "Wrong source"


    if product_id and items:
        try:
            product_id = int(product_id)
            filtered_items = [
                item for item in items if int(item["id"]) == product_id]
            if not filtered_items:
                message = "Product not found"
            items = filtered_items
        except ValueError:
            message = "Invalid ID"
            items = []

    return render_template(
        'product_display.html',
        items=items,
        message=message)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
