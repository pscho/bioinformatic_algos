
import BioUtil as bio

def findClump_main():
    # input
    filename = "E-coli.txt" ## Change this ##

    # Input method different for vibrio cholerae; commented out old section
    """
    with open(filename, "r") as handle:
        data = handle.read().split()
    """

    with open(filename, "r") as handle:
        data = handle.read()

    kmers = bio.findClump(data, 9, 500, 3)
    
    """
    for item in kmers:
        print item, 
    """

    print "Total:", len(kmers)

if __name__ == "__main__":
    findClump_main()
