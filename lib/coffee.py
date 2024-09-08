class Coffee:
    
    def __init__(self, name) -> None:
        #initialize name and list to store orders associated to a customer
        self.name = name
        self._orders = []
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name (self, value):
        #should not be able to change after the coffee is instantiated
        if hasattr(self, '_name'):
            raise AttributeError("Cannot change the name after the coffee name is instantiated")
        #conditions to set name
        if isinstance(value, str) and (len(value) >= 3):
            self._name = value
        else:
            raise Exception("Name must be a string and greater or equal to 3 characters")
    
    #method to add orders to the orders list
    def add_order(self,order):
        from order import Order
        if isinstance(order, Order):
            self._orders.append(order)
        else:
            raise Exception("Order must be of type Order")
        
        
    #method to view orders associated to a customer    
    def orders(self):
        orders = [f'{order.customer.name} {order.price}' for order in self._orders ]
        return f'List of orders : {orders}'
    
    
    #method to return a unique list of all customers who have ordered a particular coffee.
    def customers(self):
        unique_customers = set(order.customer.name for order in self._orders)
        return f'List of customers : {list(unique_customers)}'
    
    #method to return the total number of times a coffee has been ordered
    def num_orders(self):
        num_of_orders = len(self._orders)
        return f'Number of orders : {num_of_orders}'
    
    #method that returns the average price for a coffee based on its orders
    def average_price(self):
        total_price = sum(order.price for order in self._orders)
        total_orders = len(self._orders)
        if total_orders == 0:
            return 0
        else:
            return f'Average price : {total_price / total_orders}'