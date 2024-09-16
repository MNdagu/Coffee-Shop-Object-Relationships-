<h1>COFFEE SHOP OBJECT RELATIONSHIP</h1>

<small>Below is a quick overview of the key relationships and functionalities:<small>

<h2>Classes and Their Roles</h2>


<h3>Customer</h3>
<p>
<strong>Stores all instances</strong>: Customer.all keeps track of all customer instances.

<strong>Properties:</strong>
name: Customers have names between 1 and 15 characters.

<strong>Methods:</strong>
<ul>
<li>add_order(): Adds an order to the customer's list of orders.</li>
<li>orders(): Returns all orders associated with the customer.</li>
<li>coffees(): Returns a unique list of all coffees the customer has ordered.</li>
<li>create_order(): Creates an order for a given coffee and price.</li>
<li>most_aficionado(): Class method to find the customer who has spent the most on a specific coffee.</li>
</ul>
</p>


<h3>Coffee</h3>

<p>
<strong>Properties:</strong>

name: Coffees have names of at least 3 characters, and the name cannot be changed after the coffee is instantiated.
</p>

<p>
<strong>Methods:</strong>
<ul>
<li>add_order(): Adds an order to the coffee's list of orders.</li>
<li>orders(): Returns all orders associated with the coffee.</li>
<li>customers(): Returns a unique list of customers who ordered the coffee.</li>
<li>num_orders(): Returns the total number of times the coffee has been ordered.</li>
<li>average_price(): Returns the average price of the coffee based on its orders.</li>
</ul>
</p>


<h3>Order</h3>
<p>
<strong>Stores all instances:</strong> Order.all keeps track of all order instances.

<strong>Properties:</strong>
<ul>
<li>customer: Each order is associated with a customer.</li>
<li>coffee: Each order is associated with a coffee.</li>
<li>price: Price of the order between 1.0 and 10.0 (in float), immutable once set.</li>
</ul>
</p>