# Hashsets
s = set()


# Add item into set - O(1)
s.add(1)
s.add(2)
s.add(3)


# Lookup if item is in the set O(1)
if 1 in s:
    print("1 is in the set")

# remove set -O(1)
s.remove(1)
print(s)

string='aaaaaaaaaaaaaaaavvvvvvvvvvvvvvvvvvvvcccccccccccccccdddddddddddddd'
sett=set(string) #set construction -O(s) s is the length of the string
print(sett)

#Loop over items in set -O(n)
for x in s:
    print(x)