from models.model import Model


class CardiffnlpTwitterRobertaBaseSentimentLatest(Model):
    def __init__(self):
        super().__init__(
            model_name="cardiffnlp/twitter-roberta-base-sentiment-latest")
