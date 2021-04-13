#Leetspeak
##Given a paragraph of text as string, print the paragraph in leetspeak.

string = "I am a leet programmer"
#if you want there to be input text see line 6
#string = input("What would you like to say?>> ")

lstring = string.lower()
index = 0
while index < len(lstring):
    lstring = lstring.replace("a", "4")
    lstring = lstring.replace("e",'3')
    lstring = lstring.replace("g",'6')
    lstring = lstring.replace("i",'1')
    lstring = lstring.replace("o",'0')
    lstring = lstring.replace("s",'5')
    lstring = lstring.replace("t",'7')
    index += 1
print(lstring)
##part of me thinks I didn't need this in a loop
##But since it took forever and it finally worked, I'll leave it!
