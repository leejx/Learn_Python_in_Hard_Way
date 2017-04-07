def print_two(args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)


def cheese_and_crackers(cheese_count, bosex_of_crackers):
    print "cheese %d boxes %d" %(cheese_count, bosex_of_crackers)

cheese_and_crackers(20,40)

amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese,amount_of_crackers)
cheese_and_crackers(10+20,20*2)
cheese_and_crackers(amount_of_cheese+10,amount_of_crackers+10)
