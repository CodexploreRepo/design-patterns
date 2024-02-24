class DummyModel:
    def __init__(self, a: float, b: float) -> None:
        self._a = a
        self._b = b

    # bias (which link to self._b) is the only property you want to expose
    @property
    def bias(self):
        return self._b  #

    @bias.setter
    def bias(self, value: float):
        self._b = value

    @bias.deleter
    def bias(self):
        self._b = 0

    def predict(self, x: float) -> float:
        return self._a * x + self._b


if __name__ == "__main__":
    dummy_model = DummyModel(1, 2)
    # Print the prediction for the model
    print("Original model prediction:")
    print(dummy_model.predict(1))
    # @bias.setter Update the bias from 2 to 3 and check the prediction again
    print("Model prediction after updating bias:")
    dummy_model.bias = 3
    print(dummy_model.predict(1))
    # Now, delete the bias and try it again
    print("Model prediction after removing bias:")
    del dummy_model.bias
    print(dummy_model.predict(1))

    dummy_model.__a = 1
    print(dummy_model.bias)
    print(dummy_model._b)
    print(dummy_model.__a)
