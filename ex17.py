from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" %(from_file, to_file)
indata = open(from_file).read()
print "the input file is %d bytes long" % len(indata)
print "exist? %s " % exists(to_file)
out_file = open(to_file,'w')
out_file.write(indata)
out_file.write("ljx")
out_file.close()
