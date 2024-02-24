class DummyModel:
    # __init__, __repr__, __str__ are called magic methods
    # https://rszalski.github.io/magicmethods/
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    # String presentation of the object, but for developers,
    # we can use it to recreate the object
    # For example:
    #   mymodel = DummyModel(1, 2)
    #   mymodel or repr(mymodel)
    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f"{class_name}({self.a}, {self.b})"

    # Still string presentation of the object, but for end users
    # For example:
    #   mymodel = DummyModel(1, 2)
    #   print(mymodel) or str(mymodel)
    def __str__(self) -> str:
        return (
            "A dummy linear regression model in the form of y=ax+b "
            f"with a is {self.a} and b is {self.b}"
        )

    def predict(self, x: float) -> float:
        return self.a * x + self.b


if __name__ == "__main__":
    dummy_model = DummyModel(1, 2)
    # # Human readable format for the model
    print(dummy_model)
    # Developer format for the model
    print(repr(dummy_model))  # dummy_model.__repr__()
    # Print the prediction for the model
    print(dummy_model.predict(1))
