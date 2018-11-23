
from owlready import *

onto_path.append("./owlready/doc/examples")

pizza_onto = get_ontology("http://www.co-ode.org/ontologies/pizza/pizza.owl").load()

class Pizza(Thing):
  def eat(self):
    print("Miam!")

class NonVegetarianPizza(Thing):
  def eat(self):
    print("Beurk! I'm vegetarian!")

test_pizza = pizza_onto.Pizza("test_pizza")

test_pizza.has_topping = [ pizza_onto.CheeseTopping(),
                           pizza_onto.TomatoTopping(),
                           pizza_onto.MeatTopping  () ]

print("Before reasoning:", test_pizza.__class__)

pizza_onto.sync_reasoner()

print("After reasoning:", test_pizza.__class__)

test_pizza.eat()
