from graphviz import Digraph
from utilize import ip2carrier
def GenDigraph():
    path = 'log_traceroute.log'
    log = open(path, 'r')
    graph = Digraph(comment='The traceroute graph')
    counter = 1

    # Ingore the first three lines
    line = log.readline()
    line = log.readline()
    line = log.readline()

    while True:
        line = log.readline()
        if not line:
            break
        line = line.strip('\n').split()
        info = ip2carrier(line[1])
        if line[1] == '*':
            break
        else:
            meg = (line[1] + '(' + str(info[0]) + ')' + '@' + str(info[1])).replace('None', 'Local')
            graph.node(str(counter), meg)
            if counter != 1:
                status = ''
                if(float(line[-2])<= 20):
                    status = 'Good'
                elif(float(line[-2])<= 40):
                    status = 'Normal'
                elif(float(line[-2])<= 100):
                    status = 'Not Bad'
                else:
                    status = 'Bad'
                graph.edge(str(counter-1), str(counter),'Status: '+status)
        counter += 1
    graph.render('./round-table.gv', view=True)
    log.close()

if __name__ == '__main__':
    GenDigraph()