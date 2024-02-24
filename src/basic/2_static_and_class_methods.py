from typing import List


class DummyModel:
    bias = 0

    def __init__(self, coef: float) -> None:
        self._coef = coef

    # Static method does not depend on the instance,
    # i.e: independent with instance's attributes, methods via self.
    # it is mainly used for methods that semantically
    # relates to this class.
    @staticmethod
    def calculate_accuracy(a: List[int], b: List[int]):
        if len(a) != len(b):
            raise ValueError("Can not calculate accuracy!")
        else:
            num_correct_items = 0
            for i in range(len(a)):
                if a[i] == b[i]:
                    num_correct_items = num_correct_items + 1
            return num_correct_items / len(a)

    # Class method
    @classmethod
    def increase_bias(cls):
        cls.bias += 1

    def display(self):
        print(f"Coef: {self._coef}")
        print(f"Bias: {DummyModel.bias}")


if __name__ == "__main__":
    # Make a model with coef is 10
    model = DummyModel(10)
    # Increase the bias
    DummyModel.increase_bias()
    # Display the model info
    model.display()  # 1
