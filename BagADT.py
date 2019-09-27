# The Bag is an example of an Abstract Data Type
# Data abstraction means separating various data values and 
# operations that are performed with them from the exterior


class Bag:

    def __init__(self):
        self.contents = []

    def length(self):
        return len(self.contents)

    def contains(self, item):
        return item in self.contents

    def add(self, item):
        self.contents.append(item)

    def remove(self, item):
        self.contents.remove(item)

    def iterator(self):
        return iter(self.contents)


myPurse = Bag()
myPurse.add("1 dollar bill")
myPurse.add("lipstick")
myPurse.remove("lipstick")
myPurse.add("cloth")
myPurse.add("coins")


for i in myPurse.iterator():
    print(i)