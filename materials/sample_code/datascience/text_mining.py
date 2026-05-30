import nltk

nltk.download('punkt')

text = """Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't eat cardboard"""

from nltk.tokenize import sent_tokenize

tokenized_text = sent_tokenize(text)
print(tokenized_text)

from nltk.tokenize import word_tokenize

tokenized_word = word_tokenize(text)
print(tokenized_word)

from nltk.probability import FreqDist

fdist = FreqDist(tokenized_word)
print(fdist)
print(fdist.most_common(2))

import matplotlib.pyplot as plt

fdist.plot(30, cumulative=False)
plt.show()

from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
print(stop_words)
print(type(stop_words))

filtered_sent = []
for w in tokenized_word:
    if w not in stop_words:
        filtered_sent.append(w)
print("Tokenized Sentence:", tokenized_word)
print("Filtered Sentence:", filtered_sent)

##### 5. Lexicon Normalization
##### 5.1 Stemming
from nltk.stem import PorterStemmer

ps = PorterStemmer()
stemmed_words = []
for w in filtered_sent:
    stemmed_words.append(ps.stem(w))
print("Filtered Sentence:", filtered_sent)
print("Stemmed Sentence:", stemmed_words)

##### 5.2 Lemmatization
# from terminal
#  >>> import nltk
#  >>> nltk.download('wordnet')
from nltk.stem.wordnet import WordNetLemmatizer

lem = WordNetLemmatizer()
from nltk.stem.porter import PorterStemmer

stem = PorterStemmer()
word = "flying"
print("Lemmatized Word:", lem.lemmatize(word, "v"))
print("Stemmed Word:", stem.stem(word))

##### 5.3 POS Tagging
# >>> import nltk
# >>> nltk.download('averaged_perceptron_tagger')
sent = "Albert Einstein was born in Ulm, Germany in 1879."
tokens = nltk.word_tokenize(sent)
print(tokens)
print(nltk.pos_tag(tokens))

##### 6. Sentiment Analysis
##### 6.1 Text Classification
import pandas as pd
data = pd.read_csv('train.tsv', sep='\t')
print(data.head())
print(data.info())
print(data.Sentiment.value_counts())
Sentiment_count = data.groupby('Sentiment').count()
plt.bar(Sentiment_count.index.values, Sentiment_count['Phrase'])
plt.xlabel('Review Sentiments')
plt.ylabel('Number of Review')
plt.show()


