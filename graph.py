import time, os, sys, curses, math, select

rows, columns = os.popen('stty size', 'r').read().split()
rows = int(rows)
columns = int(columns)

x = 0
y = 0
y_vals = []

string = "o"

def largest(arr):
	max = arr[0]

	for i in range(1, len(arr)):
		if(arr[i] > max):
			max = arr[i]

	return max

for x in range(0, columns+1):
	y = 20 * math.sin(0.1*x) + 10

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
			string += "o"
		else:
			string += " "

	graph.append(string)
	string = ""
	decrement += 1

blank_line = ""

for i in range(0, columns):
	blank_line += " "

curses.initscr()

for l in graph:
	sys.stdout.write(l)
	if(l != blank_line):
		time.sleep(0.01)

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
