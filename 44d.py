class Parent(object):
    def implicit(self):
        print("PARENT implictit()")
    def override(self):
        print("PARENT override()")
    def altered(self):
        print("PARENT altered()")
class Child(Parent):
    
    def override(self):
        print("Child override()")
    def altered(self):
        print("BEFORE PARENT altered()")
        super(Child,self).altered()
        print("AFTER PARENT altered()")
    
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered() 