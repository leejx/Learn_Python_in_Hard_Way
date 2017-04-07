from sys import argv

script, filename = argv

txt = open(filename)

print "filename is ", txt
print txt.read()

file_again = raw_input("file again")
print open(file_again).read()
