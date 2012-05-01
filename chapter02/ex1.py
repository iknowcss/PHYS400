# The following statement will not assign the integer value 2492 to the 
# variable zipcode because it has a leading zero
# 
#  zipcode = 02492 
#
# However, if all of the tokens in the assignment number are 0-7, the statement
# executes with unexpected results

zipcode = 073405
print zipcode

# The integer "073405" is interpreted as the octal (base 8) expression of the
# decimal integer "30469".

# And now, a joke
print
print "Why is it that computer programmers confuse the dates Dec. 25"
print "and Oct. 31?"
print "Because 031 = " + str(031)
