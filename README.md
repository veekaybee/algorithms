## Grokking Algorithms

Working through [Grokking Algorithms](https://www.manning.com/books/grokking-algorithms) by Aditya Bhargava.
In Python 2.7. Code mostly modified to examine output and debut.  


## Chapter 1

+ binary.py - Binary search, Chapter 1

### Answers to Exercises

1)  Most steps with list of size 128

		import math
		math.log(128,2)
		7.0

2)  Most steps with doubled list

	math.log(265,2)
	8.049848549450562

Looking at some other values, the delta of steps between `math.log(n,2)` and `math.log(2n,2)` is approximately 1. 6