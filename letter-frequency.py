__author__ = "sharmazenith"

import os
import matplotlib.pyplot as plt 
import pandas as pd

def count_letters(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()

    freq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    
    for letter in message:
       encrypted_letter_index = alpha.find(letter)
       if encrypted_letter_index >= 0:
           freq[encrypted_letter_index] += 1

    
    output = ""
    for i in range(26):
        print (alpha[i], ":", freq[i])
        line = alpha[i] + "," + str(freq[i]) + "\n"
        output = output + line

    write_to_file(output)

    
def write_to_file(file_text):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    freqFile = open("frq.csv", 'w')
    freqFile.write(file_text)

    freqFile.close()

   
    csv_file = pd.read_csv("frq.csv", header = None)
    plt.title("Alphabet Frequency")
    plt.xlabel("Alphabet")
    plt.ylabel("Count")
    plt.bar(csv_file[0], csv_file[1], color = "#990000")
    
    plt.show()


def main():
    msg = input("Enter a message: ")
    count_letters(msg)

main()
