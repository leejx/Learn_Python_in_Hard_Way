# -*- coding: utf-8 -*-
print "say something"
print "觉得"
print "add sum = ", 25+30/6
print 3 + 2 < 5 - 7
print 5 >= -2
cars = 4
print "There are ", cars, "all"
print "cars %d here" % cars
print "cars %r, cars %d" %(cars, cars ** 2)

print "." * 10
##print "cars %d, cars %d" %cars, cars ** 2
print round(1.28222222)
# use %r for getting debugging information
formatter = "%r %r %r"
print formatter % ("one", "two", 'three')
print formatter % (formatter, formatter, formatter)
months = "jan\nfeb"
print "months:", months
print """dfadf
sdfasdf"""
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
