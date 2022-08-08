from deepdiff import DeepDiff

a = {
    "name": "yamil",
    "lastname": "muza",
    "age": "35"
}


b = {
    "name": "yamil",
    "lastname": "muza",
    "age": "36"
}

difference = DeepDiff(a, b, ignore_string_case=True)
print(difference)
