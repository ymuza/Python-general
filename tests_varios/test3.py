
chars = ["a", "b", "a"]

repeated = set(chars)
seen_chars = set()
for i in chars:
    if i in seen_chars:
        repeated.add(i)
    else:
        seen_chars.add(i)


print(repeated)

    
    
    
