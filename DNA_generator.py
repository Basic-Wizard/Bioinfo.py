#!/usr/bin/env python
import random
import argparse


def get_args():
    parser = argparse.ArgumentParser(description="This script will generate a large test file for the plesa project")
    parser.add_argument("-t", help="unit test file", type=str, required = True)
    parser.add_argument("-a", help="answer key file", type=str, required = True)
    return parser.parse_args()

parameters = get_args()
t = parameters.t
a = parameters.a

lib_index = "AAAAAAAAA"
cr1 = "TTTTTTTTTTTTTTTTT"
cr2 = "CCCCCCCCCCCCCCCC"
cr3 = "GGGGGGGGGGGGGGGG"

def generate_sequence(length, alphabet=['A', 'C', 'G', 'T']):
    sequence = []
    for i in range(length):
        sequence.append(random.choice(alphabet))
    return ''.join(sequence)

def generate_duplicate_sequences(original, num_duplicates, error_rate, insertion_prob=0.2):
    duplicates = []
    for i in range(num_duplicates):
        duplicate = []
        for j in range(len(original)):
            if random.random() < error_rate:
                a = random.random()
                if a < .5:
                    duplicate.append(random.choice(['A', 'C', 'G', 'T']))
                if a > .75:
                    duplicate.append(original[j])
                    duplicate.append(random.choice(['A', 'C', 'G', 'T']))
                else:
                    continue
            else:
                duplicate.append(original[j])
        duplicates.append(''.join(duplicate))
    return duplicates


seqs_list = []
unit_test = []

with open(t, "w") as tout, open(a , "w") as aout:
    for numbers in range(5):
        x = int(random.normalvariate(700,75))
        seq = (generate_sequence(x))
        
        barcode = (generate_sequence(20))
        y = int(random.normalvariate(7,2))
        seqs_list.append((barcode,seq,y))
        print (barcode, "\t", y, "\t", seq, file = aout)
    for gene in seqs_list:
        read = (lib_index + cr1 + gene[1] + cr2 + gene[0] + cr3 + lib_index)
        x = generate_duplicate_sequences(read,gene[2],.05)
        #print (gene[2], type (x[1]))
        #print (read)
        for n,barcodes in enumerate(x):
                print ("@seqid_", n, sep="", file = tout)
                print (barcodes, file = tout)
                print ("+", file = tout)
                q = []
                for base in range(len(barcodes)):
                    score = int(random.normalvariate(63,2))
                    q.append(chr(score))
                print("".join(q), file = tout)


