# membuat daftar belanjaan
shopping_list = {
    "apel": 2.50,
    "pisang": 1.50,
    "jeruk": 3.00,
    "anggur": 5.00
}

# menghitung total harga
total_price = 0
for item, price in shopping_list.items():
    total_price += price

# menampilkan total harga
print("Total harga belanjaan:", total_price)
