# Understanding Routing - Flask Assignment

This project is a simple Flask server assignment that demonstrates routing and handling dynamic URL parameters in Python.

## Objectives
- Create a Flask server from scratch.
- Handle dynamic URL routing.
- Pass variables and integers in URLs.
- Implement error handling for invalid routes.

## Routes & Features

| Route | Expected Output / Action |
| :--- | :--- |
| `localhost:5000/` | Returns `"Hello World!"` |
| `localhost:5000/champion` | Returns `"Champion!"` |
| `localhost:5000/say/<name>` | Returns a greeting like `"Hi {name}!"` |
| `localhost:5000/repeat/<int:num>/<string:word>` | Repeats the given word a specified number of times *(Ninja Bonus)*. |
| Any other route | Returns `"Sorry! No response. Try again."` *(Sensei Bonus)*. |

## Prerequisites

Make sure you have **Python** and **Flask** installed on your system. You can install the required packages by running:

```bash
pip install Flask