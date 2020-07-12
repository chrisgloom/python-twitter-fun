from time import sleep
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters

punkt_param = PunktParameters()
punkt_param.abbrev_types = {'dr', 'vs', 'mr', 'mrs', 'prof', 'inc'}
sentence_splitter = PunktSentenceTokenizer(punkt_param)

with open('peterPan.txt') as file:
    file_content = file.read()
    file_content = file_content.replace("\n", " ")
    sentences = sentence_splitter.tokenize(file_content)

for sentence in sentences:
    print(sentence)
    sleep(3)
