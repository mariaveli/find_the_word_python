import random

count=1
words=['ΓΑΤΕΣ','ΜΗΧΑΝΕΣ','ΦΑΓΗΤΟ','ΠΙΤΣΑ','ΠΙΤΟΓΥΡΟ','ΔΟΥΛΕΙΑ','ΤΕΤΡΑΔΙΟ','ΚΟΥΖΙΝΑ','ΚΑΘΙΣΤΙΚΟ','ΜΟΛΥΒΙ']
wordToBe=random.choice(words) #string
findTheWord=list(wordToBe) #list
listLength=len(findTheWord)
givenLetters=[]
kremala=[]

def printKremala(kremala):
    print(kremala)

def isValid(letter):
    greekAlphabet=['Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω']
    if greekAlphabet.count(letter)==0:
        return False
    return True

def findLetterInWord(letter):
    positions=[pos for pos, char in enumerate(wordToBe) if char == letter]
    for position in positions:
        kremala[position]=letter
   
def lettersGiven(letter):
    givenLetters.append(letter)
    print(givenLetters)
        

for y in range (listLength):
    kremala.append('_')
    
printKremala(kremala)

success=False

while count<6 and not success:
    print('Έχετε ήδη δώσει τα παρακάτω γράμματα ')
    print(givenLetters)
    
    i=input('Δώσε ενα γράμμα σε κεφαλαία Ελληνικά: ')
    if not isValid(i):
        print('Λάθος εισαγωγή. Δώσε ένα γράμμα σε κεφαλαία Ελληνικά')
        continue
    if givenLetters.count(i)>0:
        print('Έχεις ήδη δώσει αυτό το γράμμα.')
        continue
    
    lettersGiven(i)
    if findTheWord.count(i)>0 and isValid(i):
        findLetterInWord(i)
        
        
    else:
        print('Συγνώμη. Προσπαθησε ξανά.')
        count+=1
        print('Σας απομένουν '+ str(6-count) + ' προσπάθειες.')
    printKremala(kremala)
    if kremala.count('_')==0:
        success=True
        
        
        
if success:
    print('Μπράβο κέρδισες!!!')
else:
    print('Δυστυχώς έχασες!!! Η λέξη ήταν ' + wordToBe)

