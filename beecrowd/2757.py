a = str(int(int(input())))
b = str(int(int(input())))
c = str(int(int(input())))
print(f"A = {a}, B = {b}, C = {c}")
print(f"A = {a.rjust(10)}, B = {b.rjust(10)}, C = {c.rjust(10)}")
print(f"A = {int(a):010}, B = {int(b):010}, C = {int(c):010}")
print(f"A = {a.ljust(10)}, B = {b.ljust(10)}, C = {c.ljust(10)}")