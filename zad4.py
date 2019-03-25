bin = "11001100"
dec = 0

for i, x  in enumerate(reversed(bin)):
    if x == "1":
        dec += (2**i)
print(dec)