class ParserError (Exception) :
    pass

class Sentence (object) :

    def __init__(self, subject, verb, obj):
        #remember we take ('noun', 'princess') ruples
        #and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]
# peek the list of the words
# and return the type of the word
def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None
# confirm the expected word is the right type
# takes the expected word off the list
# return the expected word pair
def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None
# skip the stop words
def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)
    print word_list
# return the verb
def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")
# return the object
def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")
# subject
def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")
# combine final Sentence
def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)
