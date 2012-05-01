# is_triangle function as defined in ex2.ipynb
def is_triangle(a, b, c):
    """If three sticks of lengths a, b, and c may be 
    arranged to form a triangle, print Yes; otherwise, 
    print No.
    """
    sides = [a, b, c]
    sides.sort()
    if (sides[0] + sides[1] >= sides[2]):
        print "Yes"
    else:
        print "No"

# prompt_triangle function as defined in ex2.ipynb
def prompt_triangle():
    """Gets 3 side lengths from the user and use is_triangle to determine 
    whether or not a triangle can be made using those lengths
    """
    print "Input 3 lengths to be used as triangle sides:"
    a = int(raw_input(" a = "));
    b = int(raw_input(" b = "));
    c = int(raw_input(" c = "));

    print "Can you make a triangle from these side lengths?"
    is_triangle(a, b, c)

# Call the function
prompt_triangle();
