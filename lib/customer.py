class Customer:
    #list to store all customer instances
    all = []
    
    def __init__(self, name) -> None:
        #initialize name and list to store orders associated to a customer
        self.name = name
        self._orders = []
        Customer.all.append(self)
        
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        #conditions for setting name attr
        if isinstance(value, str) and (1 <= len(value) <= 15):
            self._name = value
        else:
            raise Exception("Name must be a string and between 1 and 15 characters")
    
    #method to add orders to the orders list
    def add_order(self, order):
        from order import Order
        if isinstance(order, Order):
            self._orders.append(order)
        else:
            raise Exception("Order must be of type Order")
        
    #method to view orders associated to a customer
    def orders(self):
        orders = [f'{order.coffee.name} {order.price}' for order in self._orders ]
        return f'List of orders : {orders}'
    
    #method to return a unique list of all coffees a customer has ordered using set
    def coffees(self):
        unique_coffees = set(order.coffee.name for order in self._orders)
        return f'List of customers : {list(unique_coffees)}'
    
    #method to create and return a new Order instance
    def create_order(self, coffee, price):
        from order import Order
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise Exception("coffee must be an instance of the Coffee class.")
        if not isinstance(price, float) and (1.0 <= float(price) <= 10.0):
            raise Exception("Price must be a float and between 1.0 and 10.0")
        
        order = Order(customer=self, coffee=coffee, price=price)
        
        # Add the order to the customer and coffee
        self.add_order(order)
        coffee.add_order(order)
    
        return order
    
    #class method to determine which customer instance has spent the most money on the coffee instance provided as argument
    @classmethod
    def most_aficionado(cls, coffee):
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise Exception("coffee must be an instance of Cofffee class")
        
        max_spent = 0
        aficionado = None
        
        for customer in cls.all:
            #sum up all orders for the given coffee for each customer and determine who spent the most
            total_spent = sum(order.price for order in customer._orders if order.coffee == coffee)
            #compare the total spending for each customer and returns the customer with the highest spending
            if total_spent > max_spent:
                max_spent = total_spent
                aficionado = customer
        
        return f'{aficionado.name} is the {coffee.name} coffee aficionado'
            

        