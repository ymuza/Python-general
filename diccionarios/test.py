a = {
    "name": "cosmeee",
    "lastname": "fulanito",
    "age": "35"
}


b = {
    "name": "cosme",
    "lastname": "fulanito",
    "age": "36"
}

dict1 = {}
for k in a.keys():
    if a.get(k) != b.get(k):
        print(f"<{k}> has different values <{a.get(k)}> != <{b.get(k)}>")
        dict1.update({k: a.get(k)})

print(dict1)
