import re
tmp = [input().lower() for i in range(int(input()))]
for i in tmp:
    if i.find("hello")+1 and not i[i.find("hello")+5].isalnum() :
        print("Hello! How can I help you?")
    elif i.find("hi")+1 and not i[i.find("hi")+2].isalnum() :
        print("Hello! How can I help you?")
    elif i.find("bye")+1 and not i[i.find("bye")+3].isalnum() :
        print("Goodbye! Have a nice day!")
    elif i.find("goodbye")+1 and not i[i.find("goodbye")+7].isalnum() :
        print("Goodbye! Have a nice day!") 
    elif i[-1]=='?' : print("That's an interesting question!")
    elif len(re.findall("[0-9]",i)) : print("I see some numbers there!")
    elif len(i)-i.count(' ')>19 : print("That's quite a long message!")
    else : print("I understand.")