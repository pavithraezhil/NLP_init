from nltk.corpus import wordnet as wn
panda = wn.synset('panda.n.01')
hyper = lambda s: s.hypernyms()
wordL=list(panda.closure(hyper))
print(wordL)
