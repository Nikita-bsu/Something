def right_justify(s):
    return " " * (70 - len(s)) + s


stik = right_justify("monty")
print(stik)