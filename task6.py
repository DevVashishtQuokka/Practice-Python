class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print("General Sound")
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        print("bhao bhaoooo")
    @classmethod
    def animal_type(cls):
        return "dog"
    @staticmethod
    def info():
        return "Dogs are friendly in nature and they can be pet."
    def sound(self):
        return "Bark"
    def doginfo(self, *args):
        info = [f"Dog Name: {self.name}", f"Breed: {self.breed}"]
        if args:
            info.append(f"Nature: {', '.join(args)}")
        return ", ".join(info)
 
dog = Dog("Scissor", "Rotwiller")
dog.speak()
dogsound = dog.sound()
print(dogsound)
print(Dog.animal_type())
print(Dog.info())
print(dog.doginfo("dangerous breed", "Gaurd dogs"))
