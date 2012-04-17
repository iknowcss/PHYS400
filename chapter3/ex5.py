# 1) Write a function that draws a grid like the following:
#    + - - - - + - - - - +
#    |         |         |
#    |         |         |
#    |         |         |
#    |         |         |
#    + - - - - + - - - - +
#    |         |         |
#    |         |         |
#    |         |         |
#    |         |         |
#    + - - - - + - - - - +

def do_two(f):
	f()
	f()
	
def do_four(f):
	do_two(f)
	do_two(f)

def draw_grid_plus():
	print '+ - - - -',
	
def draw_grid_pipe():
	print '|        ',
	
def draw_grid_cap():
	do_two(draw_grid_plus)
	print '+'

def draw_grid_side():
	do_two(draw_grid_pipe)
	print '|'

def draw_grid_row():
	do_four(draw_grid_side)
	draw_grid_cap()
	
def draw_grid():
	draw_grid_cap()
	do_two(draw_grid_row)
	
draw_grid()
print

# 2) Use the previous function to draw a similar grid with four rows and four columns.
def draw_grid_cap():
	do_four(draw_grid_plus)
	print '+'

def draw_grid_side():
	do_four(draw_grid_pipe)
	print '|'

def draw_grid_row():
	do_four(draw_grid_side)
	draw_grid_cap()
	
def draw_grid():
	draw_grid_cap()
	do_four(draw_grid_row)
	
draw_grid()
