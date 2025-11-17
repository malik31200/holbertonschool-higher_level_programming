# Python - Everythink Is Object

![Python Objects](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

##Introduction
In Python, **everything  is an object**. This means that all values like numbers, strings, lists and even functions are objects stored in memory. Understanding objects, their types, and how Python handles them is very important for programming, especially for avoiding bugs with variables and functions.

## id and type
Python gives each object a **type** and  an **id**.
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
Mutable objects can  be **changed in place** without creating a new object. Common mutables objects are **lists, dictionnaries and sets**.

Example:

```python
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2) #[1, 2, 3, 4]
```

Here, l1 and l2 point to the same list, so when we add 4 to `l1`,`l2`also changes.

##Immutable Objects
Immutable Objects can not be changed after creation. Common examples are **Integers, strings and tuples**.

Example:
```python
a = 1
b = a
a += 1
print(b) # 1
```

Even though we increased `a`,`b` stays  the same because integers are immutable. Python created a **new object** for `a`.

##Why it matters?
Understanding mutable vs immutable is important because Python treats them **differently in memory**.
- Mutable objects can change without creating a new object.
- Immutable objects always create a new object if you try to change them.

Example
