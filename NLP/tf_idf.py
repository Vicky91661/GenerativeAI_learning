import nltk 
import re 
import numpy as np 
  
# execute the text here as : 
import pandas as pd
spam_data = pd.read_csv('./spam.csv', delimiter=',',encoding='latin1' )
spam_data = spam_data.drop(columns = ["Unnamed: 2","Unnamed: 3","Unnamed: 4"], axis=1)
print("Spam data is => \n",spam_data.head())

# dropping duplicate data
# spam_data.drop_duplicates(inplace=True)

# Data Cleaning and Prep processing
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
wordlemmatize = WordNetLemmatizer()

corpus =[]
for i in range(0,len(spam_data)):
    review = re.sub('[^a-zA-z]',' ',spam_data['message'][i])
    review = review.lower()
    review = review.split()
    review= [wordlemmatize.lemmatize(word) for word in review if not word in stopwords.words('english') ]
    review = ' '.join(review)
    corpus.append(review)



# create TF-IDF
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
# For Binary bag of words  enable binary=True
tfidf = TfidfVectorizer(max_features=500)

x= tfidf.fit_transform(corpus).toarray()

import numpy as np
np.set_printoptions(edgeitems=30,linewidth=100000,formatter=dict(float=lambda x:"%.3g" % x))
print(x)


# N-Gram
# Create the bag of words model with N-gram 
# Bi-gram
tfidf2 = TfidfVectorizer(max_features=500,binary=True,ngram_range=(2,2))
x2= tfidf2.fit_transform(corpus).toarray()

print("The vocabolary for Bi-gram is  ",tfidf2.vocabulary_)

np.set_printoptions(edgeitems=30,linewidth=100000,formatter=dict(float=lambda x:"%.3g" % x))
print(x2)

# # tri-gram
# cv3 = CountVectorizer(max_features=500,binary=True,ngram_range=(1,3))
# x3= cv3.fit_transform(corpus).toarray()
# print("the bag of words is trigram \n",x3)

