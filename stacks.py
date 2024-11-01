# stacks- Last In First Out(LIFO)
stk = []


# Append to top of stack -o(1)
stk.append(1)
stk.append(5)
stk.append(8)

# pop from stack -O(1)
x = stk.pop()

# Ask whats on the top of stack-o(1)
print(stk[-1])

# Ask if something is in the stack-o(1)
if stk:
    print(True)


print(stk)
