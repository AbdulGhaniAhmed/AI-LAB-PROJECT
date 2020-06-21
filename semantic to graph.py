from py2neo import Graph, Node, Relationship
from nltk import word_tokenize,pos_tag
graph = Graph(password="123")



sentences=['Qasim hates peer',
           'Malaika is daughter of Ali',
           'Hussain loves Cat',
           'Bashir has a Dog',
           'Cat sits in Car'
           ]

for sentence in sentences:
    tokens=word_tokenize(sentence)
    print(tokens)
    tags= pos_tag(tokens)
    print(tags)
    nouns=[]
    verb=''

    for tuple in tags:
        print(tuple)
        if tuple[1]=='NNP':
            nouns.append(tuple[0])
        if tuple[1]=='VBZ' or tuple[1]=='NN':
            verb=tuple[0]
    node1 = Node("Person", name=nouns[0])
    graph.create(node1)
    node2 = Node("Object", name = nouns[1])
    graph.create(node2)
    relationship = Relationship(node1, verb, node2)
    graph.create(relationship)