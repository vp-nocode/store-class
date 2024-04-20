
class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = dict()

    def add_product(self, name, price):
        self.items.update({name: float(price)})
        print(f"Товар {name} по цене {price:.2f} добавлен")

    def delete_product(self, name):
        result = self.items.pop(name, None)
        if result is None:
            print(f"Товар {name} не найден")
        else:
            print(f"Товар {name} удален")
        return result

    def update_price(self, name):
        if name not in self.items:
            print(f"Товар {name} не найден")
        else:
            try:
                new_price = float(input(f"Введите новую цену для {name} (текущая цена {self.items[name]}): "))
                self.items[name] = new_price
                print(f"У товара {name} обновлена цена на {new_price}")
            except ValueError:
                print("Неправильная цена. Повторите ввод.")

    def show_store_info(self):
        print(f"Магазин {self.name} расположен по адресу {self.address}")
        print(f"Ассортимент:")
        for name, price in self.items.items():
            print(f"Товар {name} по цене {price:.2f}")


store1 = Store("Пятерочка", "ул. Пушкина, д. 10")
store2 = Store("Магнит", "ул. Труда, д. 1")
store3 = Store("Ашан", "ул. Колхозников, д. 21")

store1.add_product("Молоко", 120)
store1.add_product("Сыр", 250)
store1.add_product("Макароны", 150)
store1.show_store_info()

store2.add_product("Кефир", 65)
store2.add_product("Яблоки", 135)
store2.show_store_info()

store3.add_product("Колбаса", 300)
store3.add_product("Хлеб", 50)
store3.show_store_info()

store1.delete_product("Молоко")
store1.show_store_info()

store1.update_price("Сыр")
store1.show_store_info()

store1.delete_product("Кефир")
store1.update_price("Кефир")
