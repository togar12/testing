from flask import Flask, render_template, request

app = Flask(__name__)

# Route untuk halaman utama
@app.route('/')
def home():
    return render_template('home.html')

# Route untuk halaman produk
@app.route('/products')
def products():
    return render_template('products.html')

# Route untuk halaman keranjang belanja
@app.route('/cart')
def cart():
    return render_template('cart.html')

# Route untuk proses pembayaran
@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)
