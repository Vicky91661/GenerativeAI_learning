
sentance = """The Eiffel Tower was built from 1887 to 1889 by French engineer Gustave Eiffel, whose company specialization
in building metal frameworks and structure"""

import nltk
nltk.download('words')
words =nltk.word_tokenize(sentance)
tag_words = nltk.pos_tag(words)
print(tag_words)
print(nltk.ne_chunk(tag_words).draw())