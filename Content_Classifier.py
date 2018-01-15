import re #regularexpressions
import numpy as np
import pandas as pd
from nltk import SnowballStemmer #stemming the tweets
import string

#tokenize the tweet
def tokenize(data):
        stemmer = SnowballStemmer("english")
        stop_words = text.ENGLISH_STOP_WORDS
        temp = data
        regex = re.compile('[%s]' % re.escape(string.punctuation))
        temp = regex.sub(' ', temp)
        temp = "".join(b for b in temp if ord(b) < 128)
        temp = temp.lower()
        words = temp.split()
        no_stop_words = [w for w in words if not w in stop_words]
        stemmed = [stemmer.stem(item) for item in no_stop_words]
        return stemmed

data_uk =pd.read_csv('NLP/nlp_uk.csv')
uk_tweets=pd.DataFrame(data_uk,columns=['Nickname','Tweet content','Tweet language (ISO 639-1)'])

data_us =pd.read_csv('NLP/nlp_us.csv')
us_tweets=pd.DataFrame(data_us,columns=['Nickname','Tweet content','Tweet language (ISO 639-1)'])

print us_tweets
print uk_tweets
