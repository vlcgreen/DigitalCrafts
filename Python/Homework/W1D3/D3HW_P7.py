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

# need program to check index/pos for cypher letter with cypherbet,
# then whatever that index number is use it to pull same index from alpha
# replace the decipher text letter with whatever is in alpha[index]
