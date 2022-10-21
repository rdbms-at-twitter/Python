base_price = 100
tax_rate = 1.1

def calc_price_including_tax(price, tax):
    return int(price*tax)

if __name__ == '__main__':
    print(f'{calc_price_including_tax(price=base_price, tax=tax_rate)}円')
          