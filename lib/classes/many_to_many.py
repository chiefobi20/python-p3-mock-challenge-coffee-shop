class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def get_coffee_name(self):
        return self._name

    @get_coffee_name.setter
    def name(self, coffee_name_value):
        if (not hasattr(self, 'name')) and (type(coffee_name_value) == str) and (len(coffee_name_value)>= 3):
            self._name = coffee_name_value

    def orders(self):
        return [coffee for order in Order.all if order.coffee is self]

    def customers(self):
        pass

    def num_orders(self):
        pass

    def average_price(self):
        pass

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name_getter(self):
        return self.name

    @name_getter.setter
    def name(self, name_value):
        if (type(name_value) == str) and (1 <=len(name_value) <=15):
            self.name = name_value

    def orders(self):
        pass

    def coffees(self):
        pass

    def create_order(self, coffee, price):
        pass

class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if(type(value) is float) and (not hasattr(self, 'price')) and (1.0 <= 10.0):
            self.price = value

    @property
    def customer_getter(self):
        return self._customer

    @customer_getter.setter
    def customer(self, value):
        if type(value) == Customer:
            self._customer = value

    @property
    def coffee_getter(self):
        return self._coffee

    @coffee_getter.setter
    def coffee(self, value):
        if isinstance(value, Coffee):
            self.coffee = value
