class Car:
  name = ""
  kind = "car"
  color = ""
  value = 100.00
  def description(self):
    desc_string = "%s is a %s %s worth $%.2f." %(self.name,self.color,self.kind,self.value)
    return desc_string

MyCar1 = Car()
MyCar1.name ="Fer"
MyCar1.color="red"
MyCar1.value = 60000
print MyCar1.description()

MyCar2 = Car()
MyCar2.name = "Jump"
MyCar2.color = "blue"
MyCar2.value = 10000
print MyCar2.description()
