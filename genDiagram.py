from graphviz import Digraph
from utilize import ip2carrier
def GenDigraph(path = 'log_traceroute.log'):
    log = open(path, 'r')
    graph = Digraph(comment='The traceroute graph')
    lastCounter = 0
    counter = 1

    # Ingore the first three lines
    line = log.readline()
    line = log.readline()
    line = log.readline()

    breakcounter = 0
    while True:
        print('\r' 'Waiting for generating the graph...', end='')
        line = log.readline()
        if not line:
            break
        line = line.strip('\n').split()
        info = ip2carrier(line[1])
        if breakcounter == 3:
            break
        elif line[1] == '*':
            breakcounter += 1
        else:
            breakcounter = 0
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
                graph.edge(str(lastCounter), str(counter),'Status: '+status)
            lastCounter = counter
        counter += 1
    fileNames = path.replace('.log','.gv')
    graph.render(fileNames, view=True)
    log.close()

if __name__ == '__main__':
    GenDigraph()