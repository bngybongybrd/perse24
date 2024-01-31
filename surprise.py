code = {
    '.-': 'A',   '-...': 'B',   '-.-.': 'C',   '-..': 'D',
    '.': 'E',    '..-.': 'F',   '--.': 'G',   '....': 'H',
    '..': 'I',   '.---': 'J',  '-.-': 'K',   '.-..': 'L',
    '--': 'M',   '-.': 'N',    '---': 'O',   '.--.': 'P',
    '--.-': 'Q', '.-.': 'R',   '...': 'S',   '-': 'T',
    '..-': 'U',  '...-': 'V',  '.--': 'W',   '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9'
}
ans = ""
crypt = ""

text = "YOu CAN SEE How / tHis caN WoRk OuT / nOW at A look / sEe THE usE Of Key / bELOW"
word_list = text.split(" / ")
for line in word_list:
    for char in line:
        if char.isupper():
            crypt += "-"
        elif char.islower():
            crypt += "."
        else:
            crypt += " "
    crypt += "|"

crypt = crypt.split("|")
crypt.pop()
for line in crypt:
    char = line.split(" ")
    for i in char:
        ans += code[i]
    ans += " "
print(ans)
