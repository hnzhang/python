import turtle


def draw_tree(branch_len, t):
	'''
	'''
	step = 10
	if branch_len >step:
		if branch_len < 2*step:
			t.color("green")
		t.forward(branch_len)

		t.right(20)
		draw_tree(branch_len -step, t)
		
		t.left(40)
		draw_tree(branch_len-step, t)
		t.right(20)
		t.backward(branch_len)
		t.color("brown")
def main():
	'''
	'''
	my_turtle = turtle.Turtle()
	my_win = turtle.Screen()
	my_turtle.left(90)
	my_turtle.up()
	my_turtle.backward(330)
	my_turtle.down()
	my_turtle.color("green")
	draw_tree(100, my_turtle)
	my_win.exitonclick()

main()
