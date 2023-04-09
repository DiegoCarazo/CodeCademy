weight = 41.5
Price_per_Pound = 0
Ground_Flat_Charge = 20
Ground_Flat_Charge_premium = 125
Drone_PPP = 0 

#Ground Shipping
if (weight <= 2):
  Price_per_Pound += 1.50
elif (weight >= 2) and (weight <= 6):
  Price_per_Pound += 3.00
elif (weight >= 6) and (weight <= 10):
  Price_per_Pound += 4.00
else:
    Price_per_Pound += 4.75
print("The Ground Shipping Cost is:")
print(Ground_Flat_Charge + (Price_per_Pound * weight))
#Ground Shipping Premium
print("Ground Shipping Premium:")
print(Ground_Flat_Charge_premium + (Price_per_Pound * weight))
#Drone Shipping
if (weight <= 2):
  Drone_PPP += 4.5
elif (weight >= 2) and (weight <= 6):
  Drone_PPP += 9.0
elif (weight >= 6) and (weight <= 10):
  Drone_PPP += 12.0
else:
    Price_per_Pound += 14.25
print("Drone Shipping:")
print(Drone_PPP * weight)
