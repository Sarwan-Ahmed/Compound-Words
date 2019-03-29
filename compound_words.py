#Finding compound words from gien string
#The time complexity of this algorithm is O(n^3)


f=open("text.txt")      #open file containing  string
s=f.read().lower()      #read file and convert all in lower case
words = s.split()       #seperate words by comma in words array
no_repeat = []
result=[]

#remove all repeated words from string
no_repeat.append(words[0])
for i in range(1,len(words)):
    if words[i] not in no_repeat:
        no_repeat.append(words[i])

#create file to store result or append file if it is already existing
f= open("output.txt","a+")

#loop through string and find compound words
#if found then write both (compound word and its sub words)
#in output file
for i in range(0, len(no_repeat)-1):
    for j in range(0, len(no_repeat)):
        compw=no_repeat[i]+no_repeat[j]
        if compw in no_repeat:
            f.write(compw + ": " + no_repeat[i]+ " "+ no_repeat[j]+ "\n")


#close file
f.close()
