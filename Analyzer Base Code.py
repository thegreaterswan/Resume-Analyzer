myfile = open("jobdescription.txt") #takes in job description
words = myfile.read() 
baselist = words.split() #splits up the text into individual pieces
wordlist = []
for word in baselist:
    wordlist.append(word.lower()) #lower cases everything for analysis 
    
useless = ["if", "and", "the", "for", "to", "a", "are", "by", "with", "of", "in", "their", "this", "from", "be", "-", "will", "an", "is", "as", "on", "that", "our", "we"]

wordfreq = [] #serts blank list
for word in wordlist:
    wordfreq.append(wordlist.count(word)) #adds a count to the list


wordfreq = [int(w) for w in wordfreq] #converts count into integers from string

pairs = list(zip(wordlist, wordfreq)) #this loads two separate lists into a single list 

at2 = []
at3 = []
at4 = []
above5 = []
above10 = []

for word, count in zip(wordlist, wordfreq):
    if (word in useless):
        None  

    elif count > 10:
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
