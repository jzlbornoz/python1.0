items = [{
    'product': 'shirt',
    'price': 120,
    'tax': 0.15,
}, {
    'product': 'pants',
    'price': 160,
    'tax': 0.3,
}, {
    'product': 'jacket',
    'price': 205,
    'tax': 0.2,
}]

prices = list(map(lambda item: item['price'] + item['tax'], items))

print(prices)
