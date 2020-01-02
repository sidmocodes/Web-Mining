import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
df=pd.read_csv('train.tsv',sep="\t")
df.head()
token = RegexpTokenizer(r'[a-zA-Z0-9]+')
cv =
CountVectorizer(lowercase=True,stop_words='english',ngram_range =
(1,1),tokenizer = token.tokenize)
text_counts= cv.fit_transform(df['Phrase']) 
X_train, X_test, y_train, y_test = train_test_split(text_counts,
df['Sentiment'], test_size=0.3, random_state=1)
clf = MultinomialNB().fit(X_train, y_train)
predicted= clf.predict(X_test)
print("Predicting the 101th
data",X_test[100],":",clf.predict(X_test[100]))
print("MultinomialNB Accuracy:",metrics.accuracy_score(y_test,
predicted)) 
