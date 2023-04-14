# Your code below:
#lists
toppings = ["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms",]
prices = [2 ,6 ,1 ,3 ,2 ,7 ,2 ]
pizza_and_prices = [
  [2,	"pepperoni"],
  [6,	"pineapple"],
  [1,	"cheese"],
  [3,	"sausage"],
  [2,	"olives"],
  [7,	"anchovies"],
  [2,	"mushrooms"]
]
#Code
num_two_dollar_slices = prices.count(2)
num_pizzas = len(toppings)
pizza_and_prices.sort()
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]
pizza_and_prices.pop()
pizza_and_prices.append([2.5, "peppers"])
three_cheapest = pizza_and_prices[:3]
#Feedback
print(num_pizzas)
print(num_two_dollar_slices)
print (priciest_pizza)
print(cheapest_pizza)
print(pizza_and_prices)
print(three_cheapest)
print("We sell " + str(num_pizzas) + " different kinds of pizza!")
