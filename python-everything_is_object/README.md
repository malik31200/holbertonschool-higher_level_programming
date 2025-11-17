Python – Everything is Object

Project Badge – Master
By: Guillaume
Weight: 1

Your score updates as you progress.
A Manual QA review is required when the project is finished.

📘 Description
🔎 Background Context

Now that we understand that everything in Python is an object, we will explore how Python handles object identity, mutability, aliasing, and assignment.

Example:

>>> a = 1
>>> b = a
>>> a = 2
>>> b
1


But lists behave differently:

>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]


This project is composed of many questions about Python’s internals.
Do not start by testing everything in the interpreter.
Instead:

👉 Read → Think → Understand → Then test

These concepts are extremely useful in Python interviews.

📚 Resources

You must read/watch:

9.10. Objects and values

9.11. Aliasing

Immutable vs mutable types

Mutation (this chapter only)

9.12. Cloning lists

Python tuples: immutable but potentially changing

🎯 Learning Objectives

You must understand:

General

What is an object

Difference between class and object/instance

Mutable vs immutable objects

What is a reference

What is an assignment

What is an alias

How to know if two variables are identical

How to know if two variables refer to the same object

How to display a variable’s identifier (the CPython memory address)

Built-in mutable types

Built-in immutable types

How Python passes variables to functions

🛠 Requirements
Python Scripts

Allowed editors: vi, vim, emacs

Executed with Python 3.8.5 on Ubuntu 20.04

Must end with a newline

First line must be:

#!/usr/bin/python3


Follow pycodestyle 2.7.*

Must be executable

Length checked with wc

.txt Answer Files

One line only

No shebang

Must end with a newline

✅ Tasks

Below is the full list of tasks included in the project (all tasks are preserved):

0. Who am I?

Write the name of the function used to print the type of an object (without ()).

File: 0-answer.txt

1. Where are you?

Write the function name that returns a variable’s identifier (memory address in CPython).

File: 1-answer.txt

2. Right count

Do a and b point to the same object?

a = 89
b = 100


File: 2-answer.txt

3. Right count =

Do a and b point to the same object?

a = 89
b = 89


File: 3-answer.txt

4. Right count =

Do a and b point to the same object?

a = 89
b = a


File: 4-answer.txt

5. Right count =+

Do they point to the same object?

a = 89
b = a + 1


File: 5-answer.txt

6. Is equal

What does this print?

s1 = "Best School"
s2 = s1
print(s1 == s2)


File: 6-answer.txt

7. Is the same

What does this print?

s1 = "Best"
s2 = s1
print(s1 is s2)


File: 7-answer.txt

8. Is really equal

What does this print?

s1 = "Best School"
s2 = "Best School"
print(s1 == s2)


File: 8-answer.txt

9. Is really the same

What does this print?

s1 = "Best School"
s2 = "Best School"
print(s1 is s2)


File: 9-answer.txt

10. List equal

What does this print?

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)


File: 10-answer.txt

11. List is the same

What does this print?

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 is l2)


File: 11-answer.txt

12. List really equal
l1 = [1, 2, 3]
l2 = l1
print(l1 == l2)


File: 12-answer.txt

13. List really the same
l1 = [1, 2, 3]
l2 = l1
print(l1 is l2)


File: 13-answer.txt

14. List append
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)


File: 14-answer.txt

15. List add
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)


File: 15-answer.txt

16. Integer incrementation
def increment(n):
    n += 1

a = 1
increment(a)
print(a)


File: 16-answer.txt

17. List incrementation
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)


File: 17-answer.txt

18. List assignation
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)


File: 18-answer.txt

19. Copy a list

Create:

def copy_list(a_list):
    return a_list.copy()


File: 19-copy_list.py

20. Tuple or not?
a = ()


Is a a tuple?
File: 20-answer.txt

21. Tuple or not?
a = (1, 2)


File: 21-answer.txt

22. Tuple or not?
a = (1)


File: 22-answer.txt

23. Tuple or not?
a = (1,)


File: 23-answer.txt

24. Who I am?
a = (1)
b = (1)
a is b


File: 24-answer.txt

25. Tuple or not
a = (1, 2)
b = (1, 2)
a is b


File: 25-answer.txt

26. Empty is not empty
a = ()
b = ()
a is b


File: 26-answer.txt

27. Still the same?
id(a)
a = a + [5]
id(a)


Will the last line print the same ID?

File: 27-answer.txt

28. Same or not?
a += [4]


Does the ID stay the same?

File: 28-answer.txt

29. Blog post

Write a detailed post with:

Introduction

id and type

Mutable objects

Immutable objects

Why mutability matters

Function argument passing

Advanced tasks (optional)

Publish on Medium/LinkedIn.
Provide URLs.