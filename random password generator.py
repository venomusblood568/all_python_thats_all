import random       #to select random without any kind of password
import array        # arrays are a data structure like lists

max_len = 16         #the length of the password is defing here

NUMERICAL_CHAR = ['0','1','2','3','4','5','6','7','8','9']    #digital num which is going to be use in ps
LOWER_CASE_CHAR = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',] 
UPPER_CASE_CHAR = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',] 
SYMBOL_CHAR = ['!','@','#','$','%','&','<','>','?']

COMBINATION_LIST = NUMERICAL_CHAR + LOWER_CASE_CHAR + UPPER_CASE_CHAR + SYMBOL_CHAR  
#COMBINATION GOING TO USE AND BEFORE PRINTING OUTPUT WE ARE GOING TO SHUFFLE 

#NOW COMES THE MAIN STUFF WE ARE GOING TO USE RANDOM TO SELECT OUR RANDOM CHARACTER
rand_num = random.choice(NUMERICAL_CHAR)
rand_lower = random.choice(LOWER_CASE_CHAR)
rand_upper = random.choice(UPPER_CASE_CHAR)
rand_symbol = random.choice(SYMBOL_CHAR)

TEMP_PASSWORD = rand_num + rand_lower + rand_upper + rand_symbol 
# NOW IT IS SELECTING SET OF RANDOM COLLECTION OF CHAERCATER 

for x in range (max_len - 4):
    TEMP_PASSWORD = TEMP_PASSWORD + random.choice(COMBINATION_LIST)
    # NOW WE ARE GOING TO SHUFFLE THE PASSWORD EACH TIME SO IS DOESN'T FOLLOW SAME PATTERN OR NO TWO PASSWORD CAN BE SAME
    TEMP_PASSWORD_LIST = array.array('u' ,TEMP_PASSWORD)
    random.shuffle(TEMP_PASSWORD_LIST)

#traverse the temporary password array and append the chars and to form the password
PASSWORD = ''                                   #main password 
for x in TEMP_PASSWORD_LIST:
    PASSWORD = PASSWORD +  x 

print(PASSWORD)
