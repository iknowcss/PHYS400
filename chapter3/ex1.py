# The following code yields the following exception:
#
#    Traceback (most recent call last):
#      File "ex1.py", line 1, in <module>
#        repeat_lyrics()
#    NameError: name 'repeat_lyrics' is not defined
#
# This exception is thrown because the function is called before it is defined

repeat_lyrics()

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
