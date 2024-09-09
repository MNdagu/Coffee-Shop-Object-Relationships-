from customer import Customer
from coffee import Coffee
from order import Order


# Create some customers
alice = Customer("Alice")
bob = Customer("Bob")
john = Customer("John")

# Create some coffees
espresso = Coffee("Espresso")
latte = Coffee("Latte")
black = Coffee("Black")

# Create orders
order1 = alice.create_order(espresso, 4.50)
order2 = bob.create_order(espresso, 5.00)
order3 = alice.create_order(latte, 3.75)
order4 = Order(john, black, 3.50)

print(order4.customer.name)  
print(order4.coffee.name)    
print(order4.price)
     
# Check the number of orders for a coffee
print(espresso.num_orders()) 

# Get unique customers who ordered a specific coffee
print(espresso.customers())  

# Check the average price for coffee1
print(espresso.average_price())  

# Find the customer who spent the most on coffee1
print(Customer.most_aficionado(black)) 

print(alice.orders())
print(alice.coffees())

print(latte.orders())
print(latte.customers())
print(black.num_orders())
print(latte.average_price())

