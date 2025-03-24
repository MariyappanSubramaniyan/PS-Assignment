candidates = {
     "Alice": ["New York", "San Francisco", "Chicago"],
    "Bob": ["New York", "Chicago", "San Francisco"],
    "Charlie": ["New York", "San Francisco", "Chicago"]

}

Locations = { "New York": 1, "San Francisco": 1, "Chicago": 1}

assignment = {}

for candidate,pref in candidates.items():
    for city in pref:
        if Locations[city]>0:
            assignment[candidate] = city
            Locations[city]-=1
            break
print(assignment)