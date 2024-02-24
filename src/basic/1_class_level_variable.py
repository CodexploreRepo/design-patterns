class DummyModel:
    bias = 0  # Class-level variable

    def __init__(self, coef):
        self.coef = coef  # Instance-level variable


# Creating an instance of DummyModel
model = DummyModel(10)
print(model.coef)

# Accessing the class-level variable
print(DummyModel.bias)  # Output: 0

# Modifying the class-level variable
DummyModel.bias = 1
print(DummyModel.bias)  # Output: 1

# Note that changes to the class-level variable affect all instances
print(model.bias)  # Output: 1

model.bias = 2
print(
    DummyModel.bias
)  # Output: 1 (as model.bias = 2 is only for the model instance)
