
import BioUtil as bio

def findClump_main():
    # input
    filename = "dataset_4_4.txt" ## Change this ##

    with open(filename, "r") as handle:
        data = handle.read().split()

    kmers = bio.findClump(data[0], int(data[1]), int(data[2]), int(data[3]))
    for item in kmers:
        print item, 

if __name__ == "__main__":
    findClump_main()
