def pretty_price(price, cents):
    if cents >= 1:
        cents /= 100
    else:
        cents = cents
    final_price = price + cents
    final_price = float(final_price)
    print(final_price)

pretty_price(8, 0)
pretty_price(2, .99)
pretty_price(3, 89)
pretty_price(3, 1)
