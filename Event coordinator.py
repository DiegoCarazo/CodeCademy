guests = {}
def read_guestlist(file_name):
  text_file = open(file_name,'r')
  while True:
    line_data = text_file.readline().strip().split(",")
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    v = yield name

# To print the fist 10 names
guestlist = read_guestlist("guest_list.txt")
for a in range(1,10):
  print(next(guestlist))

# Adding Jane
print(guestlist.send('Janet, 35'))
print('-------') # for separation porpuses

# Printing the rest of the names
for b in guestlist:
  print('rest of the users: ' + b)
print('------')# for separation porpuses
# The age of the customers
for guest in guests:
  if guests[guest] >= 21: 
    print('Users over 21: ' + guest)

print('-----')# for separation porpuses

# Connected Generators & Generator Pipelines

def table_1():
  yield ("Chichen", "Table 1", "Chair {}".format(a))

def table_2():
  yield ("Beff", "Table 2", "Chair {}".format(a))

def table_3():
  yield ("Fish", "Table 3", "Chair {}".format(a))

def tables():
  yield table_1()
  yield table_2()
  yield table_3()

tables_info = tables()

# Assing the tables and chairs
def assign_tables(list_of_guests):
  for name in list_of_guests:
    yield (name, next(tables_info))

guest_assignment = assign_tables(guests)
for person in guest_assignment:
  print(person)
