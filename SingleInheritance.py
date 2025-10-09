class Parent:
    def show(self):
        print("In Parent")
class Child(Parent):
    def child_show(self):
        print("In Child")
child = Child()
child.show()
child.child_show()