d = {
    "1": [".", ",", "?", "!", ":"],
    "2": ["A", "B", "C"],
    "3": ["D", "E", "F"],
    "4": ["G", "H", "I"],
    "5": ["J", "K", "L"],
    "6": ["M", "N", "O"],
    "7": ["P", "Q", "R", "S"],
    "8": ["T", "U", "V"],
    "9": ["W", "X", "Y", "Z"],
    "0": [" "]
}

string = input().upper()
keyboard = []

for ch in string:
    for k, v in d.items():
        if ch in v:
            index = v.index(ch)
            keyboard.append(k*(index+1))
message = "".join(keyboard)
print(message)   
