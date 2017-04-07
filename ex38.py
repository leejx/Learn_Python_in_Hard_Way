ten_things = "Apples Oranges Crows Telephone Light Sugar"
stuff = ten_things.split(' ')
more_stuff = ["Day","Night", "Song", "Frisbee", "Corn", "Banana"]
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now" % len(stuff)

print "There we go: ", stuff
print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print ' # '.join(stuff[3:5])
print """adfad
asdfadf"""
print """123123
     12312312"""
a=3
b=2
c=1
code = "%d%d%d" % (a,b,c)
print code
