from nose.tools import *
from ex48 import parser

word_list1 = [('verb','go'),('direction','north'),('stop','at')]
word_list2 = [('noun','apple'),('stop','the'),('direction','south')]
word_list3 = [('assss','ddddd')]
def test_peek():
    assert_equal(parser.peek(word_list1),('verb'))
    assert_equal(parser.peek(word_list3),('assss'))

def test_match():
    assert_equal(parser.match(word_list1,'direction'),None)
    assert_equal(parser.match(word_list3,'assss'),('assss','ddddd'))

def test_skip():
    assert_equal(parser.skip(word_list1,'stop'),None)

def test_parse_verb():
#    assert_equal(parser.parse_verb(word_list2),ParserError("Expected a noun or direction next."))
    pass
def test_parse_object():
    pass
def test_parse_subject():
    pass
def parse_sentence():
    assert_equal(parse_sentence(word_list1),x)
