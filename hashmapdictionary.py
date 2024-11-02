# Hashmap Dictonaries
from collections import defaultdict
d = {'greg': 1, 'steve': 2, 'rob': 3}
print(d)

# Add key :val in dictionary - O(1)
d['john'] = 4

# Lookup:o(1)
if 'greg' in d:
    print(f'this is inside g ${d["greg"]}')


# loop ove the key:val pairs of the dictionary:O(n)
for key, value in d.items():
    print(f'key: {key} value: {value}')

# Defaultdict
default = defaultdict(list)
default[7]

#counter
from collections import Counter

string = 'aaaaaaaaaaaaaaaavvvvvvvvvvvvvvvvvvvcccccccccccccccdddddddddddddd'
counter=Counter(string)

print(d)
print(f'default:{default}')
print(f'counter:{counter}')
