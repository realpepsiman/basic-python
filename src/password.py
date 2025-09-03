import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False
checks = [0, 0, 0, 0, 0]
for chr in password:
    if chr.islower():
        checks[0] = 1
    if chr.isupper():
        checks[1] = 1
    if chr.isnumeric:
        checks[2] = 1
    if chr in "$#@":
        checks[3] = 1
if len(password) > 5 and len(password) < 17:
    checks[4] = 1

if 0 not in checks:
    is_valid = True
        

# Do all the requirement checks here.

print(is_valid)
