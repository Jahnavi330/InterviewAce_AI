# Python Developer Interview Guide

A comprehensive, interview-ready reference covering core Python concepts with definitions, explanations, examples, and best practices. Organized for quick lookup and deep review.

## Table of Contents

1. [Variables and Data Types](#1-variables-and-data-types)
2. [Object-Oriented Programming (OOP)](#2-object-oriented-programming-oop)
3. [Decorators](#3-decorators)
4. [Generators](#4-generators)
5. [Exception Handling](#5-exception-handling)
6. [File Handling](#6-file-handling)
7. [Iterators and Iterables](#7-iterators-and-iterables)
8. [Lambda Functions](#8-lambda-functions)
9. [Comprehensions](#9-comprehensions)
10. [Modules and Packages](#10-modules-and-packages)
11. [Common Pitfalls](#11-common-pitfalls)
12. [Quick Reference Cheat Sheet](#12-quick-reference-cheat-sheet)

---

## 1. Variables and Data Types

### 1.1 Variables

**Definition:** A variable in Python is a named reference to an object stored in memory. Python is **dynamically typed**, meaning a variable's type is determined at runtime based on the object it references, and variables can be reassigned to objects of different types.

```python
x = 10          # x references an int object
x = "hello"     # x now references a str object
```

**Key Concept — Names vs. Objects:** Python variables are labels (references) pointing to objects, not fixed memory boxes holding values. Multiple names can point to the same object.

```python
a = [1, 2, 3]
b = a           # b points to the SAME list object as a
b.append(4)
print(a)        # [1, 2, 3, 4] -- a is affected too
```

**Variable Naming Rules:**
- Must start with a letter or underscore, followed by letters, digits, or underscores.
- Case-sensitive (`age` ≠ `Age`).
- Cannot be a reserved keyword (`class`, `for`, `import`, etc.).
- Convention: `snake_case` for variables/functions, `PascalCase` for classes, `UPPER_SNAKE_CASE` for constants (PEP 8).

**Best Practices:**
- Use descriptive names (`user_count` instead of `uc`).
- Avoid shadowing built-ins (`list`, `dict`, `type`, `id`, `str`).
- Use type hints for clarity in production code: `age: int = 25`.

### 1.2 Built-in Data Types

Python's built-in types fall into several categories:

| Category | Types | Mutable? |
|---|---|---|
| Numeric | `int`, `float`, `complex` | No |
| Sequence | `str`, `list`, `tuple`, `range` | `list` mutable; `str`, `tuple`, `range` immutable |
| Mapping | `dict` | Yes |
| Set | `set`, `frozenset` | `set` mutable; `frozenset` immutable |
| Boolean | `bool` | No |
| Binary | `bytes`, `bytearray`, `memoryview` | `bytearray` mutable; `bytes` immutable |
| None | `NoneType` | N/A |

#### Numeric Types

```python
i = 42            # int - arbitrary precision, no overflow
f = 3.14           # float - double precision (64-bit)
c = 2 + 3j          # complex - has real and imaginary parts
print(type(i), type(f), type(c))
```

- Python integers have **arbitrary precision** (limited only by memory), unlike fixed-width integers in C/Java.
- Floating point numbers follow IEEE 754 double precision, so they suffer from **rounding errors**:

```python
print(0.1 + 0.2)   # 0.30000000000000004
```

**Best Practice:** For exact decimal arithmetic (e.g., currency), use the `decimal` module. For rational numbers, use `fractions.Fraction`.

#### Strings (`str`)

**Definition:** An immutable sequence of Unicode characters.

```python
s = "Hello, World!"
s2 = 'Single quotes work too'
s3 = """Triple-quoted
multiline string"""
```

Common operations:

```python
s.upper()           # "HELLO, WORLD!"
s.lower()            # "hello, world!"
s.split(",")         # ["Hello", " World!"]
s.strip()            # remove leading/trailing whitespace
s.replace("H", "J")  # "Jello, World!"
s[0:5]                # slicing -> "Hello"
f"{s} - {len(s)}"     # f-strings (Python 3.6+), preferred formatting
```

**Immutability:** Any operation that appears to "modify" a string actually creates a new string object.

```python
s = "hello"
id_before = id(s)
s += " world"
print(id(s) == id_before)  # False
```

**Best Practice:** For building strings in a loop, use `str.join()` or a `list` + join instead of repeated `+=`, which is O(n²) due to immutability.

```python
# Inefficient
result = ""
for word in words:
    result += word

# Efficient
result = "".join(words)
```

#### Lists (`list`)

**Definition:** A mutable, ordered sequence of objects (heterogeneous types allowed).

```python
nums = [1, 2, 3]
nums.append(4)        # [1, 2, 3, 4]
nums.insert(0, 0)      # [0, 1, 2, 3, 4]
nums.pop()             # removes and returns last item
nums[1:3]              # slicing -> [1, 2]
```

Lists are implemented as dynamic arrays: indexing is O(1), appending is amortized O(1), and inserting/removing from the front is O(n).

#### Tuples (`tuple`)

**Definition:** An immutable, ordered sequence, typically used for fixed collections of heterogeneous data (e.g., coordinates, database rows).

```python
point = (3, 4)
x, y = point            # tuple unpacking
single = (5,)            # trailing comma needed for a 1-element tuple
```

**Why use tuples over lists?**
- Immutability makes them hashable (usable as dict keys / set members) if all elements are hashable.
- Signals intent: "this collection shouldn't change."
- Slightly more memory-efficient and faster to construct than lists.

```python
locations = {(0, 0): "origin", (1, 1): "diagonal"}  # tuple as dict key
```

#### Dictionaries (`dict`)

**Definition:** A mutable mapping of unique, hashable keys to values. Since Python 3.7, dicts maintain **insertion order** as a language guarantee.

```python
person = {"name": "Alice", "age": 30}
person["email"] = "alice@example.com"   # add/update
person.get("phone", "N/A")               # safe access with default
del person["age"]
for key, value in person.items():
    print(key, value)
```

Average time complexity: O(1) for lookup, insert, and delete (backed by a hash table).

**Best Practice:** Use `dict.get()` or `collections.defaultdict` instead of checking `if key in dict` followed by access, to avoid double lookups.

```python
from collections import defaultdict
counts = defaultdict(int)
for word in words:
    counts[word] += 1
```

#### Sets (`set`)

**Definition:** A mutable, unordered collection of unique, hashable elements. Backed by a hash table, supporting fast membership tests and set algebra.

```python
a = {1, 2, 3}
b = {2, 3, 4}
a | b     # union -> {1, 2, 3, 4}
a & b     # intersection -> {2, 3}
a - b     # difference -> {1}
a ^ b     # symmetric difference -> {1, 4}
2 in a    # O(1) membership test
```

Use `frozenset` for an immutable, hashable version (usable as a dict key or set element).

#### Booleans and `None`

```python
is_active = True
result = None   # represents "no value" / absence of data
```

**Truthiness:** Every object has an inherent boolean value. Falsy values include: `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `()`.

```python
if []:
    print("won't print")   # empty list is falsy
```

**Best Practice:** Use `is None` / `is not None` to check for `None`, not `== None`, because `is` checks identity and avoids issues with custom `__eq__` overrides.

### 1.3 Type Conversion

```python
int("42")        # 42
float("3.14")     # 3.14
str(100)          # "100"
list("abc")        # ['a', 'b', 'c']
bool(0)            # False
```

Implicit conversions ("coercion") occur in mixed arithmetic (`int` + `float` → `float`), but Python generally avoids silent, unsafe coercions (e.g., `"1" + 1` raises `TypeError`, unlike JavaScript).

### 1.4 Mutability Summary

| Immutable | Mutable |
|---|---|
| `int`, `float`, `complex`, `bool` | `list` |
| `str` | `dict` |
| `tuple` | `set` |
| `frozenset` | `bytearray` |
| `bytes` | custom objects (by default) |

**Interview Tip:** A classic gotcha is using a mutable default argument:

```python
def add_item(item, basket=[]):   # BAD - default list is shared across calls
    basket.append(item)
    return basket

print(add_item("apple"))   # ['apple']
print(add_item("banana"))  # ['apple', 'banana']  <- unexpected!
```

**Fix:**

```python
def add_item(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket
```

---

## 2. Object-Oriented Programming (OOP)

### 2.1 Classes and Objects

**Definition:** A **class** is a blueprint for creating objects, bundling data (attributes) and behavior (methods). An **object** (or instance) is a concrete realization of a class.

```python
class Dog:
    species = "Canis familiaris"   # class attribute (shared by all instances)

    def __init__(self, name, age):
        self.name = name            # instance attribute
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Rex", 3)
print(my_dog.bark())      # "Rex says Woof!"
print(my_dog.species)      # "Canis familiaris"
```

`self` refers to the instance itself and must be the first parameter of instance methods (Python passes it implicitly when calling `my_dog.bark()`).

### 2.2 The Four Pillars of OOP

#### Encapsulation

**Definition:** Bundling data and methods together, restricting direct access to some components to protect object integrity.

Python doesn't enforce true private access; it uses **naming conventions**:

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance      # "protected" - convention only
        self.__pin = "1234"           # "private" - name-mangled

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    @property
    def balance(self):
        return self._balance
```

- Single underscore `_attr`: convention signaling "internal use, don't touch directly."
- Double underscore `__attr`: triggers **name mangling** (`_ClassName__attr`), mainly to avoid subclass attribute collisions, not true privacy.

```python
account = BankAccount(100)
print(account._BankAccount__pin)  # still accessible: "1234"
```

**Best Practice:** Use `@property` and `@x.setter` to expose controlled access to internal state (getters/setters, Pythonic style).

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * self._radius ** 2
```

#### Inheritance

**Definition:** A mechanism where a class (child/subclass) derives attributes and methods from another class (parent/superclass), enabling code reuse.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof"

animals = [Cat("Tom"), Dog("Rex")]
for a in animals:
    print(a.speak())
```

`super()` calls the parent class's method, useful in `__init__` to extend rather than replace behavior:

```python
class Puppy(Dog):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
```

Python supports **multiple inheritance**:

```python
class Flyer:
    def move(self):
        return "flying"

class Swimmer:
    def move(self):
        return "swimming"

class Duck(Flyer, Swimmer):
    pass

print(Duck().move())   # "flying" (MRO picks Flyer first)
```

**Method Resolution Order (MRO):** Determines the order classes are searched for a method, using the **C3 linearization algorithm**. Inspect with `ClassName.__mro__` or `ClassName.mro()`.

#### Polymorphism

**Definition:** The ability of different classes to be treated through the same interface, with each providing its own implementation ("many forms").

```python
def make_it_speak(animal):
    print(animal.speak())    # works for any object with a .speak() method

make_it_speak(Cat("Tom"))
make_it_speak(Dog("Rex"))
```

Python favors **duck typing**: "If it walks like a duck and quacks like a duck, it's a duck" — type compatibility is determined by the presence of methods/attributes, not explicit type declarations.

#### Abstraction

**Definition:** Hiding complex implementation details and exposing only the necessary interface. Achieved using **abstract base classes (ABCs)**.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

# Shape()  # TypeError: Can't instantiate abstract class
```

### 2.3 Special (Dunder) Methods

**Definition:** "Double underscore" methods that let custom objects integrate with Python's built-in syntax and protocols.

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):        # developer-facing representation
        return f"Vector({self.x}, {self.y})"

    def __str__(self):          # user-facing string
        return f"({self.x}, {self.y})"

    def __add__(self, other):    # enables v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):     # enables v1 == v2
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)     # (4, 6)
print(v1 == v2)     # False
```

Common dunders: `__init__`, `__repr__`, `__str__`, `__eq__`, `__lt__`, `__hash__`, `__len__`, `__getitem__`, `__setitem__`, `__iter__`, `__next__`, `__enter__`/`__exit__` (context managers), `__call__` (makes an instance callable).

**Best Practice:** If you override `__eq__`, also define `__hash__` if instances need to be hashable (defining `__eq__` sets `__hash__` to `None` by default).

### 2.4 Class Methods, Static Methods, and Instance Methods

```python
class Employee:
    company = "Acme Corp"

    def __init__(self, name):
        self.name = name

    def instance_method(self):
        return f"{self.name} works at {self.company}"      # accesses instance + class state

    @classmethod
    def from_string(cls, data_str):
        name = data_str.split(",")[0]
        return cls(name)                                     # alternative constructor pattern

    @staticmethod
    def is_valid_name(name):
        return isinstance(name, str) and len(name) > 0        # no access to self/cls; utility function
```

| Type | First Param | Access | Common Use |
|---|---|---|---|
| Instance method | `self` | instance + class | normal behavior |
| Class method | `cls` | class only | alternative constructors, factory methods |
| Static method | none | neither | utility/helper functions logically grouped in class |

### 2.5 Composition vs. Inheritance

**Composition:** Building complex objects by combining simpler ones ("has-a" relationship), often preferred over deep inheritance hierarchies for flexibility.

```python
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()    # Car "has-a" Engine

    def start(self):
        return self.engine.start()
```

**Best Practice:** "Favor composition over inheritance" — inheritance creates tight coupling; composition is more flexible and easier to test/modify.

### 2.6 Dataclasses

**Definition:** A decorator (`@dataclass`, Python 3.7+) that auto-generates `__init__`, `__repr__`, `__eq__`, and more for classes primarily used to store data.

```python
from dataclasses import dataclass, field

@dataclass
class Point:
    x: int
    y: int
    tags: list = field(default_factory=list)   # safe mutable default

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)   # True (auto-generated __eq__)
print(p1)          # Point(x=1, y=2, tags=[])
```

---

## 3. Decorators

### 3.1 Definition

A **decorator** is a callable that takes a function (or class) and returns a modified version, allowing behavior to be added transparently without changing the original code. Decorators rely on Python's treatment of **functions as first-class objects** (can be passed, returned, and assigned like any other value).

### 3.2 Basic Decorator

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Before the function call
# Hello, Alice!
# After the function call
```

`@my_decorator` above `greet` is syntactic sugar for `greet = my_decorator(greet)`.

### 3.3 Preserving Metadata with `functools.wraps`

Without `@wraps`, the wrapped function loses its original `__name__`, `__doc__`, etc.

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)              # preserves func.__name__, func.__doc__
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

**Best Practice:** Always use `functools.wraps` in decorators to keep introspection, debugging tools, and documentation generators working correctly.

### 3.4 Decorators with Arguments

A decorator factory takes arguments and returns an actual decorator.

```python
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hi():
    print("Hi!")

say_hi()   # prints "Hi!" three times
```

### 3.5 Class-Based Decorators

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call #{self.count}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")

say_hello()
say_hello()
```

### 3.6 Common Built-in Decorators

- `@staticmethod`, `@classmethod`, `@property` (see OOP section)
- `@functools.lru_cache(maxsize=None)` — memoizes function results for performance.
- `@functools.cached_property` — caches a computed property on first access.
- `@abstractmethod` — marks a method as required for subclasses (with ABC).
- `@functools.singledispatch` — enables function overloading based on argument type.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(50)   # fast, thanks to memoization
```

### 3.7 Stacking Decorators

Decorators apply bottom-up (closest to the function first):

```python
@decorator_a
@decorator_b
def func():
    pass
# equivalent to: func = decorator_a(decorator_b(func))
```

### 3.8 Real-World Use Cases

- Logging function calls and execution time
- Access control / authentication checks (e.g., in Flask/Django views)
- Input validation
- Caching / memoization
- Retry logic for flaky operations
- Rate limiting

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper
```

---

## 4. Generators

### 4.1 Definition

A **generator** is a special type of iterator defined using a function containing one or more `yield` statements, or a **generator expression**. Generators produce values **lazily**, one at a time, and maintain state between calls, without storing the entire sequence in memory.

### 4.2 Generator Functions

```python
def count_up_to(limit):
    n = 1
    while n <= limit:
        yield n
        n += 1

counter = count_up_to(5)
print(next(counter))   # 1
print(next(counter))   # 2
for val in counter:     # continues from where it left off: 3, 4, 5
    print(val)
```

When a generator function is called, it doesn't execute immediately — it returns a **generator object**. Code runs only when `next()` is called (explicitly or via a `for` loop), pausing at each `yield` and resuming from that point on the next call.

### 4.3 How `yield` Works

- `yield` pauses the function, saving all local state.
- On the next call to `next()`, execution resumes right after the `yield`.
- When the function ends (or hits `return`), a `StopIteration` exception is raised automatically, which `for` loops handle internally.

```python
def simple_gen():
    print("start")
    yield 1
    print("middle")
    yield 2
    print("end")

g = simple_gen()
next(g)   # prints "start", returns 1
next(g)   # prints "middle", returns 2
next(g)   # prints "end", raises StopIteration
```

### 4.4 Generator Expressions

Similar to list comprehensions, but with parentheses and lazy evaluation.

```python
squares = (x ** 2 for x in range(1_000_000))   # doesn't compute anything yet
print(next(squares))    # 0
print(sum(squares))     # computed lazily, one value at a time
```

### 4.5 Why Use Generators?

**Memory efficiency:** Generators don't build the whole sequence in memory — critical for large or infinite sequences.

```python
# Bad for large N: builds a full list in memory
def get_squares_list(n):
    return [x ** 2 for x in range(n)]

# Good: constant memory usage
def get_squares_gen(n):
    for x in range(n):
        yield x ** 2
```

**Infinite sequences:**

```python
def infinite_counter():
    n = 0
    while True:
        yield n
        n += 1

gen = infinite_counter()
for i in gen:
    if i > 5:
        break
    print(i)
```

### 4.6 `send()`, `throw()`, and Two-Way Communication

Generators can also receive values via `send()`, turning them into coroutine-like constructs.

```python
def echo():
    while True:
        received = yield
        print(f"Received: {received}")

gen = echo()
next(gen)          # prime the generator (advance to first yield)
gen.send("hello")   # prints "Received: hello"
```

### 4.7 `yield from`

Delegates to a sub-generator or iterable, simplifying generator chaining.

```python
def inner():
    yield 1
    yield 2

def outer():
    yield from inner()
    yield 3

print(list(outer()))   # [1, 2, 3]
```

### 4.8 Generators vs. Lists — Quick Comparison

| Aspect | List | Generator |
|---|---|---|
| Memory | Stores all elements | Stores only current state |
| Speed to create | Slower (builds full structure) | Instant (lazy) |
| Reusability | Can iterate multiple times | Single-use (exhausted after one pass) |
| Indexing | Supported (`lst[i]`) | Not supported |
| Use case | Small/medium data, need random access | Large/streaming data, pipelines |

**Best Practice:** Use generators for data pipelines, processing large files line-by-line, or streaming API responses, where you don't need the entire dataset in memory at once.

---

## 5. Exception Handling

### 5.1 Definition

**Exceptions** are events that disrupt the normal flow of a program's execution, typically representing errors (e.g., dividing by zero, accessing an invalid index, opening a missing file). Python uses a `try`/`except` model to catch and handle these gracefully instead of crashing.

### 5.2 Basic Syntax

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except (TypeError, ValueError) as e:
    print(f"Invalid input: {e}")
else:
    print("Runs only if no exception occurred")
finally:
    print("Always runs, exception or not (cleanup code)")
```

- `try`: code that might raise an exception.
- `except`: handles specific exception type(s).
- `else`: runs only if the `try` block completes without exceptions.
- `finally`: always runs — used for cleanup (closing files, releasing locks).

### 5.3 Exception Hierarchy

All exceptions inherit from `BaseException`. Most user code should catch subclasses of `Exception`, not `BaseException` (which also includes `SystemExit`, `KeyboardInterrupt`, `GeneratorExit`).

```
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 └── Exception
      ├── ArithmeticError
      │    └── ZeroDivisionError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── ValueError
      ├── TypeError
      ├── AttributeError
      ├── FileNotFoundError (subclass of OSError)
      ├── ImportError
      └── ...
```

**Best Practice:** Catch the **most specific exception** possible. Avoid bare `except:` (catches everything, including `KeyboardInterrupt`, and hides bugs).

```python
# Bad
try:
    risky()
except:
    pass

# Good
try:
    risky()
except ValueError as e:
    logger.error(f"Invalid value: {e}")
```

### 5.4 Raising Exceptions

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
```

**Re-raising** while preserving the original traceback:

```python
try:
    process()
except Exception as e:
    log_error(e)
    raise            # re-raises the same exception with original traceback
```

**Exception chaining** to show root cause:

```python
try:
    connect_to_db()
except ConnectionError as e:
    raise RuntimeError("Failed to initialize app") from e
```

### 5.5 Custom Exceptions

**Definition:** User-defined exception classes, typically subclassing `Exception`, used to represent domain-specific error conditions.

```python
class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the available balance."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw {amount}, balance is {balance}")

class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
```

**Best Practice:** Create custom exception hierarchies for libraries/applications so callers can catch broad or narrow categories as needed.

```python
class AppError(Exception):
    """Base class for all application-specific errors."""

class ValidationError(AppError):
    pass

class DatabaseError(AppError):
    pass
```

### 5.6 Context Managers for Resource Safety

`try`/`finally` is often replaced by the `with` statement (see File Handling) for guaranteed cleanup.

```python
class ManagedResource:
    def __enter__(self):
        print("Acquiring resource")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource")
        return False   # False = don't suppress exceptions

with ManagedResource() as res:
    print("Using resource")
```

### 5.7 Best Practices Summary

- Catch specific exceptions, not bare `except:`.
- Don't use exceptions for normal control flow (though Python's "Easier to Ask Forgiveness than Permission," EAFP, style does encourage some use — see Section 11).
- Always clean up resources with `finally` or context managers.
- Log exceptions with context (`logging.exception()` inside an `except` block captures the traceback).
- Keep `try` blocks small — wrap only the code that can actually raise the exception.
- Use custom exceptions for meaningful, domain-specific error signaling.

```python
import logging

try:
    do_something()
except ValueError:
    logging.exception("Failed to process input")   # logs full traceback
```

---

## 6. File Handling

### 6.1 Opening Files

```python
f = open("data.txt", "r")   # mode: read (text)
content = f.read()
f.close()                    # must close manually to release the file handle
```

**Best Practice:** Always use the `with` statement (context manager), which automatically closes the file even if an exception occurs.

```python
with open("data.txt", "r") as f:
    content = f.read()
# file is automatically closed here, even if an error occurred inside the block
```

### 6.2 File Modes

| Mode | Meaning |
|---|---|
| `"r"` | Read (default); error if file doesn't exist |
| `"w"` | Write; creates file or **truncates** existing content |
| `"a"` | Append; creates file if it doesn't exist, writes at the end |
| `"x"` | Exclusive creation; fails if file already exists |
| `"b"` | Binary mode (combine, e.g., `"rb"`, `"wb"`) |
| `"t"` | Text mode (default) |
| `"+"` | Read and write (e.g., `"r+"`) |

### 6.3 Reading Files

```python
with open("data.txt", "r") as f:
    all_text = f.read()          # entire file as one string
with open("data.txt", "r") as f:
    lines = f.readlines()         # list of lines (includes '\n')
with open("data.txt", "r") as f:
    for line in f:                # memory-efficient, reads line by line
        print(line.strip())
```

**Best Practice:** For large files, iterate line-by-line instead of `read()` or `readlines()`, which load the entire file into memory.

### 6.4 Writing Files

```python
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")
    f.writelines(["Line 1\n", "Line 2\n"])

with open("log.txt", "a") as f:      # append mode preserves existing content
    f.write("New log entry\n")
```

### 6.5 Working with Binary Data

```python
with open("image.png", "rb") as f:
    data = f.read()

with open("copy.png", "wb") as f:
    f.write(data)
```

### 6.6 Encoding

**Best Practice:** Always specify `encoding="utf-8"` explicitly for text files to avoid platform-dependent default encodings (e.g., `cp1252` on some Windows systems), which can cause `UnicodeDecodeError` in cross-platform code.

```python
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

### 6.7 File Paths with `pathlib`

**Best Practice:** Prefer the `pathlib` module (Python 3.4+) over string-based paths / `os.path` for more readable, cross-platform path handling.

```python
from pathlib import Path

p = Path("data") / "input.txt"
print(p.exists())
print(p.suffix)          # ".txt"
print(p.parent)           # "data"

for file in Path("logs").glob("*.txt"):
    print(file.name)

content = p.read_text(encoding="utf-8")   # shortcut, opens/reads/closes automatically
p.write_text("new content", encoding="utf-8")
```

### 6.8 CSV and JSON Files

```python
import csv
with open("data.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])

import json
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)          # parses JSON into a dict/list

with open("output.json", "w", encoding="utf-8") as f:
    json.dump({"key": "value"}, f, indent=2)
```

### 6.9 Common Errors

```python
try:
    with open("missing.txt") as f:
        data = f.read()
except FileNotFoundError:
    print("File does not exist")
except PermissionError:
    print("No permission to access the file")
except UnicodeDecodeError:
    print("File encoding mismatch")
```

### 6.10 Best Practices Summary

- Always use `with` for automatic resource cleanup.
- Specify encoding explicitly.
- Prefer `pathlib` for path manipulation.
- Iterate large files line-by-line rather than loading them fully.
- Use `csv` and `json` modules instead of manual string parsing.

---

## 7. Iterators and Iterables

### 7.1 Definitions

- **Iterable:** Any object capable of returning its members one at a time — implements `__iter__()`, which returns an iterator. Examples: `list`, `tuple`, `dict`, `str`, `set`, files.
- **Iterator:** An object that represents a stream of data; implements both `__iter__()` (returning itself) and `__next__()` (returning the next value, raising `StopIteration` when exhausted).

**Key relationship:** All iterators are iterables, but not all iterables are iterators. Calling `iter()` on an iterable produces an iterator.

```python
nums = [1, 2, 3]         # nums is an iterable
it = iter(nums)            # it is an iterator
print(next(it))             # 1
print(next(it))             # 2
print(next(it))             # 3
print(next(it))             # raises StopIteration
```

### 7.2 The Iterator Protocol

To be an iterator, an object must implement:

```python
class CountUp:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self          # an iterator returns itself from __iter__

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        self.current += 1
        return self.current

for num in CountUp(3):
    print(num)   # 1, 2, 3
```

A `for` loop is essentially syntactic sugar for:

```python
it = iter(iterable)
while True:
    try:
        item = next(it)
    except StopIteration:
        break
    # loop body
```

### 7.3 Custom Iterables (Separate from Iterators)

A cleaner pattern: make the container class iterable by returning a **new** iterator each time, so it can be iterated multiple times independently.

```python
class NumberCollection:
    def __init__(self, numbers):
        self.numbers = numbers

    def __iter__(self):
        return iter(self.numbers)     # delegates to the list's iterator

collection = NumberCollection([1, 2, 3])
for n in collection:      # first pass
    print(n)
for n in collection:      # second pass works fine -- new iterator each time
    print(n)
```

### 7.4 Generators as Iterators

Every generator is automatically an iterator (implements `__iter__` and `__next__` implicitly), making generators the easiest way to build custom iterators without boilerplate.

```python
def count_up(limit):
    current = 1
    while current <= limit:
        yield current
        current += 1
```

This is functionally equivalent to the `CountUp` class above, but far more concise.

### 7.5 Useful Iterator Tools (`itertools`)

```python
import itertools

itertools.count(10, 2)          # infinite: 10, 12, 14, ...
itertools.cycle([1, 2, 3])       # infinite: 1, 2, 3, 1, 2, 3, ...
itertools.repeat("A", 3)          # 'A', 'A', 'A'
itertools.chain([1, 2], [3, 4])    # 1, 2, 3, 4
itertools.islice(range(100), 5)     # first 5 items: 0..4
itertools.combinations([1,2,3], 2)   # (1,2), (1,3), (2,3)
itertools.permutations([1,2], 2)      # (1,2), (2,1)
itertools.groupby(sorted(data), key=fn)  # group consecutive items by key
```

### 7.6 Why Iterators Matter

- Enable **lazy evaluation** — process data one item at a time without loading everything into memory.
- Provide a uniform interface (`for x in obj`) across very different data structures.
- Foundation for generators, comprehensions, and many standard library functions (`map`, `filter`, `zip`).

**Interview Tip — Common Question:** "What's the difference between an iterable and an iterator?"
> An iterable is anything you can loop over (has `__iter__`); an iterator is the object actually doing the iteration, tracking state and producing values one at a time via `__next__`, and it becomes exhausted after a single full pass.

---

## 8. Lambda Functions

### 8.1 Definition

A **lambda function** is a small, anonymous, single-expression function defined using the `lambda` keyword. It's syntactic shorthand for a simple `def` function without a name.

```python
square = lambda x: x ** 2
print(square(5))   # 25

add = lambda x, y: x + y
print(add(2, 3))   # 5
```

Equivalent regular function:

```python
def square(x):
    return x ** 2
```

### 8.2 Syntax Rules

```python
lambda arguments: expression
```

- Can take any number of arguments (including `*args`, `**kwargs`, defaults).
- Can contain only a **single expression** — no statements (`if`/`else` must be a ternary expression, not a statement; no assignments, loops, or multiple lines).
- Implicitly returns the value of the expression.

```python
max_val = lambda a, b: a if a > b else b   # conditional expression allowed
```

### 8.3 Common Use Cases

**With `sorted()`, `min()`, `max()` as a `key` function:**

```python
people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
sorted_people = sorted(people, key=lambda p: p["age"])
```

**With `map()`, `filter()`:**

```python
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
```

**As short callbacks in GUI/event-driven code, or inline in `functools.reduce`:**

```python
from functools import reduce
product = reduce(lambda acc, x: acc * x, [1, 2, 3, 4])   # 24
```

### 8.4 When NOT to Use Lambdas

- If the logic requires more than one expression, or needs a docstring, use a regular `def` function — clearer and more maintainable.
- Avoid assigning a lambda to a name (PEP 8 discourages this):

```python
# Discouraged (PEP 8):
f = lambda x: x + 1

# Preferred:
def f(x):
    return x + 1
```

- Avoid deeply nested or overly complex lambdas — they hurt readability and can't be easily debugged (no meaningful `__name__`, hard to add breakpoints).

### 8.5 Lambdas and Closures

Lambdas can capture variables from an enclosing scope (closures), but this creates a classic **late-binding gotcha**:

```python
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])   # [2, 2, 2] -- NOT [0, 1, 2]!
```

All lambdas share the same `i`, which equals `2` (the last value) by the time they're called. **Fix** using a default argument to capture the value at creation time:

```python
funcs = [lambda i=i: i for i in range(3)]
print([f() for f in funcs])   # [0, 1, 2]
```

---

## 9. Comprehensions

### 9.1 Definition

**Comprehensions** provide a concise, readable syntax for creating lists, dicts, sets, or generators by applying an expression to each item in an iterable, optionally filtering with a condition.

### 9.2 List Comprehensions

```python
squares = [x ** 2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
pairs = [(x, y) for x in range(3) for y in range(3) if x != y]   # nested loops

# Equivalent traditional loop:
squares = []
for x in range(10):
    squares.append(x ** 2)
```

**With conditional expression (ternary) inside the mapping part:**

```python
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
```

### 9.3 Dict Comprehensions

```python
squares_dict = {x: x ** 2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

word_lengths = {word: len(word) for word in ["apple", "banana", "kiwi"]}

inverted = {v: k for k, v in {"a": 1, "b": 2}.items()}   # swap keys/values
```

### 9.4 Set Comprehensions

```python
unique_lengths = {len(word) for word in ["cat", "dog", "bird", "ox"]}
```

### 9.5 Generator Expressions

```python
gen = (x ** 2 for x in range(1000000))   # lazy, memory-efficient
total = sum(x ** 2 for x in range(10))    # parentheses optional as sole function arg
```

### 9.6 Nested Comprehensions

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

transposed = [[row[i] for row in matrix] for i in range(3)]
```

### 9.7 Comprehensions vs. `map()`/`filter()`

```python
# Comprehension (generally more Pythonic / readable)
result = [x * 2 for x in nums if x > 0]

# Equivalent with map/filter
result = list(map(lambda x: x * 2, filter(lambda x: x > 0, nums)))
```

**Best Practice:** Comprehensions are usually preferred in Python over `map()`/`filter()` with lambdas, for readability, especially when a filter condition is involved.

### 9.8 When to Avoid Comprehensions

- If the logic requires multiple statements, side effects, or exception handling — use a regular loop instead for clarity.
- Avoid excessive nesting (more than 2 levels) — split into a helper function or traditional loop.

```python
# Hard to read:
result = [y for x in data if x > 0 for y in transform(x) if y is not None]

# Clearer:
result = []
for x in data:
    if x > 0:
        for y in transform(x):
            if y is not None:
                result.append(y)
```

### 9.9 Performance Note

List comprehensions are typically **faster** than equivalent `for` loops with `.append()`, because the iteration is optimized at the C level in CPython.

---

## 10. Modules and Packages

### 10.1 Modules

**Definition:** A **module** is simply a single `.py` file containing Python definitions (functions, classes, variables) that can be imported and reused elsewhere.

```python
# mymath.py
def add(a, b):
    return a + b

PI = 3.14159
```

```python
# main.py
import mymath
print(mymath.add(2, 3))
print(mymath.PI)

from mymath import add, PI       # import specific names
from mymath import add as sum_two   # alias
import mymath as mm                # module alias
```

### 10.2 Packages

**Definition:** A **package** is a directory containing multiple modules and a special `__init__.py` file (which can be empty), turning the directory into an importable namespace. This allows organizing large codebases hierarchically.

```
my_package/
    __init__.py
    math_utils.py
    string_utils.py
    sub_package/
        __init__.py
        advanced.py
```

```python
from my_package import math_utils
from my_package.sub_package import advanced
```

**`__init__.py`** can also control what's exposed when someone does `from package import *`, via `__all__`:

```python
# my_package/__init__.py
from .math_utils import add, subtract
__all__ = ["add", "subtract"]
```

### 10.3 The Module Search Path

When you `import x`, Python searches, in order:
1. The directory of the currently running script.
2. Directories listed in `PYTHONPATH` (environment variable).
3. Standard library directories.
4. Site-packages (third-party installed packages).

Inspect the search path with `sys.path`.

### 10.4 `if __name__ == "__main__":`

Every module has a `__name__` attribute. When run directly, `__name__ == "__main__"`; when imported, `__name__` equals the module's name. This idiom lets a file act as both a reusable module and a standalone script.

```python
def main():
    print("Running as a script")

if __name__ == "__main__":
    main()
```

### 10.5 Absolute vs. Relative Imports

```python
# Absolute import (preferred, unambiguous)
from my_package.sub_package import advanced

# Relative import (within a package, relative to current module's location)
from . import math_utils           # same package
from .. import string_utils         # parent package
from .sub_package import advanced    # sibling sub-package
```

**Best Practice:** Prefer absolute imports for clarity, especially in larger projects (PEP 8 recommendation), though relative imports are fine within a self-contained package.

### 10.6 Virtual Environments and Dependency Management

**Definition:** A **virtual environment** is an isolated Python environment with its own installed packages, preventing dependency conflicts between projects.

```bash
python -m venv venv               # create
source venv/bin/activate            # activate (Linux/macOS)
venv\Scripts\activate                # activate (Windows)
pip install requests
pip freeze > requirements.txt        # snapshot dependencies
pip install -r requirements.txt       # reproduce environment
```

**Best Practice:** Always use a virtual environment (or tools like `poetry`, `pipenv`, or `uv`) per project rather than installing packages globally.

### 10.7 Standard Library Highlights

Commonly referenced in interviews:

- `os`, `sys` — OS interaction, interpreter internals
- `pathlib` — object-oriented filesystem paths
- `collections` — `defaultdict`, `Counter`, `namedtuple`, `deque`, `OrderedDict`
- `itertools` — efficient looping constructs
- `functools` — `reduce`, `lru_cache`, `partial`, `wraps`
- `datetime` — date/time handling
- `json`, `csv` — data serialization
- `re` — regular expressions
- `logging` — application logging
- `unittest`, `pytest` (third-party) — testing
- `typing` — type hints (`List`, `Dict`, `Optional`, `Union`, etc.)

### 10.8 Circular Imports

**Pitfall:** Module A imports Module B, and Module B imports Module A, causing an `ImportError` (partial initialization).

```python
# a.py
import b
def foo():
    return b.bar()

# b.py
import a          # circular!
def bar():
    return a.foo()
```

**Fixes:**
- Restructure code to remove the circular dependency (often a sign of poor separation of concerns).
- Move the import inside the function (deferred/local import).
- Merge the modules if they're tightly coupled.

---

## 11. Common Pitfalls

### 11.1 Mutable Default Arguments

Already covered in Section 1.4 — default argument values are evaluated **once**, at function definition time, and shared across all calls if mutable.

```python
def append_to(item, target=[]):   # BUG: shared list persists across calls
    target.append(item)
    return target
```

### 11.2 Late Binding Closures in Loops

```python
funcs = []
for i in range(3):
    funcs.append(lambda: i)
print([f() for f in funcs])   # [2, 2, 2], not [0, 1, 2]
```

**Fix:** Use a default argument (`lambda i=i: i`) or a factory function to capture the current value.

### 11.3 Modifying a List While Iterating

```python
nums = [1, 2, 3, 4, 5]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)     # BUG: skips elements because indices shift
print(nums)   # [1, 3, 5] -- looks right here but is unreliable in general
```

**Fix:** Iterate over a copy, or build a new list.

```python
nums = [n for n in nums if n % 2 != 0]
# or
for n in nums[:]:      # iterate a shallow copy
    if n % 2 == 0:
        nums.remove(n)
```

### 11.4 Shallow vs. Deep Copy

```python
import copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)      # or original[:] or list(original)
shallow[0].append(99)
print(original)   # [[1, 2, 99], [3, 4]] -- inner lists are shared!

deep = copy.deepcopy(original)
deep[0].append(100)
print(original)   # unaffected -- fully independent copy
```

**Rule of thumb:** `copy.copy()` duplicates only the outer container; nested mutable objects are still shared references. `copy.deepcopy()` recursively copies everything.

### 11.5 Comparing Floats with `==`

```python
print(0.1 + 0.2 == 0.3)   # False, due to floating-point representation
```

**Fix:** Use `math.isclose()`:

```python
import math
print(math.isclose(0.1 + 0.2, 0.3))   # True
```

### 11.6 Variable Scope and the `global`/`nonlocal` Keywords

```python
counter = 0
def increment():
    counter += 1     # UnboundLocalError: assignment makes counter local
```

**Fix:**

```python
def increment():
    global counter
    counter += 1
```

For nested functions, use `nonlocal` to modify a variable in an enclosing (but non-global) scope.

```python
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
    inner()
    return count
```

### 11.7 `is` vs `==`

- `==` compares **values** (calls `__eq__`).
- `is` compares **identity** (same object in memory, i.e., same `id()`).

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True (same value)
print(a is b)   # False (different objects)

x = 256
y = 256
print(x is y)   # True (CPython caches small ints -256 to 256)
x = 257
y = 257
print(x is y)   # False (or True depending on interpreter optimizations - unreliable!)
```

**Best Practice:** Never rely on `is` for value comparison of numbers/strings; only use it for `None`, `True`, `False`, or explicit singleton checks.

### 11.8 Integer Division Confusion

```python
print(5 / 2)     # 2.5  (true division, always returns float)
print(5 // 2)     # 2    (floor division)
print(-5 // 2)     # -3   (floors toward negative infinity, not toward zero!)
```

### 11.9 Exception Swallowing

```python
try:
    do_risky_thing()
except Exception:
    pass    # BAD: silently hides bugs, makes debugging very hard
```

**Best Practice:** At minimum, log the exception; never silently swallow errors in production code.

### 11.10 Misusing `except Exception` Too Broadly

Catching overly broad exceptions can mask real bugs (e.g., a `TypeError` from a typo gets treated the same as an expected `ValueError`). Prefer catching specific, expected exception types.

### 11.11 String Concatenation in Loops

```python
result = ""
for s in large_list_of_strings:
    result += s     # O(n^2) time complexity due to string immutability
```

**Fix:** `result = "".join(large_list_of_strings)`.

### 11.12 Not Using Context Managers for Resources

Forgetting to close files, sockets, or database connections leads to resource leaks. Always prefer `with` statements (Section 6.1, 5.6).

### 11.13 Confusing `*args` / `**kwargs` Ordering

Function signature order must be: standard positional args → `*args` → keyword-only args → `**kwargs`.

```python
def f(a, b, *args, c=10, **kwargs):
    pass
```

### 11.14 Class Attribute Mutability Trap

```python
class Student:
    grades = []     # class attribute - SHARED across all instances!

    def add_grade(self, grade):
        self.grades.append(grade)

s1 = Student()
s2 = Student()
s1.add_grade(90)
print(s2.grades)   # [90] -- unexpectedly shared!
```

**Fix:** Initialize mutable attributes in `__init__` so each instance gets its own.

```python
class Student:
    def __init__(self):
        self.grades = []
```

### 11.15 EAFP vs. LBYL

Python idiomatically favors **EAFP** ("Easier to Ask Forgiveness than Permission") over **LBYL** ("Look Before You Leap"), especially to avoid race conditions (e.g., file existing between check and use).

```python
# LBYL (less Pythonic, can race)
if key in my_dict:
    value = my_dict[key]
else:
    value = default

# EAFP (Pythonic, atomic)
try:
    value = my_dict[key]
except KeyError:
    value = default
```

### 11.16 Circular Imports

Covered in Section 10.8 — a frequent real-world pain point as codebases grow.

### 11.17 Off-by-One / Range Confusion

```python
range(5)         # 0, 1, 2, 3, 4  (stop is exclusive)
range(1, 5)        # 1, 2, 3, 4
list[0:5]          # slicing is also stop-exclusive
```

---

## 12. Quick Reference Cheat Sheet

### Data Type Complexity (Average Case, CPython)

| Operation | list | dict | set |
|---|---|---|---|
| Access by index/key | O(1) | O(1) | N/A |
| Search (`in`) | O(n) | O(1) | O(1) |
| Insert/Append | O(1)* | O(1) | O(1) |
| Delete | O(n) | O(1) | O(1) |

\* Amortized; occasional O(n) resize.

### OOP Cheat Sheet

| Concept | Keyword/Syntax |
|---|---|
| Define class | `class Foo:` |
| Inheritance | `class Bar(Foo):` |
| Call parent method | `super().method()` |
| Abstract method | `@abstractmethod` (with `ABC`) |
| Property getter/setter | `@property` / `@x.setter` |
| Class method | `@classmethod` |
| Static method | `@staticmethod` |
| Operator overload | `__add__`, `__eq__`, `__lt__`, etc. |

### Exception Handling Cheat Sheet

```python
try:
    ...
except SpecificError as e:
    ...
except (ErrorA, ErrorB):
    ...
else:
    ...          # no exception occurred
finally:
    ...          # always runs
```

### Key Interview Definitions (One-Liners)

- **Variable:** A name bound to an object in memory.
- **Mutable vs Immutable:** Whether an object's internal state can change after creation.
- **Class:** A blueprint for creating objects.
- **Inheritance:** Reusing behavior from a parent class.
- **Polymorphism:** Same interface, different implementations.
- **Encapsulation:** Bundling data and restricting direct access.
- **Decorator:** A function that wraps another function to extend its behavior.
- **Generator:** A function using `yield` to lazily produce a sequence of values.
- **Iterator:** An object implementing `__iter__` and `__next__`.
- **Iterable:** An object implementing `__iter__`, capable of being looped over.
- **Lambda:** An anonymous, single-expression function.
- **Comprehension:** Concise syntax for building lists/dicts/sets/generators from iterables.
- **Module:** A single `.py` file of reusable code.
- **Package:** A directory of modules with an `__init__.py`.
- **GIL (Global Interpreter Lock):** A CPython mutex ensuring only one thread executes Python bytecode at a time, limiting true parallelism for CPU-bound multithreading (use multiprocessing for CPU-bound parallel work).

### Common `dunder` Methods Quick Table

| Method | Purpose |
|---|---|
| `__init__` | Constructor / initializer |
| `__repr__` | Developer-friendly string representation |
| `__str__` | User-friendly string representation |
| `__eq__` | `==` comparison |
| `__lt__`, `__gt__` | `<`, `>` comparisons |
| `__hash__` | Enables use as dict key / set member |
| `__len__` | `len(obj)` |
| `__getitem__` | `obj[key]` indexing |
| `__iter__` | Makes object iterable |
| `__next__` | Advances an iterator |
| `__enter__` / `__exit__` | Context manager (`with` statement) |
| `__call__` | Makes an instance callable like a function |

---

*End of guide. Use this document as a fast-review reference before interviews, or as a source for retrieval-augmented question answering on core Python concepts.*
