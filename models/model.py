from transformers import Pipeline, pipeline


class Model:
    def __init__(self, model_name: str, task: str = "text-classification"):
        self.model_name: str = model_name
        self.pipeline: Pipeline = pipeline(task=task, model=model_name)

    def evaluate(self, texts: list[str], top_k: int = 1):
        """
        Evaluate the sentiment of a list of texts.

        Args:
            texts (list): A list of text strings.

        Returns:
            list: A list of dictionaries containing the sentiment prediction for each text.
        """
        return self.pipeline(texts, top_k=top_k)
