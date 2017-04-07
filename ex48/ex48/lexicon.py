Directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right',
            'back']
Verbs = ['go', 'stop', 'kill', 'eat']
Stops = ['the', 'in', 'of', 'from', 'at', 'it']
Nouns = ['door', 'bear', 'princess', 'cabinet']
#input a direction,then print a pair('direction', 'input_direction')
def scan(dir):
    words = dir.split()
    result = []
    for word in words:
        if word in Directions:
            result.append(('direction', word))
        elif word in Verbs:
            result.append(('verb', word))
        elif word in Stops:
            result.append(('stop', word))
        elif word in Nouns:
            result.append(('noun', word))
        elif word.isdigit():
            result.append(('number', int(word)))
        else:
            result.append(('error', word))
    return result
