from collections import Counter

deliveries = [
    {"courier": "DHL", "origin": "Berlin", "destination": "Munich"},
    {"courier": "DHL", "origin": "Berlin", "destination": "Munich"},
    {"courier": "DHL", "origin": "Berlin", "destination": "Hamburg"},
    {"courier": "UPS", "origin": "Paris", "destination": "Lyon"},
    {"courier": "UPS", "origin": "Paris", "destination": "Lyon"},
    {"courier": "UPS", "origin": "Paris", "destination": "Nice"},
    {"courier": "FedEx", "origin": "Rome", "destination": "Milan"},
    {"courier": "FedEx", "origin": "Rome", "destination": "Milan"},
    {"courier": "FedEx", "origin": "Rome", "destination": "Milan"},
    {"courier": "FedEx", "origin": "Naples", "destination": "Turin"},
]

# Step 1: Count (courier, origin, destination) tuples
counter = Counter((d["courier"], d["origin"], d["destination"]) for d in deliveries)

# Step 2: Organize into final structure
result = {}
for (courier, origin, destination), count in counter.items():
    result.setdefault(courier, {})[(origin, destination)] = count

print(result)
