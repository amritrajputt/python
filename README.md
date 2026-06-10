# 🐍 Python Learning Journey

Welcome to the Python Learning Journey repository! This repository contains a structured set of files, exercises, and examples tracing through python fundamentals to advanced concepts like Object-Oriented Programming (OOP), decorators, and generators.

It is structured both as a daily progression (Days 1 to 5) and as dedicated deep-dives into core Python features.

---

## 📂 Repository Structure

Below is an overview of the directory structure and the topics covered in each section:

```
python/
├── day 1/                  # Python basics and imports
│   ├── hello.py            # Basic hello world and simple functions
│   └── first.py            # Importing functions from other files
│
├── day 2/                  # Control flow and data structures
│   ├── conditionals/       # Exercises on if-else conditions (Problems 1 to 7)
│   ├── lists.py            # Lists operations and methods
│   ├── tuple.py            # Tuples operations
│   └── dictionary.py       # Dictionaries and key-value mapping
│
├── day 3/                  # Iteration, loops and functions
│   ├── loops/              # Iterative statements and exercises
│   │   ├── function/       # Function basics, arguments, and return types
│   │   │   ├── circle.py             # Math utility function
│   │   │   ├── defaultparameter.py   # Functions with default params
│   │   │   ├── functionkwargs.py     # Understanding **kwargs
│   │   │   ├── functionwithastrick.py# Understanding *args
│   │   │   ├── lambdafunctions.py    # Anonymous functions
│   │   │   ├── recursivefun.py       # Recursive function examples
│   │   │   └── yield.py              # Introduction to generator yields
│   │   └── ...             # Loop exercises (prime check, factorial, backoff, etc.)
│
├── day 4/                  # Variable scopes and Intro to OOP
│   ├── scopes.py           # Local vs Global scopes, namespaces
│   └── oops/               # Basic Object Oriented Programming concepts
│
├── day 5/                  # Advanced Python decorators
│   └── decorators/         # Exercises on writing custom decorators
│
├── oops/                   # 🏛️ OOP Deep Dive
│   ├── access modifier/    # Public, protected, and private properties
│   ├── classandobject.py   # Class instantiation and examples (Bank, Book, Student)
│   ├── gettersetter.py     # Encapsulation using getters and setters
│   ├── propertydecorator.py# Using @property, getters, and setters decorators
│   ├── staticAttributes.py # Shared class attributes vs instance attributes
│   └── singlyLinkedList.py # Implementing a Linked List data structure in Python
│
├── decorators/             # 🛠️ Custom Decorators
│   ├── authorization.py    # Decorators check access/credentials
│   ├── dec.py              # Standard decorator syntax
│   └── loggingDecorators.py# Automated function call and execution logging
│
└── generators/             # ⚡ Advanced Generators
    ├── generators.py       # Basic custom iterators and yield expressions
    ├── infiniteGenerator.py# Creating endless stream generators
    ├── sendValuetoGenerators.py # Bidirectional communication with generators using .send()
    └── closeGenerator.py   # Closing generators manually using .close()
```

---

## 🚀 Key Topics Covered

### 1. ⚙️ Basics & Control Flow (Days 1 & 2)
- String manipulations, Lists, Tuples, and Dictionaries.
- Multi-conditional if-elif-else execution blocks.

### 2. 🔁 Loops & Functions (Day 3)
- Loop structures with termination check, exponential backoff algorithms, and duplicate detection.
- Positional, keyword (`*args`), and named keyword (`**kwargs`) parameters.
- Recursion basics and basic iterator pipelines.

### 3. 🏛️ Object-Oriented Programming (Day 4 & `oops/`)
- **Classes and Objects**: Model real-world systems like banking accounts and students.
- **Inheritance & Polymorphism**: Sharing logic across subclasses and method overriding.
- **Encapsulation**: Using access modifiers:
  - `_protected`: Single underscore convention.
  - `__private`: Double underscore for name mangling.
- **Static Methods**: Defining utility functions inside classes using `@staticmethod`.
- **Linked Lists**: Implementation of a basic singly linked list.

### 4. 🛠️ Decorators (`decorators/` & Day 5)
Decorators are functions that modify the behavior of another function without directly changing its code.
- **Timing Execution**: Custom decorators to measure run time.
- **Logging**: Dynamic function arguments and execution logs.
- **Authentication**: Simulating user access controls.

### 5. ⚡ Generators (`generators/`)
Generators produce values on the fly using `yield`, which optimizes memory utilization:
- Creating infinite sequences without high memory consumption.
- Sending values into generators dynamically using `generator.send(value)`.
- Cleaning up and exiting generators with `generator.close()`.

---

## 🛠️ How to Run

1. Make sure you have **Python 3.x** installed.
2. Clone or open the directory structure.
3. Open a terminal and run any file using:
   ```bash
   python python/<directory-path>/<file-name>.py
   ```
   For example, to run the singly linked list demo:
   ```bash
   python python/oops/singlyLinkedList.py
   ```
