# The following code runs without error. Functions may be defined in any order.
# In our case, repeat_lyrics() calls print_lyrics(), but print_lyrics() is 
# defined after repeat_lyrics(). Only when repeat_lyrics is evaluated for the
# first time is it bound

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."
    
repeat_lyrics()
