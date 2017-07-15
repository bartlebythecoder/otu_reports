#!/usr/bin/python

import matplotlib.pyplot as plt
import sqlite3

def hex_to_num(x):
    h2n_dict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,
                 '8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'J':18}
    return int(h2n_dict[x])



# MAIN PROGRAM

# Open the SQLite 3 database

print ('Which database would you like?')
print ('1. Spinward Marches')
print ('2. Solomani Rim')
print ('3. Core')
db_choice_no = input('Please pick a number... ')
database_dict = {'1':'spinward_marches.db','2':'solomani_rim.db','3':'core.db'}
header_dict = {'1':'the Marches','2':'the Rim','3':'Core'}
conn = sqlite3.connect(database_dict[db_choice_no])
c = conn.cursor()                   

       


tech_level_rating = {   '0':10,'1':10,'2':10,'3':10,'4':10,
                        '5':100,'6':100,'7':100,'8':100,'9':100,
                        'A':1000,'B':1000,'C':1000,'D':1000,'E':1000,
                        'F':1000,'G':1000,'H':1000,'J':1000}
                        
starport_to_color = {'A':10,'B':9,'C':8,'D':7,'E':6,'X':5}
                        

sql3_select = """ SELECT    name,
                            uwp, 
                            cx
                    FROM    tb_t5_systems """


c.execute(sql3_select)
allrows = c.fetchall()

name = list()
law_level = list()
accept_level = list()
tech_level = list()
strange_level = list()
starport = list()

for row in allrows:
    name_row = row[0]
    starport_row = row[1][0]
    law_level_row = hex_to_num(row[1][6])
    accept_level_row = hex_to_num(row[2][2])
    tech_level_row = hex_to_num(row[1][8])
    strange_level_row = hex_to_num(row[2][3])
    print (name_row, starport_row, tech_level_row)
    
    
    if starport_row == 'A':
        starport.append(starport_row)
        name.append(name_row)
        law_level.append(law_level_row)
        accept_level.append(accept_level_row)
        tech_level.append(tech_level_row)
        strange_level.append(strange_level_row)
    
plt.xlabel('Tech Level')
plt.ylabel('Strange Level')
plt.title('Acceptance and Law in ' + header_dict[db_choice_no])

plt.axis([-1, 17, -1, 12])
plt.scatter(tech_level,strange_level,s=100, c = accept_level, cmap=plt.cm.YlGn)

# for i, txt in enumerate(name):
	# plt.annotate(txt, (law_level[i]-.5,accept_level[i]))
	
plt.show()