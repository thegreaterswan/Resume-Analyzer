myfile = open("jobdescription.txt") #takes in job description
words = myfile.read() 
wordlist = words.split() #splits up the text into individual pieces


wordfreq = [] #serts blank list
for word in wordlist:
    wordfreq.append(wordlist.count(word)) #adds a count to the list

for w, z in zip(wordfreq, wordlist):####################FIX THIS IT ISNT HJOLDING THE CHANGE
    if w == 1:
        wordfreq.remove(w)
        wordlist.remove(z)

wordfreq = [int(w) for w in wordfreq] #converts count into integers from string

pairs = list(zip(wordlist, wordfreq)) #this loads two separate lists into a single list 

at2 = []
at3 = []
at4 = []
above5 = []
above10 = []

for word, count in zip(wordlist, wordfreq):
    if count > 10:
        above10.append([word, count])
        above10dic = dict(above10)
        
    elif count >= 5 and count < 10:
        above5.append([word, count])
        above5dic = dict(above5)

    elif count == 4:
        at4.append([word, count])
        at4dic = dict(at4)

    elif count == 3:
        at3.append([word, count])
        at3dic = dict(at3)

    elif count == 2:
        at2.append([word, count])
        at2dic = dict(at2)

    else: 
        None     
            
print(above10dic)
print(above5dic)
print(at4dic)
print(at3dic)
print(at2dic)
