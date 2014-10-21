# FrequentWord algorithm #

import PatternCount

def frequentWord_main():
    # input
    filename = "dataset_2_9.txt" ## Change this ##

    handle = open(filename, "r")
    data = handle.read().splitlines()
    handle.close()
    
    for item in frequentWord(data[0], int(data[1])):
        print item,

def frequentWord(text, k):
    freqPatterns = set()
    count = []
    for i in range(0, (len(text) - k) + 1):
        pattern = PatternCount.getText(text, i, k)
 
        count.append( PatternCount.patternCount(text, pattern) )

    maxCount = max(count)
    for i in range(0, (len(text) - k) + 1):
        if count[i] == maxCount:
            # set - there are no duplicates #
            freqPatterns.add( PatternCount.getText(text, i, k) )
            
    return freqPatterns

if __name__ == "__main__":
    frequentWord_main()
