base_price: int = 100
tax_rate: float = 1.1

## Type Annotation is only information and it is not mandatory.

def calc_price_including_tax(price: int, tax: float) -> int:
    return int(price*tax)

if __name__ == '__main__':
    print(f'{calc_price_including_tax(price=base_price, tax=tax_rate)}円')
          