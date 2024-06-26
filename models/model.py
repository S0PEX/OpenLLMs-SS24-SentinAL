import torch
from datasets import Dataset
from transformers import Pipeline, pipeline


class Model:
    def __init__(self, model_name: str, task: str = "text-classification"):
        self.model_name: str = model_name
        self.pipeline: Pipeline = pipeline(task=task, model=model_name, max_length=512, truncation=True)

    def evaluate(self, texts: list[str], top_k: int = 1):
        """
        Evaluate the sentiment of a list of texts.

        Args:
            texts (list): A list of text strings.
            top_k (int): The number of sentiment predictions to return.

        Returns:
            list: A list of dictionaries containing the sentiment prediction for each text.
        """
        return self.pipeline(texts, top_k=top_k)

    def evaluate_dataset(self, dataset: Dataset, feature: str, top_k: int = 1):
        """
        Evaluate the sentiment of a dataset.

        Args:
            dataset (datasets.Dataset): A dataset containing text data.
            feature (str): The name of the column containing the text data.
            top_k (int): The number of sentiment predictions to return.

        Returns:
            list: A list of dictionaries containing the sentiment prediction for each text.
        """
        data = dataset[feature]
        return self.evaluate(data, top_k=top_k)
