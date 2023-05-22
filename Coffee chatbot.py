def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()
  latte = order_latte()
  print("Alright, that's a {size} {drink_type}!".format(size = size, drink_type= drink_type))
  name = input('Can I get your name please?')
  print('Thanks, {name}! Your drink will be ready shortly.'.format(name= name))

def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message = "I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response."
    print(print_message)
    return get_size()
def get_drink_type():
  res = input("What type of drink would you like \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n")
  if res == 'a':
    return 'brewed coffee'
  if res == 'b':
    return 'mocha'
  if res == 'c':
    return 'latte'
  else:
    print_message = "I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response."
    print(print_message)
    return get_drink_type()

def order_latte():
  res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n")
  if res == 'a':
    return '2% milk'
  if res == 'b':
    return 'Non-fat milk'
  if res == 'c':
    'Soy milk'
  else:
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
    return order_latte()

coffee_bot()
