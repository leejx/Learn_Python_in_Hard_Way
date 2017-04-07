def break_words(stuff):
    """This break words for us"""
    words = stuff.split(' ')
    return words
def sort_words(words):
    """sort words"""
    return sorted(words)
def print_first_word(words):
    """print first"""
    word = words.pop(0)
    print words
#dfasdfasdafd
def print_last_word(words):
    """print last"""
    word = words.pop(-1)
    print word
    
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_sentence(sentence):
    """take a full sentence and return the sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """print the first and last words of sentence"""
    word = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
