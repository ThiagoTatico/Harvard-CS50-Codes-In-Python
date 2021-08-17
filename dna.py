# Identify who a DNA sequence belongs to

# Libraries-----------------------------------------------
import csv
import sys
# ------------------------Libraries-----------------------


def main():
    
    # Checks for command line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # Open the file and read
    with open(sys.argv[2]) as sequeF:
        sequence = sequeF.read()

    # Open the file and read
    with open(sys.argv[1]) as dataB:
        readerD = csv.DictReader(dataB)
        STRs = readerD.fieldnames[1:]
        
        # Stores the quantities of each STR for comparison with the DNAS Data Base
        dna_test = {}
        for str in STRs:
            dna_test[str] = str_counter(sequence, str)
        
        # Check the compatibility of the dna_test with the base date
        for row in readerD:
            
            if dna_locator(STRs, dna_test, row):
                print(f"{row['name']}")
                return
            
        print("No match")

# FUNCTIONS-------------------------------------------------------------------


def str_counter(sequence, str):
    """count how many STR repetitions exist in sequence (for each type of STR)"""
    count = 0
    while str*(count + 1) in sequence:
        count += 1
    return count
# ---------------------------------FUNCTIONS----------------------------------


def dna_locator(STRs, dna_test, row):
    """compatible dna locator"""
    for str in STRs:
        if dna_test[str] != int(row[str]):
            return False
    
    return True
# ---------------------------------FUNCTIONS----------------------------------


# END-LINE
if __name__ == "__main__":
    main()