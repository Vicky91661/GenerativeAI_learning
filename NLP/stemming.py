#  classification Problem 
# Comments of products is a positive review or negative review
# Review ---> [Eating, Eats, Eaten]=> Eat, [going , gone, goes]=> go

words  = ["eating","eats","eaten","writing","writen","programming", "programs","finally","finalized","history"]

# PorterStremmer

import nltk
from nltk.stem import PorterStemmer

stemming  = PorterStemmer()

for word in words:
    print(word+"----->"+stemming.stem(word))


# RegexpStemmer Class

from nltk.stem import RegexpStemmer
reg_stemmer = RegexpStemmer('ing$|s$|e$|able$', min=4 )
print("The stem of the word eating is => "+reg_stemmer.stem('eating'))
print("The stem of the word ingeating is => "+reg_stemmer.stem('ingeating'))




# Snowball Stemmer

from nltk.stem import SnowballStemmer
 
# Choose a language for stemming, for example, English
stemmer = SnowballStemmer(language='english')
 
# Example words to stem
words_to_stem = ['running', 'jumped', 'happily', 'quickly', 'foxes']
 
# Apply Snowball Stemmer
stemmed_words = [stemmer.stem(word) for word in words_to_stem]
 
# Print the results
print("Original words:", words_to_stem)
print("Stemmed words:", stemmed_words)
