from helper import save_model

final_adjectives = []

file1 = open('adjectives/english-adjectives-manual-filtered.txt', 'r')
Lines = file1.readlines()

for line in Lines:
    adj = line[:-1]
    final_adjectives.append((adj, adj.capitalize()))

save_model(final_adjectives,"adjectives/adjectives_list")