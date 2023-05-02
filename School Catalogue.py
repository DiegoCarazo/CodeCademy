class School:
  
  def __init__(self, name, level, numberOfStudent):
    self.name = name
    self.level = level
    self.numberOfStudent = numberOfStudent

  def getName(self):
    return self.name

  def getLevel(self):
    return self.level

  def getNumberOfStudents(self):
    return self.numberOfStudent

  def setNumberOfStudents(self, new_amount):
    self.numberOfStudents = new_amount

  def __repr__(self):
    return f"A {self.level} school name {self.name} with {self.numberOfStudent} students."

a = School("Codecademy", "high", 100)
print(a)
print(a.getName())
print(a.getLevel())
a.setNumberOfStudents(200)
print(a.getNumberOfStudents())

# Create the PrimarySchool class
class PrimarySchool(School):
  def __init__(self, name, numberOfStudent, pickupPolicy):
    super().__init__(name, 'Primary', numberOfStudent)
    self.pickupPolicy = pickupPolicy
  
  def getPickupPolicy(self):
    return self.pickupPolicy
  
  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + "The pickup policy is {pickupPolicy}".format(pickupPolicy = self.pickupPolicy)

b = PrimarySchool("Codecademy", 300, "Pickup Allowed")
print(b.getPickupPolicy())
print(b)

#Create the highSchool class
class HighSchool(School):
  def __init__(self, name, numberOfStudent, sportsTeams):
    super().__init__(name, 'High', numberOfStudent)
    self.sportsTeams = sportsTeams
  
  def getSportsTeams(self):
    return self.sportsTeams
  
  def __repr__(self):
    parent = super().__repr__()
    return parent + f" information of our sport Team {self.sportsTeams}"


c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(c.getSportsTeams())
print(c)

class High(School):
  pass
