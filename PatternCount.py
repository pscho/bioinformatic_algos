# Bioinformatic Algorithms #

def readToList(filename):
    with open(filename, "r") as handle:
        retVal = handle.read().splitlines()

    return retVal

def patternCount():
    
    filename = "test.txt" ## Change this ##

    text = readToList(filename)

    print text


if __name__ == "__main__":
    patternCount()
