for i in range(1,6):
        print("*"*i)
print("\n\n")
for i in range(1,6):
        print("*"*(6-i))

print("\n\n")

for i in range(1,6):
        print("{0:>5}".format("$"*i))
print("\n\n")

for i in range(6):
    print("{0:>5}".format("$"*(5-i)))

print("\n\n")
for i in range(1,6):
    print("{0:^9}".format("$"*(2*i-1)))
print("\n\n")
for i in range(1,6):
    print("{0:^9}".format("$"*(11-2*i)))
print("\n\n")
for i in range(1,10):
    if i <= 5:
        print("{0:^9}".format("$"*(2*i-1)))
    else:
        print("{0:^9}".format("$"*(19-2*i)))