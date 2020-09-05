import csv

path="phoible.csv"

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

"""
l1=input('Language 1: ')
l2=input('Language 2: ')
"""
n=input("Number of Languages to compare: ")
n=int(n)
lang=[]

d=dict()

for i in range(n):
    l=input("Language {}: ".format(i+1))
    lang.append(l);
for l in lang:
    if(l not in d):
        d[l]=[]#poppulate with empty list

similar=d[lang[0]] #initialize array for similarities 
#initialize with all phonemes of the 1st language and remove the uncommon ones through intersection.

with open(path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
         if (row['LanguageName']) in d:##adding all the phonemes to the corresponding language
             d[row['LanguageName']].append(row['Phoneme'])
    similar=d[lang[0]]

    ##checking for similar phonemes deleting the dissimilar ones
    for phon in d.values():
        similar=intersection(phon,similar)
    print(similar)
