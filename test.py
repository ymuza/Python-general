def greet(*args, greeting="Hello"):
    for name in args:
        print(f"{greeting}, {name}!")

greet("Alice", "Bob")                    # greeting uses default: "Hello"
greet("Alice", "Bob", greeting="Hi")     # greeting passed by keyword: "Hi"
greet("Alice", "Bob", "Hi")              # ❌ TypeError! "Hi" gets absorbed into args



