
class Graph:
    def __init__(self):
        self.graph = {}
    
    def addVertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def addEdge(self,vertex1,vertex2,isDirected=False):
        self.addVertex(vertex1)
        self.addVertex(vertex2)
        self.graph[vertex1].append(vertex2)
        if not isDirected:
            self.graph[vertex2].append(vertex1)

    def showGraph(self,vertex=None):
        if not vertex:
            print(self.graph)
            return
        print(self.graph[vertex])
    
    def display(self):
        for k,v in self.graph.items():
            print(k," -> ",v)

    def getVertices(self):
        for k in self.graph:
            print(k,end=" ")
        print()
    
    def getEdges(self,vertex=None):
        if not vertex:
            for k,v in self.graph.items():
                for vertex in v:
                    print(f"({k},{vertex})")
            return
        for v in self.graph[vertex]:
            print(f"({vertex},{v})")

    def removeVertex(self,vertex):
        if vertex in self.graph:
            del self.graph[vertex]
        
            for k,v in self.graph.items():
                if vertex in v:
                    v.remove(vertex)
    
    def isEdge(self,vertex1,vertex2):
        return vertex1 in self.graph[vertex2] or vertex2 in self.graph[vertex1]
            
    def removeEdge(self,vertex1,vertex2):
        if self.isEdge(vertex1,vertex2):
            self.graph[vertex1].remove(vertex2)
            self.graph[vertex2].remove(vertex1)

if __name__ == "__main__":
    gr = Graph()

    gr.addEdge("A","B")
    gr.addEdge("B","C")
    gr.addEdge("C","D")
    gr.addEdge("B","D")


    gr.display()
    gr.removeEdge("A","B")
    gr.display()