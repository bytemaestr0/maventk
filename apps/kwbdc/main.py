#!/usr/bin/env python3

import itertools, os, time 

filenames = []
file_counter = 1
directory = "apps/kwbdc/dictionaries"

def leet_conversion(word):
    leet_combo = {'a': '4', 'b': '8', 'e': '3', 'g': '6', 'l': '1', 'o': '0', 's': '5', 't': '7'}
    return ''.join(leet_combo.get(char.lower(), char) for char in word)

def merge_dictionaries(filelist):
    for i in itertools.count(start=1):
        if os.path.exists(f"{directory}/pass_dictionary{i}"):
            pass
        else:
            final_file = f"{directory}/pass_dictionary{i}"
            break
    with open(final_file, "w") as output_file:
        for filename_or_path in filelist:
            with open(filename_or_path) as input_file:
                output_file.write(input_file.read())
    return final_file
def main(word):
    variations = set()
    word_lower = word.lower()
    word_capitalize = word.capitalize()
    word_upper = word.upper()
    leet_word = leet_conversion(word)
    leet_capitalize = leet_conversion(word_capitalize)
    leet_upper = leet_conversion(word_upper)
    
    variations.update([
        word_lower, word_capitalize, word_upper,
        leet_word, leet_capitalize, leet_upper
    ])

    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*']
    
    for num in numbers:
        variations.update([
            word_lower + num, word_capitalize + num, word_upper + num,
            leet_word + num, leet_capitalize + num, leet_upper + num
        ])
        
        for char in special_chars:
            variations.update([
                word_lower + num + char, word_capitalize + num + char, word_upper + num + char,
                leet_word + num + char, leet_capitalize + num + char, leet_upper + num + char
            ])
    
    for length in range(2, 4): 
        for combo in itertools.product(numbers + special_chars, repeat=length):
            combo_str = ''.join(combo)
            variations.update([
                word_lower + combo_str, word_capitalize + combo_str, word_upper + combo_str,
                leet_word + combo_str, leet_capitalize + combo_str, leet_upper + combo_str
            ])
    
    for year in range(1900, 2101):
        year_str = str(year)
        variations.update([
            word_lower + year_str, word_capitalize + year_str, word_upper + year_str,
            leet_word + year_str, leet_capitalize + year_str, leet_upper + year_str
        ])
        
        for char in special_chars:
            variations.update([
                word_lower + year_str + char, word_capitalize + year_str + char, word_upper + year_str + char,
                leet_word + year_str + char, leet_capitalize + year_str + char, leet_upper + year_str + char
            ])
            
            for char2 in special_chars:
                variations.update([
                    word_lower + year_str + char + char2, word_capitalize + year_str + char + char2, word_upper + year_str + char + char2,
                    leet_word + year_str + char + char2, leet_capitalize + year_str + char + char2, leet_upper + year_str + char + char2
                ])
    
    return variations

num_of_words = int(input("How many different words: "))

if num_of_words >= 2:
    need_merge = True
else:
    need_merge = False

list_of_words = []

for i in range(0, num_of_words):
    word_to_append = input(f"Word{i+1}: ").strip()
    list_of_words.append(word_to_append)

for word in list_of_words:
    variations = main(word)
    while True:
        for i in itertools.count(start=1):
            if os.path.exists(f"{directory}/pass{i}"):
                file_counter += 1
            else:
                outfile = f"{directory}/pass{i}"
                filenames.append(outfile)
                break
        break
    with open(outfile, "w") as file:
        for variation in sorted(variations):
            file.write(variation + "\n")
final_file = merge_dictionaries(filenames)
for file in filenames:
    os.remove(file)
print("Dictionary saved as " + final_file)
time.sleep(1)

os.system("clear")

