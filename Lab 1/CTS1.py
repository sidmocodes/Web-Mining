from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
tokens = []
stems = dict()
ps = PorterStemmer()
for i in range(1,2):
 f = open("hindi.txt", "r", encoding="UTF-8")
 data = f.read()
 doc_tokens = word_tokenize(data)
 for token in doc_tokens:
 if token not in tokens:
 tokens.append(token)
 doc_stem = ps.stem(token)
 if doc_stem not in stems:
 stems[doc_stem] = [1,set([i])]
 else:
 stems[doc_stem][0] = stems[doc_stem][0]+1
 stems[doc_stem][1].add(i) 
