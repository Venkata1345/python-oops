# Python OOP Practice: Employee Management System

This repository contains my study notes and practice code for Object-Oriented Programming (OOP) in Python. It simulates a basic HR system to demonstrate core OOP concepts.

## 🧠 Concepts Covered
* **Classes & Instances:** Creating blueprints (`Employee`) and concrete objects.
* **Methods:** Using Instance methods, Class methods (`@classmethod`), and Static methods (`@staticmethod`).
* **Inheritance:** Extending functionality with `Developer` and `Manager` subclasses.
* **Polymorphism:** Overriding parent methods (e.g., `apply_raise`).
* **Super:** Using `super().__init__` to maintain clean, DRY code.

## 📂 Code Structure

### The Base Class: `Employee`
* Sets up the basic attributes: `first`, `last`, `pay`.
* Includes a `apply_raise()` method to increase salary.

### The Subclasses
1.  **`Developer`**
    * Inherits from `Employee`.
    * Adds a `programming_language` attribute.
    * Overrides the `raise_amount` to give developers a 10% raise (vs. 4% standard).

2.  **`Manager`**
    * Inherits from `Employee`.
    * Manages a list of employees.
    * Includes methods to `add_emp`, `remove_emp`, and `print_emp` to list their team.

## 🚀 How to Run
1.  Clone the repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/python-oop-learning.git](https://github.com/YOUR_USERNAME/python-oop-learning.git)
    ```
2.  Run the script:
    ```bash
    python oop_practice.py
    ```

## 📝 Learning Goals
My goal is to master Python OOP principles to build scalable and maintainable software. Future updates will include Property Decorators (`@property`) and Magic Methods (`__repr__`, `__str__`).
