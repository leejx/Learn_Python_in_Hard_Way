from sys import argv
script, input_file = argv

def print_all(f):
    print f.read()
#locate to the f byte of the file
def rewind(f):
    print f.seek(2)

def print_a_line(line_count,f):
    print line_count, f.readline()

current_file = open(input_file)
print_all(current_file)
print "rewind:"
#rewind(current_file)
print_a_line(1,current_file)
print_a_line(3,current_file)
