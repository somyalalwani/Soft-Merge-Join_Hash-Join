# SortMerge Join & Hash Join

- Not used any external library/jarfiles.
- Language Used :Python

Given M memory blocks and two large relations R(X,Y)and S(Y,Z). Develop iterator for the following operations.

```
● SortMerge Join
- open() - Create sorted sublists for R and S, eachof size M blocks.
- getnext() - Use 1 block for each sublist and get minimumof R & S. Join this minimum Y value with the other table and return. Checkfor B(R)+B(S)<M^2
- close() - close all files


● Hash Join
- open() - Create M1 hashed sublists for R and S
- getnext() - For each Ri and Si thus created, loadthe smaller of the two in the main memory and create a search structure over it.You can use M1 blocks to achieve this. Then recursively load the other filein the remaining blocks and for each record of this file, search correspondingrecords (with same join attribute value) from the other file.
- close() - close all files
```

**Join condition** (R.Y==S.Y).

Use 1 block for output which is filled by row returnedby getnext() and when it gets full, append it to the output file and continue.

**Input Parameters:**

1. Path to file containing relation R
2. Path to file containing relation S
3. Type of join sort/hash
4. Number of blocks M

**Attribute Type :**
Note that all attributes, X, Y and Z are strings andY may be a non-key attribute.

**Block Size :**
Assume that each block can store 100 tuples for bothrelations, R and S.


**Input format :**

```
2020201092.sh <path of R file> <path of S file><sort/hash> <M>
```

**Output file:** 
```
<R filename>_<S filename>_join.txt
```
