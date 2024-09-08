Below is a quick overview of the key relationships and functionalities:

##Classes and Their Roles


#Customer
Stores all instances: Customer.all keeps track of all customer instances.

Properties:
name: Customers have names between 1 and 15 characters.

Methods:
add_order(): Adds an order to the customer's list of orders.
orders(): Returns all orders associated with the customer.
coffees(): Returns a unique list of all coffees the customer has ordered.
create_order(): Creates an order for a given coffee and price.
most_aficionado(): Class method to find the customer who has spent the most on a specific coffee.


#Coffee
Properties:
name: Coffees have names of at least 3 characters, and the name cannot be changed after the coffee is instantiated.

Methods:
add_order(): Adds an order to the coffee's list of orders.
orders(): Returns all orders associated with the coffee.
customers(): Returns a unique list of customers who ordered the coffee.
num_orders(): Returns the total number of times the coffee has been ordered.
average_price(): Returns the average price of the coffee based on its orders.


#Order
Stores all instances: Order.all keeps track of all order instances.

Properties:
customer: Each order is associated with a customer.
coffee: Each order is associated with a coffee.
price: Price of the order between 1.0 and 10.0 (in float), immutable once set.