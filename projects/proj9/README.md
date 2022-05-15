### Problem Set 9: Reductions and NP Completeness 

## Overview

This homework will program the polynomial time reduction from 3SAT to k-Vertex Cover.

The input to the class with be an instance of 3SAT, and in each case, it will produce a graph and a value, such that there is a cover if and only if the 3SAT is satisfiable and the satisfying assignement to the 3SAT will be extracted from the vertex cover.
  
The text book explains the reductions.

On the reduced graph, we will do an exhaustive search for the vertex cover, and then interpret that back as a truth assignement for the 3SAT. Thus solving the 3SAT by solving the vertex cover.
