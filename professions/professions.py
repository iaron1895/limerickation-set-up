from helper import count_syllables, load_model, save_model

file1 = open('professions/professions.txt', 'r')
Lines = file1.readlines()

professions = []
for line in Lines:
    prof = line[:-1]
    if prof.isalpha():
        syl = count_syllables(line[:-1])
        if syl < 4:
            professions.append(prof)

file1.close()

final_professions = []
adjectives = load_model('adjectives/adjectives_list.pickle')
adjective_professions_dictionary = dict()
for (adj1, adj2) in adjectives:
    adjective_syllables = count_syllables(adj1)
    result = []
    for p in professions:
        profession_syllables = count_syllables(p)
        if profession_syllables + adjective_syllables in [2,3,4]:
            result.append(p)
            if (p, p.capitalize()) not in final_professions:
                final_professions.append((p, p.capitalize()))
    adjective_professions_dictionary[adj1] = result

print(adjective_professions_dictionary["abandoned"])
print(len(final_professions))

save_model(final_professions,"professions/professions_list")
save_model(adjective_professions_dictionary, "professions/adjective_professions")
