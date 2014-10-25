# utility functions for bioinformatics #

# Given a genome and integers k, L, t, return a list of all
# k-mers forming (L,t) clumps in the genome
def findClump(genome, k, L, t):
    #print "--- findClump: finding pattern counts in genome"
    clumps = {}
    for i in range(0, (len(genome) - k) + 1):
        word = getText(genome, i, k)
        if word not in clumps:
            #print "--- findClump: adding ", word, " to count dictionary"
            clumps[word] = patternMatch(genome, word)

    #print "--- findClump: calculating (L,t) clumps"
    kmers = []
    for pattern in clumps:
        patLocs = clumps[pattern]
        # Don't bother checking if pattern count is less than t
        if len(patLocs) < t:
            continue

        for i in range(0, len(patLocs) - t + 1):
            if patLocs[i + (t - 1)] - patLocs[i] <= L - k:
                kmers.append(pattern)
                break

    return kmers

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

# Return the locations of a given pattern in the given text
def patternMatch(text, pattern):
    locations = []
    for i in range(0, (len(text) - len(pattern)) + 1):
        word = getText(text, i, len(pattern))

        if pattern == word:
            locations.append(i)

    return locations

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

