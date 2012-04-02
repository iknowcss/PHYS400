# 1) Type this example into a script and test it.
def do_twice(f):
    f()
    f()
    
def print_spam():
    print 'spam'

do_twice(print_spam) # It works!
print

# 2) Modify do_twice so that it takes two arguments, a function object and a
#    value, and calls the function twice, passing the value as an argument.
def do_twice(f,v):
    f(v)
    f(v)
    
# 3) Write a more general version of print_spam, called print_twice, that takes
#    a string as a parameter and prints it twice.
def print_twice(s):
	print s
	print s
    
# 4) Use the modified version of do_twice to call print_twice twice, passing 
#    'spam' as an argument.
do_twice(print_twice,'spam') # Prints "spam" 4 times
print
    
# 5) Define a new function called do_four that takes a function object and a 
#    value and calls the function four times, passing the value as a 
#    parameter. There should be only two statements in the body of this 
#    function, not four.
def do_four(f,v):
	do_twice(f,v)
	do_twice(f,v)
	
do_four(print_twice,'spam') # Prints "spam" 8 times
print
