import sys

# This program should take two arguments, a command--either "encode" or "decode"--
# and then a string.

if len(sys.argv) != 3:
    print("Incorrect number of arguments.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} command string\n", file=sys.stderr)
    sys.exit(1)

command, x = sys.argv[1:3]

match command:
    case "encode":
        # Implement the encoding here
        y = []
        for a in x:
            y.append(hex(ord(a)))
        
        encoding = "".join(y)
        print(encoding)

    case "decode":
        # Implement the decoding here
        x = x.split("0x")
        x.pop(0)
        for i in range(len(x)):
            x[i] = chr(int(x[i], base = 16))
        decoding = "".join(x)
        print(decoding)
