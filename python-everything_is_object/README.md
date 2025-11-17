# Python - Everything Is Object

<div align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Python Objects" width="150"/>
<p><strong>Python is awesome!!!</strong></p>
</div>


## Introduction
In Python, **everything  is an object**. This means that all values like numbers, strings, lists and even functions are objects stored in memory. Understanding objects, their types, and how Python handles them is very important for programming, especially for avoiding bugs with variables and functions.

## id and type
Python gives each object a **type** and  an **id**. Every object in Python has a unique ID and a type.
- `type(obj)`shows the type of the object.
- `id(obj)` shows the memory address of the object.

Example:

```python
a = 10
print (type(a)) #<class 'int'>
print (id(a)) #memory address
```
`type`tells us what **the object it is**. `id` tells us **where it is in memory**.

##Mutable Objects
Mutable objects can  be **changed in place** without creating a new object. Common mutables objects are **lists, dictionnaries and sets**. When modified their id remains the same.

Example:

```python
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2) #[1, 2, 3, 4]
print(l1 is l2) #True
print(l1 == l2) #True
```

Here, l1 and l2 point to the same list, so when we add 4 to `l1`,`l2`also changes.
`l1 is l2` is true because l1 et l2 point to the same object
`l1 == l2` is too true because the content is the same

## Immutable Objects
Immutable Objects can not be changed after creation. Common examples are **Integers, floats, bool, strings and tuples**.
If you try to change them, this creates a new object and a new ID.

Example:
```python
a = 1
b = a
print("id(a) before:", id(a))

a += 1

print(b) # 1
print(a) #2

print("id(a) after:", id(a)) # new ID for a

print(a == b) #False
print(a is b) #False
```

`a == b`is false because the values are differents.
`a is b`is false because the two objects differents.
Even though we increased `a`,`b` stays  the same because integers are immutable. Python created a **new object** for `a`.

## Why it matters?
Understanding mutable vs immutable is important because Python treats them **differently in memory**.
- Mutable objects can change without creating a new object.
- Immutable objects always create a new object if you try to change them.

![Description image](img.png)

Example with lists vs integers:

```python
l = [1, 2]
l += [3] #modifies the same object

i = 10
i += 1 #creates a new object
```

## How arguments are passed to functions
Python passes variables by **assignement** (sometimes called pass-by-object-reference).
- For **mutable objects**, functions can modify the original object.
- For **immutable objects**, functions can not modify the original object.

Example:

```python
def add_item(lst):
    lst.append(4)

my_list = [1, 2, 3]
add_item(my_list)
print(my_list)  #[1, 2, 3, 4]

def add_one(a_list):
    n += 1

a = 1
add_one(a)
print(a) #1 stay the same
```
