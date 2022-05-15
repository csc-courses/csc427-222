## Problem Set 9: Reductions and NP Completeness 

### Overview

This homework will program the polynomial time reduction from 3SAT to k-Vertex Cover.

The input to the class with be an instance of 3SAT, and in each case, it will produce a graph and a value, such that there is a cover if and only if the 3SAT is satisfiable and the satisfying assignement to the 3SAT will be extracted from the vertex cover.
  
The text book explains the reductions.

On the reduced graph, we will do an exhaustive search for the vertex cover, and then interpret that back as a truth assignement for the 3SAT. Thus solving the 3SAT by solving the vertex cover.

### Data representations

We shall represent a SAT instance as a list of clauses, where each clause is a list of pairs, where each pair is a variable name and the integer 0 if the variable appears alone, and 1 if the variable appears complemented. Note that this is the same represenntation as in the previous problem set. In our use, there shall be exactly three variables in any clause.

We will wrap a CNF inside an instance of a CNF object which adds a few useful methods.

A graph will be represented as an instance of a Graph class. The vertices and edges will be represented as lists.

It is not necessary to proceed in this manner, but I have suggested that the names of the vertices of the graph be derived from the names of the appearances of the variables, as they appear in the formula. That a variable can appear multiple times, each with a distinct name, can be handled by forming a pair, with the name in the form of the CNF an integer index, which continuously increments with each vertex.
<pre>
     vertex := ( (name: string, logic: {0,1}), index: integer )
</pre>


The classes Graph and CNF are provided for you.

### Project

The Reduce_3SAT_VCover class is instantiated with a CNF object. The _makegraph creates the Graph object with the vertices and edges in the reduction from 3SAT to vertex cover for the cnf formula given at the instantiation of the Reduce_3SAT_VCover instance.

I have suggested a format for the vertices of the graph. If the vertex widgets are created first, there will be an easy way to tell those vertices that are part of any vertex widget and those that are part of any clause widget, because of the index of the any vertex widget has a precise bound. This observation may be helpful.

Once built, and the computed, the function findcover finds the vertex cover using exhaustive search. 

Finally, the function solvecnf takes the cover and extracts the associated True/False values of the variables, returning it as a dictionary suitable for tesing by the CNF.issatisfied function.
