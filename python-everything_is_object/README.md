Python – Everything is Object

Project Badge

Master – By Guillaume
Weight: 1

Your score will be updated as you progress.
A Manual QA review must be requested once you complete the project.

📘 Description
🔎 Background Context

Now that we understand that everything in Python is an object, let’s take a deeper look at how Python handles different object types.

Have you ever modified a variable without intending to?

>>> a = 1
>>> b = a
>>> a = 2
>>> b
1


But what about this?

>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]


This project is different from the usual ones.
The first part is composed of conceptual questions such as:

“What would be the result of…?”

You must read all the documentation first, then think, reason, and try to understand how Python works internally.

Do not start by testing everything in a Python interpreter.
Instead: read → think → brainstorm → then test.

Understanding these concepts is essential, especially for Python job interviews, where such questions frequently appear.

🎯 Learning Objectives

By the end of this project, you should be able to explain (without Google):

General Concepts

What is an object

Difference between a class and an instance/object

Difference between mutable and immutable objects

What is a reference

What is an assignment

What is an alias

How to check if two variables are identical

How to check if two variables refer to the same object

How to display a variable’s identifier (id())

Built-in mutable types

Built-in immutable types

How Python passes variables to functions

🛠 Requirements
Python Scripts

Editors allowed: vi, vim, emacs

Interpreted/compiled on Ubuntu 20.04 LTS, Python 3.8.5

Files must end with a newline

First line must be:

#!/usr/bin/python3


Follow pycodestyle 2.7.*

All files must be executable

File length is checked using wc

.txt Answer Files

Only one line

No shebang

Must end with a newline

📂 Tasks Summary

This project includes tasks such as:

Identifying object types

Understanding object identity vs equality

Working with mutable and immutable objects

Behavior of lists vs integers in function calls

Creating a function to copy a list

Determining whether something is a tuple

Understanding how Python handles list concatenation and mutation

Writing a blog post summarizing all concepts learned

For example:

Task examples include:

type function

id function

Whether variables point to the same object

How lists behave when modified

How += differs from + for lists

The final task (Task 29) requires writing a blog post on Medium or LinkedIn covering:

Introduction

id and type

Mutable objects

Immutable objects

Why mutability matters

Function argument passing

Advanced observations (if applicable)

You must include examples and at least one picture.