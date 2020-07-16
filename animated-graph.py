import time, os, sys, curses, math, select

rows, columns = os.popen('stty size', 'r').read().split()
rows = int(rows)
columns = int(columns)

a = 10
b = 0.1
c = 0

b_sign = -1
b_upper = 0.117
b_lower = 0
b_increment = 0.0008

b_frames = (b_upper - b_lower) / b_increment

a_upper = 13
a_lower = 7
a_increment = (a_upper - a_lower) / b_frames

c_increment = -1 * b_increment * 300

while True:
	x = 0
	y = 0
	y_vals = []
	string = "o"

	for x in range(0, columns+1):
		y = a * math.sin(b*x + c) + 15

		if(y <= rows):
			y = int(round(y))
			y_vals.append(y)

	#print(y_vals)

	decrement = 0
	x_val = 0
	graph = []
	string = ""

	for y in range(0, rows):
		y = rows - decrement

		for x in range(1, len(y_vals)):
			if y_vals[x] == y:
				string += "+"
			else:
				string += " "

		graph.append(string)
		string = ""
		decrement += 1

	for l in graph:
		print(l)

	if b > b_upper:
		b_sign = -1
	elif b < b_lower:
		b_sign = 1

	b += b_sign * b_increment

	a += b_sign * a_increment

	c += c_increment

	time.sleep(0.04)



'''
graph_instruct = ""
space_block = ""

for l in graph:
	for c in l:
		if(c == " "):
			space_block += c
		else:
			graph_instruct += 'sys.stdout.write("' + space_block + '")\n'
			graph_instruct += 'sys.stdout.write("' + c + '")\n'
			space_block = ""

exec(graph_instruct)
'''
