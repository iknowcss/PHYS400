# Exercise 7.4
def eval_loop():
    """Takes input from the user and evaluates it using the python
    interpreter until the user types "done" at which point eval_loop()
    returns the last evaluated result
    """
    i = 1
    result = None
    while True:
        print "In [" + str(i) + "]:",
        instruction = raw_input();
        if instruction == "done":
            return result;
        result = eval(instruction)
        print result
        i += 1

# Fire it up!
print "The last result was " + str(eval_loop())
