# limerickation-set-up

The code in this repository creates the initial pickle files needed to set up the limerickation application.

Step 1 - Adjectives:
The complete adjectives list is taken from https://gist.github.com/hugsy/8910dc78d208e40de42deb29e62df913
Run adjectives.py to filter out any adjectives longer than 3 syllables
The english-adjectives-manual-filtered.txt file contains the list of adjectives shorter than 4 syllables and that can apply to a person.
Run adjectives-pickle.py to save the list as a pickle file. 

Step 2 - Places:
The list of places is taken from https://datahub.io/core/world-cities\#readme, a list by Geonames.
Run places.py to save city and country names that only contain alphabetic characters as a pickle file.

Step 3 - Professions:
The list of professions is taken from https://www.britannica.com/dictionary/eb/3000-words/topic/jobs-professions/1
Run professions.py to create a pickle file containing a dictionary where the keys are the adjectives found in step 1, and for each adjective
a list of professions is created to find all potential combinations of adjective and professions that are between 2 and 4 syllables. 

Step 4 - Templates:
Download the json limerick data set from https://doi.org/10.5281/zenodo.5722527
Run templateCreation.py to create four pickle files, each containing POS tagged templates for second, third, fourth and fifth verses of a limerick respectively.

These pickle files are used for the initialisation of the limerickation application.
