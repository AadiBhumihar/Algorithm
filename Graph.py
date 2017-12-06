#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:28:20 2017

@author: bhumihar
"""

class Vertex :
    
    def __init__(self,node) :
        self.id = node
        self.visited = False
        
    def setVertexId(self,id):
        self.id = id;
        
    def getVertexId(self) :
        return self.id ;
    
    def setVisited(self) :
        self.visited = True ;
        
    def getVisited(self) :
        return self.visited ;

class Graph:
    def __init__(self,numvertex,cost=0) :
       self.adjMatrix = [[0]*numvertex for _ in range(numvertex)];
       self.numVertices = numvertex;
       self.vertices = [];
       for i in range(0,numvertex):
           vertex = Vertex(i)
           self.vertices.append(vertex)
           
    def setvertex(self,vtx,id) :
        if 0<= vtx <= self.numVertices :
            self.vertices[vtx].setVertexId(id);
            
    def getVertexindex(self,id) :
        for ix in range(0,self.numVertices) :
            if id == self.vertices[ix].getVertexId() :
                return ix ;
            
        else :
            return -1
        
    def addEdge(self,frm,to,cost=1) :
        
        if(self.getVertexindex(frm)!=-1 and self.getVertexindex(to)!=-1) :
            self.adjMatrix[self.getVertexindex(frm)][self.getVertexindex(to)] = cost ;
            #self.adjMatrix[self.getVertexindex(to)][self.getVertexindex(frm)] = cost ;
       
    def getvertices(self) :
        res_vertices = [];
        for ix in range(self.numVertices) :
            res_vertices.append(self.vertices[ix].getVertexId());
        return res_vertices ;
    
    def printMatrix(self) :
        print("   ","   ".join(self.getvertices()));
        for ix in range(self.numVertices) :
            print(self.vertices[ix].getVertexId(), " ", end="")
            for iy in range(self.numVertices) :
                print("%2d"%(self.adjMatrix[ix][iy]), " ", end="")
            print();
            
    def getEdges(self) :
        edges_res = []
        for ix in range(self.numVertices) :
            for iy in range(self.numVertices) :
                if (self.adjMatrix[ix][iy]!=0) :
                    frm  = self.vertices[ix].getVertexId();
                    to =   self.vertices[iy].getVertexId();
                    edges_res.append((frm,to,self.adjMatrix[ix][iy]))
        
        return edges_res ;
    
    
G =Graph(5)
G.setvertex(0,'a');
G.setvertex(1,'b');
G.setvertex(2,'c');
G.setvertex(3,'d');
G.setvertex(4,'e');

G.addEdge('a','e',10);
G.addEdge('a','c',20);
G.addEdge('c','b',30);
G.addEdge('b','e',40);
G.addEdge('e','d',50);
G.addEdge('f','e',60);

print("graph Data");
G.printMatrix()            
for item in G.getEdges() :
    print(item[0],'--->',item[1],'Cost:',item[2]);