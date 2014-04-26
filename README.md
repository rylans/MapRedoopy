MapRedoopy
==========

A wrapper on top of Python's built-in map function which first splits the input array into n parts, then spawns n processes in order to map asynchronously.

## Usage

Instead of:
```
result = map(f, list)
```

Use:
```
from mapredoopy import mappy
result = mappy(f, list, 4) #spawns four processes
```

## Purpose

Why did I write this code? For fun and practice.

## Todo list

* Write benchmark tests to show that async map is faster than sync map
* Make an async implementation of reduce
* Use (key, value) pairs as output
