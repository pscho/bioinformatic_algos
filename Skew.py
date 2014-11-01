
import BioUtil as bio

def skew_main():
    filename = "test_data.txt" ## Change this

    with open("test_data.txt", "r") as handle:
        data = handle.read()

    skew = bio.skewCG(data)
    for item in skew:
        print item,

if __name__ == "__main__":
    skew_main()
