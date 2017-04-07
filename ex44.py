class Parent(object):
    """docstring for Parent."""
    def implicit(self):
        print "PARENT implicit()"

    def override(self):
        print "parent override()"

    def altered(self):
        print "parent altered()"

class Other(object):
    """docstring for Other."""
    def implicit(self):
        print "Other implicit()"

    def override(self):
        print "Other override()"

    def altered(self):
        print "Other altered()"

class Child(Parent):
    """docstring for Child."""
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "son override()"


    def altered(self):
        print "child before parent altered()"
        super(Child, self).altered()
        print "child after parent altered()"
        self.other.altered()



dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
