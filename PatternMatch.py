
import BioUtil as bio

def patternMatch_main():
    # input
    filename = "Vibrio_cholerae.txt" ## Change this ##

    # Input method different for vibrio cholerae; commented out old section
    '''
    handle = open(filename, "r")
    data = handle.read().splitlines()
    handle.close()
    
    matchLoc = BioUtil.patternMatch(data[1], data[0])
    '''

    with open(filename, "r") as handle:
        data = handle.read()

    matchLoc = bio.patternMatch(data, "CTTGATCAT") ## Change this ##

    for item in matchLoc:
        print item,

if __name__ == "__main__":
    patternMatch_main()
