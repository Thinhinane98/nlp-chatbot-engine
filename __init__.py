import nltk
import csv

sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

def log_chat(text, pos_tags, return_dict):
    with open('log.csv','a') as file:
        writer = csv.writer(file)
        writer.writerows([[text, str(pos_tags), str(return_dict)]])

def get_entity_action(sentence):
    tokens = nltk.word_tokenize(sentence)
    word_pos = nltk.pos_tag(tokens)
    print ("\n\nPOS Tags ....")
    print (word_pos)

    nouns = [word for word,pos in word_pos if pos in ['NN','NNP','NNS','NNPS']]
    verbs = [word for word,pos in word_pos if pos in ['VB','VBD','VBG','VBN','VBP','VBZ']]
    question = [word for word,pos in word_pos if pos in ["WDT","WP","WP$","WRB"]]

    return_dict =  {"nouns":nouns, "verbs":verbs, "question_words": question}
    log_chat(sentence, word_pos, return_dict)
    return return_dict


text = input("Enter Text :: ")
while text != "end":
    sentences = sent_tokenizer.tokenize(text)
    sentences = [sent.capitalize() for sent in sentences]
    for sentence in sentences:
        result = get_entity_action(sentence)
        print ("\n\n")
        print (result)
    text = input("\nEnter Text ::")
