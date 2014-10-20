# FrequentWord algorithm #

def main():
    # input
    filename = "dataset_2_9.txt" ## Change this ##

    handle = open(filename, "r")
    data = handle.read().splitlines()
    handle.close()
    
    print frequentWord(data[0], int(data[1]))

def frequentWord(text, k):
    freqPatterns = []
    for i in range(0, (len(text) - k) + 1):
        pass

    return ""

if __name__ == "__main__":
    main()
