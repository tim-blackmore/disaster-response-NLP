import nltk
import re
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.base import BaseEstimator, TransformerMixin
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download(['punkt', 'wordnet', 'averaged_perceptron_tagger', 'vader_lexicon'])


def tokenize(text):
    """
    tokenize text data. Replace urls, make lower case, strip whitespace, and lemmatize
    :param text:
    :return: the cleaned lemmatized version of the text.
    """
    url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    detected_urls = re.findall(url_regex, text)
    for url in detected_urls:
        text = text.replace(url, "urlplaceholder")

    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens


class StartingVerbExtractor(BaseEstimator, TransformerMixin):
    """ Calculate if first word in sentence is verb

       Attributes:
           starting_verb     The function to calculate if starting word is verb
           fit               N/A
           transform         The method that transforms or runs the calculation
    """

    def starting_verb(self, text):
        sentence_list = nltk.sent_tokenize(text)
        for sentence in sentence_list:
            pos_tags = nltk.pos_tag(tokenize(sentence))
            first_word, first_tag = pos_tags[0]
            if first_tag in ['VB', 'VBP'] or first_word == 'RT':
                return True
        return False

    def fit(self, x, y=None):
        return self

    def transform(self, X):
        X_tagged = pd.Series(X).apply(self.starting_verb)
        return pd.DataFrame(X_tagged)


class TextLengthExtractor(BaseEstimator, TransformerMixin):
    """ Calculates the length of the text

        Attributes:
            fit               N/A
            transform         The method that transforms or runs the calculation
    """

    def fit(self, x, y=None):
        return self

    def transform(self, X):
        X_tagged = pd.Series(X).apply(lambda x: sum(len(word) for word in str(x).split(" ")))
        return pd.DataFrame(X_tagged)


class WordCountExtractor(BaseEstimator, TransformerMixin):
    """ Calculates the number of words in the text

        Attributes:
            fit               N/A
            transform         The method that transforms or runs the calculation
    """
    def fit(self, x, y=None):
        return self

    def transform(self, X):
        X_tagged = pd.Series(X).apply(lambda x: len(str(x).split(" ")))
        return pd.DataFrame(X_tagged)


class SentimentExtractor(BaseEstimator, TransformerMixin):
    """ Calculate the compound sentiment of the statement

       Attributes:
           calculate_sentiment     The function to calculate the compound sentiment
           fit                     N/A
           transform               The method that transforms or runs the calculation
    """
    def calculate_sentiment(self, text):
        sia = SentimentIntensityAnalyzer()
        return sia.polarity_scores(text)["compound"]

    def fit(self, x, y=None):
        return self

    def transform(self, X):
        X_tagged = pd.Series(X).apply(self.calculate_sentiment)
        return pd.DataFrame(X_tagged)
