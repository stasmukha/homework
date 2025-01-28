class Product:
    def __init__(self, type, name, price):
        self.tyoe = type
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self, type, name, price):
        self.tyoe = type
        self.name = name
        self.price = price
        self.amount = 0
        
    def add (self, amount):
        if type(amount) == int or float:
            self.amount += amount
        
        else:
            raise ValueError('Incorrect type argument')
        
    def set_discount(self):
        for item in self.name:
            print(item)
        
    
        

p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)