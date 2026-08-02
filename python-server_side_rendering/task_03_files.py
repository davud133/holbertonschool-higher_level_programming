import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)


def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Validate source
    if source not in ('json', 'csv'):
        return render_template('product_display.html', error="Wrong source")

    # Read data from the correct file
    if source == 'json':
        data = read_json()
    else:
        data = read_csv()

    # Filter by id if provided
    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html', error="Product not found")

        data = [p for p in data if p['id'] == product_id]
        if not data:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
