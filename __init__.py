import nltk
sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

def get_entity_action(sentence):
    tokens = nltk.word_tokenize(sentence)
    word_pos = nltk.pos_tag(tokens)
    print ("\n\nPOS Tags ....")
    print (word_pos)
    nouns = [word for word,pos in word_pos if pos in ['NN','NNP','NNS','NNPS']]
    verbs = [word for word,pos in word_pos if pos in ['VB','VBD','VBG','VBN','VBP','VBZ']]
    question = [word for word,pos in word_pos if pos in ["WDT","WP","WP$","WRB"]]
    return {"nouns":nouns, "verbs":verbs, "question_words": question}


text = input("Enter Text :: ")
while text != "end":
    sentences = sent_tokenizer.tokenize(text)
    sentences = [sent.capitalize() for sent in sentences]
    for sentence in sentences:
        result = get_entity_action(sentence)
        print ("\n\n")
        print (result)
    text = input("\nEnter Text ::")
