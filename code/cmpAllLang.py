import csv

path="phoible.csv"

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

d=dict()

with open(path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
         if (row['LanguageName']) not in d:
             d[row['LanguageName']]=[row['Phoneme'],]
         else:
            d[row['LanguageName']].append(row['Phoneme'])
    #print(d)
##d now contains all languages and corresponding phonemes

similar=d['English'] #initialize array for similarities 
#English was just chosen at random 
#initialize with all phonemes of the 1st language and remove the uncommon ones through intersection.

    ##checking for similar phonemes deleting the dissimilar ones
for phon in d.values():
    similar=intersection(phon,similar)
print(similar)
