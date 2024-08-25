from nltk.sentiment.vader import SentimentIntensityAnalyzer

class sentiment:
    def __init__(self):
        pass
    
    def main(self, text):
        sid = SentimentIntensityAnalyzer()
        sentiment_scores = sid.polarity_scores(text)
        sentiment_scores['text'] = text
        result = sentiment().__classify(sentiment_scores)
        return result
    
    def __classify(self, sentiment_scores):
        if sentiment_scores['pos'] >= 0.5:
            sentiment_scores['category'] = 'Positive'
        elif sentiment_scores['neg'] >= 0.5:
            sentiment_scores['category'] = 'Negative'
        else:
            sentiment_scores['category'] = 'Neutral'
        return sentiment_scores