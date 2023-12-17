from graphviz import Digraph
dot = Digraph(comment='The Round Table')
dot.node('A', label = 'QQ') 
dot.node('B', label = 'www')
dot.edge("A", "B", label = "Like")
dot.render('test-output/round-table.gv', view=True)  # doctest: +SKIP
str(dot)