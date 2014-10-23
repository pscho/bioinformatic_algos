# Reverse a sequence #

def reversed_main():
    handle = open("dataset_3_2.txt", "r") # change this #
    data = handle.read().splitlines()
    handle.close()
    
    handle = open("output.txt", "w")
    for item in reverseComplement(data[0]):
        handle.write(item)
    handle.close()

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

if __name__ == "__main__":
    reversed_main()
