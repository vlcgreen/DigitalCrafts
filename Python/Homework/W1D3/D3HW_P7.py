#Caesar Cipher

decipher = "lbh zhfg hayrnea jung lbh unir yrnearq"

alpha = 'abcdefghijklmnopqrstuvwxyz'

alpha = list(alpha)

cipherbet = []
index = 0

while index < len(alpha):
    position = (index + 13) % 26
    cipherbet.append(alpha[position])
    index += 1 

print(cipherbet)

## Now that I have my working cypher I need to figure out how to replace each letter


