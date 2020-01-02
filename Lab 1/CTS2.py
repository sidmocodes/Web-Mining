from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import pyPDF2
tokens = []
stems = dict()
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()
for i in range(1,11):
 f = open("doc"+str(i)+".pdf", "rb”)
 data = f.read()
 doc_tokens = word_tokenize(data)
 doc_tokens = [doc_tokens.lower() for doc_tokens in doc_tokens if
doc_tokens.isalpha()]
 for token in doc_tokens:
 if token not in tokens:
 if token not in stop_words:
 tokens.append(token)
 doc_stem = ps.stem(token)
 if token not in stop_words:
 if doc_stem not in stems:
 stems[doc_stem] = [1,set([i])]
 else:
 stems[doc_stem][0] = stems[doc_stem][0]+1
 stems[doc_stem][1].add(i) 
