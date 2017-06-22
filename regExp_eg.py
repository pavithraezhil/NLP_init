import re
re1 = re.compile('python')
print(bool(re1.match('Python')))

import nltk

from nltk.corpus import brown

brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
unigram_tagger.tag(brown_sents[2007])

bigram_tagger = nltk.BigramTagger(brown_tagged_sents)
bigram_tagger.tag(brown_sents[2007])

raw = "OMG, Natural Language Processing is SO cool and I'm really enjoying this workshop!"
tokens = nltk.word_tokenize(raw)
tokens = [i.lower() for i in tokens]

lancaster = nltk.LancasterStemmer()
stems = [lancaster.stem(i) for i in tokens]

lancaster = nltk.PorterStemmer()
stems = [lancaster.stem(i) for i in tokens]

from nltk import WordNetLemmatizer

lemma = nltk.WordNetLemmatizer()
text = "Women in technology are amazing at coding"
ex = [i.lower() for i in text.split()]

lemmas = [lemma.lemmatize(i) for i in ex]
