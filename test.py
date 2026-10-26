"""Ejemplo de *args combinado con un argumento keyword-only."""


def greet(*args, greeting="Hello"):
    """Saluda a cada nombre recibido en args usando el saludo indicado."""
    for name in args:
        print(f"{greeting}, {name}!")


greet("Alice", "Bob")                    # greeting uses default: "Hello"
greet("Alice", "Bob", greeting="Hi")     # greeting passed by keyword: "Hi"
greet("Alice", "Bob", "Hi")              # no error: "Hi" gets absorbed into args and prints "Hello, Hi!"
