from coffee import Coffee
from customer import Customer


class Order:
    
    def __init__(self, customer, coffee, price) -> None:
        #initialized with a Customer instance, a Coffee instance, and a price
        self.customer = customer
        self.coffee = coffee
        self.price = price
        
        # Automatically add this order to the customer's and coffee's order lists
        self.customer.add_order(self)
        self.coffee.add_order(self)
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        #should not be able to change after the coffee is instantiated
        if hasattr(self, '_price'):
            raise AttributeError("Cannot change the price after the order is instantiated")
        #conditions to set price
        if isinstance(value, float) and (1.0 <= float(value) <= 10.0):
            self._price = float(value)
        else:
            raise Exception("Price must be a float and between 1.0 and 10.0")
        
        
    #property customer
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        #conditions to set customer
        if isinstance (value, Customer):
            self._customer = value
        else:
            raise Exception("Customer must be of type Customer")
        
    #property coffee        
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        #conditions to set coffee
        if isinstance (value, Coffee):
            self._coffee = value
        else:
            raise Exception("Coffee must be of type Coffee")