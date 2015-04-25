print "Welcome to PigLatin Translator 0.1!"
print ""
pyg = 'ay' # Define suffix
def getInput():
    return raw_input("Enter your word:") # Use it for everything

def firstUp(original, word):
    if original[0].isupper(): # Check whether first letter is uppercase
        return word[0].upper() + word[1:] # Makes The First Letter Upper ;)
    else:
        return word

def toEng():
    original = getInput()
    word = original[:len(original)-2].lower() # Get word without suffix + lowercase
    firstLetter = word[len(word)-1] # Get (the real) first letter
    word = firstLetter + word[:len(word)-1]# First letter + word - first letter - suffix
    piggy = firstUp(original, word) # First letter to upper?
    return piggy

def toPyg():
    original = getInput() # Original to Lower
    word = original+original[0].lower()+pyg # Define Base + first to lowercase
    word = word[1:len(word)] # Get rid of the first first letter
    piggy = firstUp(original, word) # First letter to upper?
    return piggy

whatToDo = raw_input("1 or 2?")
if whatToDo == "1":
        print toEng()
elif whatToDo == "2":
        print toPyg()
