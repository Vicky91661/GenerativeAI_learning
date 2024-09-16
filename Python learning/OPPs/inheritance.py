# Inherit property and method form the parent class is know as inheritance
# multi level inheriatance
# multiple inheritance


# multi level inheritance
class grandParent :
    def test_grandParent(self):
        return "this is the grand parent class"
    
class parent(grandParent):
    def test_parent(self):
        return "this is the parent class"
class child(parent):
    def test_child(self):
        return "this is the child class"
child_class_object = child()
print(child_class_object.test_child())
print(child_class_object.test_parent())
print(child_class_object.test_grandParent())

# multiple inheritance
class grandParent2 :
    def test_grandParent(self):
        return "this is the grand parent class"
    
class parent2:
    def test_parent(self):
        return "this is the parent class"
class child2(grandParent2,parent2):
    def test_child(self):
        return "this is the child class"
child_class_object2 = child2()
print(child_class_object2.test_child())
print(child_class_object2.test_parent())
print(child_class_object2.test_grandParent())