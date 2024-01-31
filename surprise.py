code = {
    'A': '.-',     'B': '-...',   'C': '-.-.',  'D': '-..',
    'E': '.',      'F': '..-.',   'G': '--.',   'H': '....',
    'I': '..',     'J': '.---',   'K': '-.-',   'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',   'P': '.--.',
    'Q': '--.-',   'R': '.-.',    'S': '...',   'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',   'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',
    '4': '....-',  '5': '.....',  '6': '-....',  '7': '--...',
    '8': '---..',  '9': '----.'
}
text = "YOu CAN SEE How / tHis caN WoRk OuT / nOW at A look / sEe THE usE Of Key / bELOW"
decode = ""
caps = ""
word_list = text.split(" / ")

for line in word_list:
    for char in line:
        if char.isupper():
            caps += char
    caps += "\n"

print(caps)

for line in word_list:
    for char in line:
        if char in code:
            decode += code[char]
    decode += " "
print(decode)
