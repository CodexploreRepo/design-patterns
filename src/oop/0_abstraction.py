"""
An example shows how to use abstract 
"""

from abc import ABC, abstractmethod


class BaseLRModel(ABC):
    """
    This class encapsulates data, i.e, bias and methods predict()
    Abstract class: interface
    """

    def __init__(self, bias: float) -> None:
        self._bias = bias

    @abstractmethod
    def predict(self, x: float):
        pass


# OneDimensionalLRModel inherits from BaseLRModel: y= ax + bias
class OneDimensionalLRModel(BaseLRModel):
    def __init__(self, a: float, bias: float) -> None:
        # The below line is equal to `self._bias = bias`
        # but we can simple call super from the base class
        super().__init__(bias)
        self._a = a

    def predict(self, x: float):
        return self._a * x + self._bias


# TwoDimensionalLRModel inherits from BaseLRModel
class TwoDimensionalLRModel(BaseLRModel):
    def __init__(self, a: float, b: float, bias: float) -> None:
        super().__init__(bias)
        self._a = a
        self._b = b

    # Polymorphism is here, which indicates that multiple models can inherit
    # from the base model, each has its own predict method
    def predict(self, x1: float, x2: float):
        return self._a * x1 + self._b * x2 + self._bias


if __name__ == "__main__":
    odmodel = OneDimensionalLRModel(1, 2)
    print(odmodel._a)
    print(odmodel.predict(1))
