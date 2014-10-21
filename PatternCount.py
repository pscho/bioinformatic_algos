# Bioinformatic Algorithms #
# PatternCount algorithm (naive?) #

def patternCount_main():
    # input
    filename = "dataset_2_6.txt" ## Change this ##

    handle = open(filename, "r")
    data = handle.read().splitlines()
    handle.close()
    
    matchCount = patternCount(data[0], data[1])

    # write results
    handle = open("PatternCount.txt", "w")
    handle.write("Input\n" +
                 data[0] + "\n" + 
                 data[1] + "\n" + 
                 "Output" + "\n" + 
                 str(matchCount) + "\n")
    handle.close()

def patternCount(text, pattern):
    count = 0

    for i in range(0, (len(text) - len(pattern)) + 1):
        word = getText(text, i, len(pattern))

        if pattern == word:
            count += 1

    return count

def getText(text, i , k):
    word = ""
    for j in range(i, i + k):
        word = word + text[j]
    return word
            
if __name__ == "__main__":
    patternCount_main()
