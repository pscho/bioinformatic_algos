# utility functions for bioinformatics #

# Retrieve a text of length k starting at index i from the given text 
def getText(text, i , k):
    word = ""
    for j in range(i, i + k):
        word = word + text[j]
    return word

# Count the number of times a given pattern appears in the given text
def patternCount(text, pattern):
    count = 0

    for i in range(0, (len(text) - len(pattern)) + 1):
        word = getText(text, i, len(pattern))

        if pattern == word:
            count += 1

    return count

# Return the reversed complement of a given sequence
def reverseComplement(text):
    reverse = [0] * len(text)
    complement = ""
    for i in range(0, len(text)):
        # Get complement
        if text[i] == 'A':
            complement = 'T'
        elif text[i] == 'T':
            complement = 'A'
        elif text[i] == 'C':
            complement = 'G'
        elif text[i] == 'G':
            complement = 'C'
        else:
            print "ERROR - Illegal character in sequence:", text[i]
            raise SystemExit

        # Add to reversed list 
        reverse[len(text) - (i + 1)] = complement
    
    return reverse
