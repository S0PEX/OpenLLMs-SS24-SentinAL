# Sentiment Analysis Generalization and Encoding Impact Experiment

Sentiment analysis is a crucial aspect of understanding public opinion, detecting trends, and monitoring social media content. While many models are trained specifically on data from platforms like Twitter, it's essential to evaluate their performance in other contexts. This experiment focuses on assessing the generalization capability of sentiment analysis models in non-Twitter domains. Additionally, we aim to understand how specific wordings, tenses, and character encodings influence sentiment classification. Identifying instances of false positives and false negatives due to non-standard characters is a critical part of this evaluation.

### Getting Started

To get started with SentinAL, please refer to the [Getting Started guide](getting-started.md) for instructions on setting up the project environment, cloning the repository, and installing the required packages.

---

### 1. Task

The primary goal of this task is to evaluate the generalization capability of two sentiment analysis models when applied to non-Twitter domains. Specifically, we aim to understand how different wordings, tenses, and character encodings influence sentiment classification. We will compare the performance of the [Twitter-roBERTa-base-sentiment-latest](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) model, trained on Twitter data, and the [distilroberta-finetuned-financial-news-sentiment-analysis](https://huggingface.co/mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis) model, trained on financial news data.

The task will include:

1. Comparing the models based on their target domains and cross-domain performance.
2. Analyzing how a potential attacker could bypass sentiment detection by using identically looking but differently encoded letters to alter sentiment classification.
3. (If time permits) Additional tests on how tense and persona affect sentiment classification.

**Examples:**

- **Standard English vs. Non-standard characters:**
  - Standard English: "I love this!"
  - Non-standard character: "I lоve this!" (using a Cyrillic 'о' instead of a Latin 'o')
- **Tense:**

  - Present tense: "I love this product."
  - Past tense: "I loved this product."
  - Future tense: "I will love this product."

- **Persona:**
  - First person: "I think this is great."
  - Third person: "He thinks this is great."
  - Group speaking: "We believe this is great."

### 2. Data Basis

- **Medium:** Text
- **Language:** English
- **Source:** Various sources including news articles, product reviews, blog posts, and social media platforms other than Twitter (e.g., Facebook, Instagram, Reddit).
- **Datasets:** [tweet_eval](https://huggingface.co/datasets/tweet_eval), [financial_phrasebank](https://huggingface.co/datasets/takala/financial_phrasebank).

### 3. OpenLLM to Use

We will use two models for this experiment:

1. [Twitter-roBERTa-base-sentiment-latest](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) - Trained on ~124M tweets from January 2018 to December 2021 and finetuned for sentiment analysis with the TweetEval benchmark.
2. [distilroberta-finetuned-financial-news-sentiment-analysis](https://huggingface.co/mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis) - Trained on financial news data for sentiment analysis.

### 4. Experiment Design

**Procedure:**

1. **Data Collection:**

   - Gather text samples from various non-Twitter sources such as news articles, product reviews, blog posts, and other social media platforms, or use existing sentiment datasets, e.g., [tweet_eval](https://huggingface.co/datasets/tweet_eval), [financial_phrasebank](https://huggingface.co/datasets/takala/financial_phrasebank).
   - Ensure a diverse mix of sentiments (positive, negative, neutral) in the collected data.

2. **Data Preparation:**

   - Organize the collected data into a structured format suitable for analysis.
   - Annotate the data with expected sentiment labels (positive, negative, neutral), if the data was scraped by ourselves.
   - Preprocess the datasets to transform the raw sentences into ones that look the same but differ in encoding. For example, replace characters with identically looking ones but with different encodings.

3. **Model Evaluation:**

   - Use both models to predict sentiments for the collected raw text samples.
   - Then repeat the same for the transformed data.
   - Record the predicted sentiments along with the confidence scores provided by each model.

4. **Analysis of Specific Wordings and Tenses (Optinally):**

   - Investigate how different tenses (past, present, future) and specific wordings affect sentiment classification.
   - Analyze the impact of non-standard characters and different encodings on the sentiment predictions.

5. **Error Analysis:**

   - Identify instances of false positive and false negative sentiment classifications.
   - Examine the specific cases where non-standard characters or different encodings caused misclassification.

6. **Evaluation:**

   - Compare the models' predictions against the annotated labels to calculate metrics such as accuracy, precision, recall, and F1 score.
   - Summarize the findings to understand the generalization capability of the models and the impact of non-standard characters on sentiment classification.

<!---
**Testing with Common LLMs (Optinally):**

To contextualize the results, we will also evaluate how other common sentiment analysis models (e.g., GPT-3, etc.) perform on the same task. This will help in understanding whether the issues observed are specific to the selected models or are common across different models. Since the two main targeted models are both BERT-based, it is important to determine if the issues are related to the architecture itself.

-->

**Conclusion:**

This experiment aims to provide insights into the robustness and limitations of the [Twitter-roBERTa-base-sentiment-latest](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) and [distilroberta-finetuned-financial-news-sentiment-analysis](https://huggingface.co/mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis) models when applied to other domains. By identifying specific challenges posed by different wordings, tenses, and character encodings, we can better understand how to improve sentiment analysis models for broader applications.

---

**References:**

- [TweetEval benchmark](https://github.com/cardiffnlp/tweeteval)
- [Twitter-roBERTa-base-sentiment-latest](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest)
- [distilroberta-finetuned-financial-news-sentiment-analysis](https://huggingface.co/mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis)
