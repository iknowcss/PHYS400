width = 17
height = 12.0
delimiter = '.'

# 1) width/2
#    This will yield "8". The variable "width" is assigned an integer. When
#    width is divided by 2, you expect the answer should be 8.5. However, 
#    since width is an integer and 2 is an integer, the yielded value must also
#    be an integer. The numbers following the decimal point are truncated.
print width/2

# 2) width/2.0
#    This will yield "8.5". As before the variable "width" is assigned an 
#    integer. When width is divided by 2.0, the answer is be 8.5 as you expect.
#    Width is an integer but 2.0 is a float. Any time one of the operands is a
#    float, the result is a float
print width/2.0

# 3) height/3
#    This will yield "4.0". "height" is a float and 3 is an integer, so the 
#    result is a float
print height/3

# 4) 1 + 2 * 5
#    According to order of operations, multiplication takes precidence over 
#    addition, so 2 * 5 will be added to 1 yielding 11
print 1 + 2 * 5

# 5) delimiter * 5
#    When the multiplication operator is applied to a string and an int, a new
#    string is returned with the initial string repeated an integer number of 
#    times. In this case, "delimiter" has the string value ".", so 
#    delimiter * 5 will yield "....."
print delimiter * 5
