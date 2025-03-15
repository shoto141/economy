def get_prices():
    prices = {}
    while True:
        store = input("Введите название магазина или 'стоп' для завершения: ")
        if store.lower() == 'стоп':
            break
        price = float(input(f"Введите цену товара в магазине '{store}': "))
        prices[store] = price
    return prices

def calculate_savings(prices):
    min_price = min(prices.values())
    savings = {store: price - min_price for store, price in prices.items() if price > min_price}
    return savings

def display_savings(savings):
    if not savings:
        print("Нет экономии по сравнению с самым дешевым магазином.")
    else:
        print("Вы можете сэкономить следующие суммы в магазинах:")
        for store, saving in savings.items():
            print(f"{store}: сэкономите {saving:.2f} руб.")

def main():
    print("Добро пожаловать в программу расчета экономии на покупках!")
    prices = get_prices()
    savings = calculate_savings(prices)
    display_savings(savings)

if __name__ == "__main__":
    main()