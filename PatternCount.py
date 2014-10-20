# Bioinformatic Algorithms #
# PatternCount algorithm (naive?) #

def main():
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
        # get word
        word = ""
        for j in range(i, i + len(pattern)):
            word = word + text[j]

        if pattern == word:
            count += 1

    return count
            
if __name__ == "__main__":
    main()
