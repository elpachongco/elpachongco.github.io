---
layout: post
title:  "Code Snippets #0: Deploy when port exists using recursion"
date:   2022-07-19 20:40:26 +0800
categories: programming, code-snippets
---

I'm starting a new category of posts called "Code Snippets" where I share code
I find interesting. 

In this first installment is a simple code snippet I originally wrote in Powershell
to scan a local port continuously and do something when the port is
found:

```python
function deploy(): 
	if ( port_exists(port) ):
		do_something()
	else: 
		deploy()

deploy()
```

Recursion has been a hard concept for me to put into practice and this served
as a good introduction to it. However, this doesn't feel like a 'proper'
recursion to me. 

I was so satisfied with this code so I showed it to my programmer co-worker
friend. He asked me what will happen if the program doesn't ever find the port?
I didn't think much of it because I know the user can just close the program
and the port scanning is slow enough (around 1 sec for each function call). 

I later realized what he meant. Being a better programmer than me, he knew
something was missing. And so, let's try to improve the code.  

```python
function deploy(retries):
	
	if ( retries < 1 ): 
		raise Exception("Port not found, Maximum retries reached.")

	if ( port_exists(port) ):
		do_something()
	else: 
		deploy(retries-1)

# Limit retries to n
n = 10
deploy(n) 
```

This feels more like recursion. The program will now only do a maximum of `n`
retries. After that, if the port still doesn't exist, it will throw an error. 

The reason why I said the previous code didn't feel like a proper recursion was
because it didn't limit the number of times it can call itself.

This limit is called the base case. In the code:

```python
function deploy(retries):
	
	if (retries < 1 ): # <--- This is the Base case
		raise Exception("Port not found, Maximum retries reached.")

	if ( port_exists(port) ):
		do_something()
	else: 
		deploy(retries-1) 

# Limit retries to n
n = 10
deploy(n) 
```

The base case is a condition where if it is true, it stops the recursion.

Without the base case, some recursive functions could result to infinite
recursions — something that should not happen, hence why the computer will
throw an error (usually a stack overflow) when it finds an infinite recursive
function.

For example, you can try to run this python code: 

```python
def a(b):
	return a(b+1)

a(1)
```

In this code, nothing will stop `a` from calling itself again which could be
problematic. This is why adding the base case and a way to achieve the base
case is important.

Back to the code snippet, what else can we do to improve the code?

Here's an idea: add a time.sleep() before each recurse to prevent the code
from executing too fast and eating unnecessary memory:

```python
import time
function deploy(retries):
	
	if (retries < 1 ): 
		raise Exception("Port not found, Maximum retries reached.")

	if ( port_exists(port) ):
		do_something()
	else: 
		time.sleep(1) # <--- Do a 1-second sleep before every recurse
		deploy(retries-1)

# Limit retries to n
n = 10
deploy(n) 
```

Without the `time.sleep(1)`, the program will loop as fast as it can, faster
than what the code needs to be which will just waste our computer's resources
especially if the `port_exists` function consumes a lot of memory or cpu when
called. 

Note: I mentioned earlier that the port scanning takes 1 second so adding a
time.sleep(1) will make the program scan every 2 seconds. I didn't add that to
my original code but in this case, I added it since it's a different program.

That's it for this code snippet. Try to improve the code, and maybe publish it.
I will be happy to read them :).

To end this episode, I'll give you something to think about. Here's the same
program but instead of recursion, it uses a while loop:

```python
function deploy(retries):
	
	while not port_exists(port):
		if ( retries < 1 ): 
			raise Exception("Port not found, Maximum retries reached.")
		retries -= 1

	do_something()

# Limit retries to n
n = 10
deploy(n) 
```

Practice your programming skills and think of these questions:

1. What are the advantages and disadvantages of using recursion or
   iteration (i.e. a while loop)? 
2. What types of situations does it make sense to use recursion versus
   iteration? 

I will leave you, the reader to answer these questions. See you in the next
Code Snippet! 
