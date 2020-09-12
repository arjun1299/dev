import csv

path='phoible.csv'

d={}
## Lists all the languages along with their phonemes after extracting from phoible.csv

## start with empty dictionary 
with open(path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
         if (row['LanguageName']) not in d:
             d[row['LanguageName']]=[row['Phoneme'],]
         else:
            if(row['Phoneme'] not in d[row['LanguageName']]):
                d[row['LanguageName']].append(row['Phoneme'])
    print(d)

with open('listLang.csv', 'w', newline='') as csvfile:
    fieldnames=['Language','Phonemes']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    for x,y in d.items():
        writer.writerow({fieldnames[0]:x,fieldnames[1]:y})
