# Turquoise

## Features

- Infix notation for a variety of [[mathematical operators](https://en.wikipedia.org/wiki/mathematical_operators)](https://en.wikipedia.org/wiki/mathematical_operators)
- Shorthand functions for common operations and expressions
- Seamless integration of calculations involving numbers, symbols, strings, booleans, lists, and more

Several tools for debugging and development are also under development or planned:

- [[Transpiling](https://en.wikipedia.org/wiki/Transpiling)](https://en.wikipedia.org/wiki/Transpiling) to clean [[Python](https://en.wikipedia.org/wiki/Python)](https://en.wikipedia.org/wiki/Python) code
- Interactive visualization of the [[abstract syntax tree](https://en.wikipedia.org/wiki/abstract_syntax_tree)](https://en.wikipedia.org/wiki/abstract_syntax_tree) for use in debugging
- A linter to standardize code written in Turquoise
- A profiler to analyze the performance of Turquoise programs
- Time-complexity and space-complexity analysis of algorithms
- An interactive debugger

## Design Philosophy

### Brevity
Turquoise draws on the [object-oriented](https://en.wikipedia.org/wiki/object-oriented) principles of languages like Python and [JavaScript](https://en.wikipedia.org/wiki/JavaScript), but emphasizes concision to accelerate the development workflow.

### Flexibility
Turquoise's data structures and operators are structured to be infinitely reconfigurable to the needs of your task.

### Efficiency
A core part of Turquoise's design philosophy revolves around making the planning -> development -> feedback loop as seamless and pain-free as possible. The language is dynamic and meant to be interacted with as a key part of the development process.

### Interoperability
This is currently a (very) new and feature-limited programming language, so it is intended to work cohesively with other technologies, libraries, and modules while maintaining a reasonable dependency scope for the language's core features. Eventually, Turquoise will be able to run arbitrary Python code on representations of its data structures and likewise, snippets of Turquoise code will be able to be executed with a Python library. Transpiling (transcompiling) is also being explored as a way to bridge the gap between Turquoise's methodology and Python's massive ecosystem of modules and libraries.

### Intuitiveness
Everything in the language should, to a reasonable extent, do what you expect it to. When confusion arises, efficient strategies for clarifying the language's behavior will be available.

### Consistency
Exceptions to rules and principles should be minimized wherever possible in order to make the language's basic concepts universally applicable.

*This document was generated from [`turquoise.ipynb`](https://nbviewer.jupyter.org/github/generic-github-user/turquoise/blob/master/turquoise.ipynb) at 2021-06-04 13:13:31*