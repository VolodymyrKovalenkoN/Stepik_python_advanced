letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
morse_dict = dict(zip(letters, morse))

text = (input().upper()).replace(" ", "")
symbols_list = []
for ch in text:
    for k in morse_dict:
        if ch in k:
            symbols_list.append(morse_dict[k])
print(" ".join(symbols_list))