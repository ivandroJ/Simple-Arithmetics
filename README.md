# 🧮 Arithmetic CLI Program

A simple command-line Python program that performs **basic arithmetic operations**: addition, subtraction, multiplication, and division. The user is prompted to enter two numbers and select an operation.

## 🚀 Features

- Addition
- Subtraction
- Multiplication
- Division (with float support)
- Input validation for operation selection

## 🧑‍💻 Usage

### 1. Run the program

```bash
python main.py
```

### 2. Follow the prompts:

```
Welcome to the Arithmetic program!
Insert the first number: 10
Insert the second number: 5
Select the operation:
1 - Addition
2 - Subtraction
3 - Multiplication
4 - Division
Option: 3

Multiplication
Result: 50.0
```

## 📄 Code Structure

- `main()` — Entry point, collects user input.
- `execute(first, second)` — Prompts operation and calls the appropriate function.
- `addition(a, b)` — Returns the sum.
- `subtraction(a, b)` — Returns the difference.
- `multiplication(a, b)` — Returns the product.
- `division(a, b)` — Returns the quotient.

## ✅ Requirements

- Python 3.10 or newer (uses `match-case` syntax)

## 📌 Notes

- The program uses `float()` to allow decimal inputs.
- If the user selects an invalid operation, it prompts again recursively.
