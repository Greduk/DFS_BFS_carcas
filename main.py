import graphviz
import sets
import os
import copy
os.environ["PATH"] += os.pathsep + 'C:\\Program Files\\Graphviz\\bin\\'

checked_nodes = {}
stack = []
f = open('input.txt', 'r')
n = [[int(j) for j in list(filter(None, i.split(' ')))] for i in list(filter(None, f.read().split('\n')))]
f.close()

q = sets.adjacency_to_set(n)

q = [list(i) for i in q]
dot = graphviz.Digraph(comment='Graph', strict=True)
for i in range(len(q)):
	dot.node(str(i))
for i in range(len(q)):
	for j in range(len(q[i])):
		if q[i][j] > i:
			dot.edge(str(i), str(q[i][j]), arrowhead='none', color='white')

f = open('output_BFS.txt', 'w')
for qq in range(len(n)):
	if qq not in checked_nodes:
		stack.append(qq)
		checked_nodes[qq] = qq
		for zxc in stack:
			f.write(str(zxc) + ' ')
		f.write('\n')
		while len(stack) > 0:
			tmp = stack.pop(0)
			for zxc in stack:
				f.write(str(zxc) + ' ')
			f.write('\n')
			for i in range(len(n[tmp])):
				if n[tmp][i] == 1 and i not in checked_nodes:
					stack.append(i)
					checked_nodes[i] = tmp
					for zxc in stack:
						f.write(str(zxc) + ' ')
					f.write('\n')

dot1 = copy.deepcopy(dot)
for i in range(len(n)):
	if i == 0:
		continue
	dot1.edge(str(i), str(checked_nodes[i]), arrowhead='none', color='red')

dot1.render('karkas_bfs.gv', view=False)

del checked_nodes[0]

for i in range(1, len(n)):
	f.write(str(i) + ' ')
f.write('\n')
for i in range(1, len(n)):
	f.write(str(checked_nodes[i]) + ' ')
f.close()

checked_nodes = {}
stack = []
f = open('output_DFS.txt', 'w')
for qq in range(len(n)):
	if qq not in checked_nodes:
		stack.append(qq)
		checked_nodes[qq] = qq
		for zxc in stack:
			f.write(str(zxc) + ' ')
		f.write('\n')
		while len(stack) > 0:
			tmp = stack.pop()
			for zxc in stack:
				f.write(str(zxc) + ' ')
			f.write('\n')
			for i in range(len(n[tmp]) - 1, -1, -1):
				if n[tmp][i] == 1 and i not in checked_nodes:
					stack.append(i)
					checked_nodes[i] = tmp
					for zxc in stack:
						f.write(str(zxc) + ' ')
					f.write('\n')

for i in range(1, len(n)):
	f.write(str(i) + ' ')
f.write('\n')
for i in range(1, len(n)):
	f.write(str(checked_nodes[i]) + ' ')

f.close()

dot2 = dot
for i in range(len(n)):
	if i == 0:
		continue
	dot2.edge(str(i), str(checked_nodes[i]), arrowhead='none', color='blue')

dot2.render('karkas_dfs.gv', view=False)

print('Graph converted successfully.')
