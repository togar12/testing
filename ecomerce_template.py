home_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Home Page</title>
</head>
<body>
    <h1>Selamat Datang di Toko Online Kami</h1>
    <p>Kami menyediakan berbagai produk berkualitas dengan harga terjangkau.</p>
    <a href="/products">Lihat produk kami</a>
</body>
</html>
"""

products_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Produk</title>
</head>
<body>
    <h1>Daftar Produk</h1>
    <ul>
        <li>Produk 1</li>
        <li>Produk 2</li>
        <li>Produk 3</li>
    </ul>
    <a href="/">Kembali ke halaman utama</a>
</body>
</html>
"""

cart_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Keranjang Belanja</title>
</head>
<body>
    <h1>Keranjang Belanja</h1>
    <ul>
        <li>Produk 1 - Harga: Rp 100.000</li>
        <li>Produk 2 - Harga: Rp 50.000</li>
    </ul>
    <p>Total Harga: Rp 150.000</p>
    <a href="/">Kembali ke halaman utama</a>
    <a href="/checkout">Lanjut ke proses pembayaran</a>
</body>
</html>
"""

checkout_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Proses Pembayaran</title>
</head>
<body>
    <h1>Proses Pembayaran</h1>
    <form>
        <label for="name">Nama:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="address">Alamat:</label>
        <textarea id="address" name="address"></textarea><br><br>
        <label for="payment_method">Metode Pembayaran:</label>
        <select id="payment_method" name="payment_method">
            <option value="transfer_bank">Transfer Bank</option>
            <option value="kartu_kredit">Kartu Kredit</option>
            <option value="cod">Cash on Delivery</option>
        </select><br><br>
        <button type="submit">Bayar</button>
    </form>
    <a href="/cart">Kembali ke keranjang belanja</a>
</body>
</html>
"""
