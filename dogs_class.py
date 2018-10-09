#Las clases van con mayusculas
class Dog:
    def __init__(self,name,breed,color,size,weight):
        self.name = name
        self.breed = breed
        self.color = color
        self.size = size
        self.weight = weight
        print(f"Hello, I`m {name} and I'm alive, my breed is {breed}, my color is {color}, size {size} and my weight {weight}")
        

    def bark(self,sound = "Whoof!"):
       print(f"{self.name} Says: {sound}")

    def eat(self, type_of_food = 'meat'):
      print(f"{self.name} is eating {type_of_food}, and its weight is {self.weight}")

    def weight(self):
        return f"Im {self.name} and my weight is {self.weight}"
 