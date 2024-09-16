import nltk
from nltk.stem import WordNetLemmatizer

'''
    Pos tag
    Noun - n
    Verb - v
    Adjective - a
    Adverb - r
'''
lemmatizer = WordNetLemmatizer()
print("the root word for the word GOING for the pos tag =' verb ' "+lemmatizer.lemmatize("going",pos='v'))


words  = ["eating","eats","eaten","writing","writen","programming", "programs","finally","finalized","history"]


for word in words:
    print(word+" -----> "+lemmatizer.lemmatize(word,pos ='v'))