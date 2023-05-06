import random

when = ['a long time ago','few century back','it is a tail before you were even born',
        'its a story of christ era','the day you were born','it was era before thanos arrived']

who =  ['spider-man','ironman','captian america','hulk','thor','deadpool','vision']

went =  ['batcave','avenger tower','gotham city','stark tower','Arkham Asylum']
         
what = ['to dance', 'to steal his favourite ice cream ','to fight for justice','to take revenge','to work on new base']

#now we have provided the things we want in our story 
# now we are going to active random fuction to form story from the list 

story = (random.choice(when) + ',' + random.choice(who) + ' went to ' + random.choice(went) + ' ' + random.choice(what) + '.')
print(story)

 
 
