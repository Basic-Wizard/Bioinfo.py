# Author: Keenan Raleigh Keenan.Raleigh@gmail.com

# Check out some Python module resources:
#   - https://docs.python.org/3/tutorial/modules.html
#   - https://python101.pythonlibrary.org/chapter36_creating_modules_and_packages.html
#   - and many more: https://www.google.com/search?q=how+to+write+a+python+module

'''This module is a collection of the useful functions and variables that I created throughout the 
BGMP program at the University of Oregon. This includes ...'''

__version__ = "0.2"         # Read way more about versioning here:
                            # https://en.wikipedia.org/wiki/Software_versioning

DNA_bases = "AGAGAGGGAGATTTCTCTTCCGACACGCAAGACATCAGCGCGTTCGagcat"
RNA_bases = "CUUACGUCAGGCAGUCGAUCGAUGCAGUCGAUGAUCAUCGUCGUAGCGAUG"

def convert_phred(letter):
    '''this function will return a numeric quality score that coralates to the inputed phred score'''
    score_n = int(ord(letter)-33)
    return score_n


def qual_score(phred_score: str) -> float:
    """gets an average quality score"""
    index = 0
    b=0
    while index < len (phred_score):
        score_n = convert_phred (str(phred_score)[index])
        index+=1
        b=b+ (score_n)
        c = b/ len(phred_score)
    return c


def validate_DNA_seq(seq): 
    '''determines if a sequence is DNA, RNA or other'''
    seq = seq.upper()
    if len (seq) == seq.count("T") + seq.count("A") + seq.count("C") + seq.count("G") + seq.count("N"):
        print ("sequence is likely DNA")
        return (True)
    elif len (seq) == seq.count("U") + seq.count("A") + seq.count("C") + seq.count("G") + seq.count("N"):
        print ("sequence is likely RNA")
        return (False)
    else:
        print("This is likely not an oligonucleotide")
        return (False)
    pass 

def gc_content(seq):
    '''Measures CG content of DNA sequence'''
    if validate_DNA_seq(seq) == True:
        seq = seq.upper()
        gc_content = ((seq.count("G") + seq.count("C")) / len(seq))
        print (gc_content)
        return gc_content
    else:
        print ("sequence is not DNA, may be RNA")


def oneline_fasta(f,o):
    '''docstring'''
    with open (o, "w") as fo:
        with open(f,"r") as fh:   #opens the file as fh
            for n,line in enumerate(fh):     #starts a for loop for each line in file f 
                line = line.strip('\n')
                if n == 0:
                    print (line, file = fo)
                elif n!=0 and line[0] == ">":
                    print (file = fo)
                    print (line, file = fo)
                else:
                    #seq
                    print (line, end = "", file = fo)

if __name__ == "__main__":
    # write tests for functions above
    #convert_phred unit tests
    assert convert_phred("I") == 40, "wrong phred score for 'I'"
    assert convert_phred("C") == 34, "wrong phred score for 'C'"
    assert convert_phred("2") == 17, "wrong phred score for '2'"
    assert convert_phred("@") == 31, "wrong phred score for '@'"
    assert convert_phred("$") == 3, "wrong phred score for '$'"
    print("Your convert_phred function is working! Nice job")

    #___________________________________________________________________________________________________________________________________________
    #Qual_score Unit tests

    seq_name: str = "@GAAATG_1_1101_4446_2137_1"
    seq: str = "TGCAGGTTGAGTTCTCGCTGTCCCGCCCCCATCTCTTCTCTTCCAGTCTGGCTCTGGAGCAGTTGAGCCCAGCTCAGGTCCGCCGGAGGAGACCG"
    phred_score: str = "FFHHHHHJJJJIJIJJJIJJJJJJIIIJJJEHJJJJJJJIJIDGEHIJJFIGGGHFGHGFFF@EEDE@C??DDDDDDD@CDDDDBBDDDBDBDD@"

    old_convert_phred = convert_phred
    del convert_phred

    try:
        qual_score(phred_score)
    except NameError:
        pass
    else:
        raise AssertionError("qual_score does not call convert_phred - make sure you're not duplicating previous effort!")
    finally:
        convert_phred = old_convert_phred
        del old_convert_phred
        
    print("you used the function you wrote, excellent!")

    assert qual_score(phred_score) == 37.62105263157895, "wrong average phred score"
    print("You calcluated the correct average phred score")

    #____________________________________________________________________________________________________________________________________________________________________
    #validate_DNA_seq Unit tests

    assert validate_DNA_seq("AATAGAT") == True, "DNA string not recognized"
    print("Correctly identified a DNA string")
    assert validate_DNA_seq("AAUAGAU") == False, "DNA string not recognized"
    print("Correctly identified a RNA string")
    assert validate_DNA_seq("Hi there!") == False, "Non-DNA identified as DNA"
    print("non-DNA sequence")

    #_____________________________________________________________________________________________________________________________________________________________________
    #gc_content Unit tests
    assert gc_content("GCGCGC") == 1
    assert gc_content("AATTATA") == 0
    assert gc_content("GCATGCAT") == 0.5
    print("correctly calculated GC content")