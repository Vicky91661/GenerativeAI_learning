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
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

corpus =[]
for i in range(0,len(spam_data)):
    review = re.sub('[^a-zA-z]',' ',spam_data['message'][i])
    review = review.lower()
    review = review.split()
    review= [ps.stem(word) for word in review if not word in stopwords.words('english') ]
    review = ' '.join(review)
    corpus.append(review)



# create bag of words
import sklearn
from sklearn.feature_extraction.text import CountVectorizer

# For Binary bag of words  enable binary=True
cv = CountVectorizer(max_features=500,binary=True)

x= cv.fit_transform(corpus).toarray()
print("the bag of words is  \n",x)

print("Your top 500 Words is ",cv.vocabulary_)

# N-Gram
# Create the bag of words model with N-gram 
# Bi-gram
cv2 = CountVectorizer(max_features=500,binary=True,ngram_range=(1,2))
x2= cv2.fit_transform(corpus).toarray()
print("the bag of words is for bigram  \n",x2)

# tri-gram
cv3 = CountVectorizer(max_features=500,binary=True,ngram_range=(1,3))
x3= cv3.fit_transform(corpus).toarray()
print("the bag of words is trigram \n",x3)

