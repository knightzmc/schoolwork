# Graphs

Graphs represent objects and the connections between them, eg flight paths between cities

Each object in the graph is called a Vertex (Vertices)
Each connection is called an edge
Neighbors are vertices connected by an edge
Degree of a node is how many edges is has

## Weighted Graphs

A weighted graph is one in which the edges are labelled, with distances for example

## Directed Graphs

In a directed graph, each edge has a direction associated with it, and it can only be traversed in that direction

## Adjacency Matrix

An adjacency matrix can be used to represent a graph in a form that can be processed by a computer

If 2 vertices are connected a 1 is placed in the matrix in 2 positions, therefore for an undirected graph the matrix will be symmetrical

The remaining spaces are then filled with 0s or nulls

If the graph was weighted, you'd store the weight rather than 1 or 0 in the matrix

## Adjacency List

An adjacency list is an alternative method for representing a graph
For each vertex, it lists the adjacent vertices

Adjacency lists are best used when there are few edges between vertices
