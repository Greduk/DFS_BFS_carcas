import graphviz
import sets
import os
os.environ["PATH"] += os.pathsep + 'C:\\Program Files\\Graphviz\\bin\\'

checked_nodes = [0]
stack = [0]
f = open('input.txt', 'r')
n = [[int(j) for j in list(filter(None, i.split(' ')))] for i in list(filter(None, f.read().split('\n')))]
f.close()

f = open('output_BFS.txt', 'w')
while len(stack) > 0:
	for i in stack:
		f.write(str(i) + ' ')
	f.write('\n')
	tmp = stack.pop(0)
	for i in range(len(n[tmp])):
		if n[tmp][i] == 1 and i not in checked_nodes:
			stack.append(i)
			checked_nodes.append(i)

f.close()

checked_nodes = [0]
stack = [0]
f = open('output_DFS.txt', 'w')
while len(stack) > 0:
	for i in stack:
		f.write(str(i) + ' ')
	f.write('\n')
	tmp = stack.pop()
	for i in range(len(n[tmp]) - 1, -1, -1):
		if n[tmp][i] == 1 and i not in checked_nodes:
			stack.append(i)
			checked_nodes.append(i)

f.close()

q = sets.adjacency_to_set(n)

q = [list(i) for i in q]
dot = graphviz.Digraph(comment='Graph')
for i in range(len(q)):
	dot.node(str(i))
for i in range(len(q)):
	for j in range(len(q[i])):
		if q[i][j] > i:
			dot.edge(str(i), str(q[i][j]), arrowhead='none')

dot.render('graph.gv', view=False)
print('Graph converted successfully.')
