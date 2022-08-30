from helper import count_syllables

file1 = open('adjectives/english-adjectives.txt', 'r')
Lines = file1.readlines()

# filter out all adjectives longer than 3 syllables
with open('adjectives/english-adjectives-filtered.txt', 'w') as f:
    for line in Lines:
        if line[:-1].isalpha():
            syl = count_syllables(line[:-1])
            if syl < 4:
                f.write(line)

f.close()
file1.close()