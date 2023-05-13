from flask import Flask, render_template, request
from templates import home_html, products_html, cart_html, checkout_html

app = Flask(__name__)

# Route untuk halaman utama
@app.route('/')
def home():
    return home_html

# Route untuk halaman produk
@app.route('/products')
def products():
    products = [
        {
            'id': 1,
            'name': 'Product 1',
            'description': 'This is product 1',
            'price': 100000
        },
        {
            'id': 2,
            'name': 'Product 2',
            'description': 'This is product 2',
            'price': 200000
        },
        {
            'id': 3,
            'name': 'Product 3',
            'description': 'This is product 3',
            'price': 300000
        }
    ]
    return render_template(products_html, products=products)

# Route untuk halaman keranjang belanja
@app.route('/cart', methods=['GET', 'POST'])
def cart():
    if request.method == 'POST':
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        # Lakukan proses penambahan produk ke keranjang
        return 'Produk telah ditambahkan ke keranjang'

    # Lakukan proses penampilan keranjang belanja
    return cart_html

# Route untuk halaman proses pembayaran
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # Lakukan proses pembayaran
        return 'Pembayaran telah berhasil'

    # Lakukan proses penampilan halaman pembayaran
    return checkout_html

if __name__ == '__main__':
    app.run(debug=True)
