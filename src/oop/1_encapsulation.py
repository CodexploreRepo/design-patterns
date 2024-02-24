# Encapsulation is basically wrapping methods and data into an unit,
# e.g., a class. There is no strict concept of "private" variables in Python,
# but a convention as follows
class DummyModel:
    def __init__(self):
        self.a = 1  # public variable
        self._b = 2  # protected variable: used within the class and its subclass (via inheritance)
        self.__c = 3  # private variable: used within the class only


if __name__ == "__main__":
    model = DummyModel()
    print("a: ", model.a)
    print("b: ", model._b)
    print("_DummyModel__c: ", model._DummyModel__c)
    print("c: ", model.__c)  # Error! Please change it to _DummyModel__c
