from graphviz import Digraph
import os

class DrawGraph:
    def __init__(self, relations, dist=os.path.join(os.path.dirname(os.path.abspath(__file__)),'./dist/sample')):
        self.dg = Digraph(format='png')
        self.dist = dist
        self.relations = relations

    def save(self):
        self.dg.render(self.dist)


    def draw(self):
        for k in self.relations.keys():
            self.dg.node(k)
        for k, v_list in self.relations.items():
            for v in v_list:
                self.dg.edge(v,k)

if __name__ == '__main__':
    data = {'1':['1'],'2':['1'],'3':['1','2']}
    draw = DrawGraph(data)
    draw.draw()
    draw.save()
    