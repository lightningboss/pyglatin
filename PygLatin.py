pyg = 'ay' # Define suffix
whatToDo = raw_input("Do you want to translate from PygLatin to English (1) or from English to PygLatin (2)?") # What should I do?!?
if whatToDo == "1":
    original_1 = raw_input('Enter your word:') # Get input
    if len(original_1) > 0 and original_1.isalpha():
        wordLower = original_1.lower() # To lowercase
        withoutAy = wordLower[:len(wordLower)-2] # Get word without -ay
        firstLetter = withoutAy[len(withoutAy)-1] # Get first letter
        final_word = firstLetter + withoutAy[:len(withoutAy)-1]# First letter + withoutAy - first leter
        final_word = final_word[0].upper() + final_word[1:] # First letter to upper
        print final_word
    else:
        print 'Error: empty (Error Code: 0x589dfff)'
elif whatToDo == "2":
    original_2 = raw_input('Enter your word:') # Get input
    if len(original_2) > 0 and original_2.isalpha():
        word = original_2.lower() # Original to Lower
        first = word[0]
        new_word = word+first+pyg # Define Base
        new_word = new_word[1:len(new_word)] # Get rid of one first letter
        new_word = new_word[0].upper() + new_word[1:] # First letter to upper
        print new_word
    else:
        print 'Error: empty (Error Code: 0x589dfff)'
else:
    print "You didn't type in 1 or 2!"
