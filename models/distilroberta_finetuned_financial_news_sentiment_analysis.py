from models.model import Model


class DistilrobertaFinetunedFinancialNewsSentimentAnalysis(Model):
    def __init__(self):
        super().__init__(
            model_name="mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")


