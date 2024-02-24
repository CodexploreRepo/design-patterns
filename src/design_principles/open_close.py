import pandas as pd


class DataPipeline:
    def drop_missing_data(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.dropna()

    def standardize_data(self, data: pd.DataFrame) -> pd.DataFrame:
        return (data - data.mean()) / data.std()

    # Adding this
    def encode_data(self, data: pd.DataFrame) -> pd.DataFrame:
        return pd.get_dummies(data)

    def process(self, data: pd.DataFrame) -> pd.DataFrame:
        return (
            data.pipe(self.drop_missing_data)
            .pipe(self.encode_data)
            .pipe(self.standardize_data)
        )


# Refactor the DataPipeline class to accept pluggable strategies.

from abc import ABC, abstractclassmethod


class DataProcessingStrategy(ABC):
    @abstractclassmethod
    def apply(self, data: pd.DataFrame) -> pd.DataFrame:
        pass


class DropMissingDataStrategy(DataProcessingStrategy):
    def apply(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.dropna()


class StandardizeDataStrategy(DataProcessingStrategy):
    def apply(self, data: pd.DataFrame) -> pd.DataFrame:
        return (data - data.mean()) / data.std()


class EncodeDataStrategy(DataProcessingStrategy):
    def apply(self, data: pd.DataFrame) -> pd.DataFrame:
        return pd.get_dummies(data)


class RefactoredDataPipeline:
    def __init__(self):
        self.strategies = []

    def add_strategy(self, strategy: DataProcessingStrategy):
        self.strategies.append(strategy)

    def process(self, data: pd.DataFrame) -> pd.DataFrame:
        for strategy in self.strategies:
            data = strategy.apply(data)
        return data


if __name__ == "__main__":
    pipeline = DataPipeline()
    data = pd.DataFrame(
        {
            "A": [1, 2, 3, None, 5],
            "B": [5, 3, 2, 1, 3],
            "C": ["a", "a", "b", "b", "a"],
        }
    )
    processed_data = pipeline.process(data)
    print(processed_data)

    r_pipeline = RefactoredDataPipeline()
    r_pipeline.add_strategy(DropMissingDataStrategy())
    r_pipeline.add_strategy(EncodeDataStrategy())
    r_pipeline.add_strategy(StandardizeDataStrategy())
    print(r_pipeline.process(data))
