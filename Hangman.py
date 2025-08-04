s0 = "------------------"
s1 = "=================="
s2 = "         |        "
s3 = "        🙂        "
s4 = "        /|\       "
s5 = "         |        "
s6 = "        / \       "

words = [
    "apple", "banana", "cherry", "grape", "orange", "kiwi", "mango",
    "peach", "pear", "plum", "papaya", "pineapple", "apricot", "blueberry",
    "blackberry", "coconut", "cranberry",  "guava", "lemon", "lime",
    "lychee", "pomegranate", "raspberry",
    "starfruit", "strawberry", "watermelon", "jackfruit", "dragonfruit",
    "grapefruit", "custardapple" 
]

import random
word = random.choice(words)
word = "banana"
s = ["_" for i in range(len(word))]
d = {}
l = [s1,s2,s3,s4,s5,s6]
for i in range(len(word)):
    if word[i] in d:
        d[word[i]].append(i)
    else:
        d[word[i]] = [i]

chance = 0
hang = ""
while chance<6:
    print("".join(s))
    inp = input("Your Guess: ")
    if inp in word:
        for i in d[inp]:
            s[i] = inp
        
        print("Hangman Status🔽")
        if hang:
            print(hang)
        else:
            print(s0)
    
        if "_" not in s:
            break
    
    else:
        hang += l[chance]+"\n"
        print("Hangman Status🔽")
        print(hang) 
        chance+=1
if "".join(s)==word:
    print("YOU WON🏆")
else:
    print("YOU LOST😥")
        


    
