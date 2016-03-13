print "Welcome to PigLatin Translator 0.1!"
print ""
suffix = 'ay' # Define suffix
def getInput():
    return raw_input("Enter your word:") # Use it for everything

def firstUp(original, word):
    if original[0].isupper(): # Check whether first letter is uppercase
        return word[0].upper() + word[1:] # Makes The First Letter Upper ;)
    else:
        return word
def isItAWord(word):
    if len(word) > 0 and word.isalpha(): # Check for common mistakes in writing
        return word
    else:
        return "Error: No Word! (Error Code: 0x589dfff)"
def toEng():
    original = getInput()
    if not (original[len(original)-2:len(original)] == "ay"):
        print "It seems like you've entered English, not Pyglatin! No problem, here's your word:"
    word = original[:len(original)-2].lower() # Get word without suffix + lowercase
    firstLetter = word[len(word)-1] # Get (the real) first letter
    word = firstLetter + word[:len(word)-1]# First letter + word - first letter - suffix
    piggy = firstUp(original, word) # First letter to upper?
    return isItAWord(piggy)

def toPyg():
    original = getInput()
    if (original[len(original)-2:len(original)] == "ay"):
        print "It seems like you've entered Pyglatin, not English! No problem, here's your word:"
    word = original+original[0].lower()+suffix # Define Base + first to lowercase
    word = word[1:len(word)] # Get rid of the first first letter
    piggy = firstUp(original, word) # First letter to upper?
    return isItAWord(piggy)

whatToDo = raw_input("Do you want to translate from English to PygLatin (1) or from PygLatin to English (2)?") # What should I do?!?
if whatToDo == "1":
        print toPyg()
elif whatToDo == "2":
        print toEng()
else:
    print "Error: There is no other choice! (Error Code: 0x132dfaa)"
