import os
import pickle
import json
import nltk

class Limerick():
    def __init__(self, value):
        self.text = value
        values = value.split('\n')
        self.verse1 = values[0]
        self.verse2 = values[1]
        self.verse3 = values[2]
        self.verse4 = values[3]
        self.verse5 = values[4]
    def __str__(self):
        return self.text

# save object as a pickle file
def save_model(model,filename):
    filename += ".pickle"
    with open(filename, 'wb') as target:
        pickle.dump(model, target)

# load object from a pickle file
def load_model(filename):
    with open(filename, 'rb') as target:
        model = pickle.load(target)
    return model

# return Part of Speech tags from list of words
def get_pos_tags(tokens):
    return nltk.pos_tag(tokens)

# filter out limericks from field 'is_limerick' and save as new list
def return_all_limericks():
    f = open('templates/limerick_dataset_oedilf_v3.json')
    data = json.load(f)
    limericks = [d for d in data if d['is_limerick']]
    f.close()   
    all_limericks = []
    for l in limericks:
        all_limericks.append(Limerick(l['limerick']))
    save_model(all_limericks, 'list_of_limericks')
    return all_limericks

# get all second verse templates as POS tags
def get_second_verse_templates():
    all_limericks = return_all_limericks()
    
    # filter limericks by second verse first word
    limericks = [l for l in all_limericks if (l.verse2.startswith("Who ") or l.verse2.startswith("He ") or l.verse2.startswith("She ") or l.verse2.startswith("Whose "))]
    second_verses = [l.verse2 for l in limericks]

    # all second verses should start with who or whose
    for i,v in enumerate(second_verses):
        if v.startswith("He") or v.startswith("She"):
            replacement = 'Who'
            words = v.split()
            words[0] = replacement
            second_verses[i] = ' '.join(words)

    templates = []
    for verse in second_verses:
        # skip all second verses that are questions or are split by full stop
        if '?' in verse or '.' in verse[:-1] or verse[-1] != '.':
            continue
        verse = verse.lower()
        words = verse.split()
        tags = get_pos_tags(words)
        template = [tag[1] for tag in tags]
        # add all templates to pickle file
        if (template[0] == 'WP' or template[0] == 'WP$') and template not in templates:
            templates.append(template)
    save_model(templates, 'templates/second_verse_templates')
    return templates

# get all third verse templates as POS tags
def get_third_verse_templates():
    all_limericks = return_all_limericks()

     # filter limericks by third verse first word
    verses = [l.verse3 for l in all_limericks if (l.verse3.startswith("He ") or l.verse3.startswith("She ") or l.verse3.startswith("I "))]
    
    templates = []
    for verse in verses:
        # skip all third verses that are questions or are split by full stop
        if '?' in verse or '.' in verse[:-1]:
            continue
        tokens = verse.split()
        tags = nltk.pos_tag(tokens)
        template = [t[1] for t in tags]
        # add all templates to pickle file
        templates.append(template)
    save_model(templates, 'templates/third_verse_templates')
    return templates

# get all fourth verse templates as POS tags
def get_fourth_verse_templates():
    all_limericks = return_all_limericks()
    verses = [l.verse4 for l in all_limericks]
    
    templates = []
    for verse in verses:
        # skip all fourth verses that are questions or are split by full stop
        if '?' in verse or '.' in verse[:-1]:
            continue
        tokens = verse.split()
        tags = nltk.pos_tag(tokens)
        template = [t[1] for t in tags]
        # add all templates to pickle file
        templates.append(template)
    save_model(templates, 'templates/fourth_verse_templates')
    return templates

# get all fifth verse templates as POS tags
def get_fifth_verse_templates():
    all_limericks = return_all_limericks()
    verses = [l.verse5 for l in all_limericks]
    
    templates = []
    for verse in verses:
        # skip all fifth verses that are questions or are split by full stop
        if '?' in verse or '.' in verse[:-1]:
            continue
        tokens = verse.split()
        tags = nltk.pos_tag(tokens)
        template = [t[1] for t in tags]
        # add all templates to pickle file
        templates.append(template)
    save_model(templates, 'templates/fifth_verse_templates')
    return templates

# get all third verse templates for experiment in report as POS tags

def get_third_verse_templates_experiment():
    all_limericks = return_all_limericks()
    verses = [l.verse3 for l in all_limericks]
    
    templates = []
    for verse in verses:
        if '?' in verse or '.' in verse[:-1]:
            continue
        tokens = verse.split()
        tags = nltk.pos_tag(tokens)
        template = [t[1] for t in tags]
        templates.append(template)
    save_model(templates, 'templates/third_verse_templates_experiment')
    return templates
