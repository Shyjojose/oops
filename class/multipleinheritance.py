class flyable:
    def __init__(self, name):
        self.name = name
    def fly(self):
        return f"{self.name} is flying"
class swimmable:
    def __init__(self, name):
        self.name = name
    def swim(self):
        return f"{self.name} is swimming"
class runnable:
    def __init__(self, name):
        self.name = name
    def run(self):
        return f"{self.name} is running"
class duck(flyable, swimmable, runnable):
    def __init__(self, name):
        super().__init__(name)
    def quack(self):
        return f"{self.name} says Quack!"
d = duck("Donald")
print(d.fly()) # Output: Donald is flying
print(d.swim()) # Output: Donald is swimming
print(d.run()) # Output: Donald is running
print(d.quack()) # Output: Donald says Quack!
print(duck.mro()) # Output: [<class '__main__.duck'>, <class '__main__.flyable'>, <class '__main__.swimmable'>, <class '__main__.runnable'>, <class 'object'>]
#the multiple inheritance goes from left to right, so the flyable class is called first, then swimmable and runnable. The mro() method shows the method resolution order for the duck class, which is the order in which Python looks for methods when they are called on an instance of the duck class.
#also from top to bottom, so the flyable class is called first, then swimmable and runnable. The mro() method shows the method resolution order for the duck class, which is the order in which Python looks for methods when they are called on an instance of the duck class.