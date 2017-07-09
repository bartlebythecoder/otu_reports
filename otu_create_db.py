#!/usr/bin/python

# This program loads a flat file of Traveller star data
# and loads it into a database for reporting purposes

import sqlite3

def create_t5_table(c,conn):
    sql_create_tb_t5_table = """CREATE TABLE    tb_t5_systems( 
                                                hex TEXT,
                                                name TEXT,
                                                uwp TEXT,
                                                remarks TEXT,
                                                ix TEXT,
                                                ex TEXT,
                                                cx TEXT,
                                                strangeness TEXT,
                                                n TEXT,
                                                bases TEXT,
                                                zone TEXT,
                                                pbg TEXT,
                                                w TEXT,
                                                allegiance TEXT,
                                                stellar TEXT
                                               );"""
                                               
    c.execute('DROP TABLE IF EXISTS tb_t5_systems')
    c.execute(sql_create_tb_t5_table)                                                
                                               
                                               
# MAIN PROGRAM

# Open the SQLite 3 database

 
conn = sqlite3.connect('otu.db')
c = conn.cursor()                   
create_t5_table(c,conn)               



i = 0
for line in open("load_data.txt"):
    i += 1
    systems_ = str(line)
    if i == 1:
        hex_char = systems_.find('Hex')
        name_char = systems_.find('Name')
        uwp_char = systems_.find('UWP')
        remarks_char = systems_.find('Remarks')
        ix_char = systems_.find('{')
        ex_char = systems_.find('(')
        cx_char = systems_.find('[')
        naval_char = systems_.find('N ')
        base_char = systems_.find('B ')
        zone_char = systems_.find('Z ')
        pbg_char = systems_.find('PBG')
        w_char = systems_.find('W ')
        a_char = systems_.find('A ')
        stellar_char = systems_.find('Stellar')
    if i > 2:
        hex_ = (systems_[hex_char:name_char-1])
        name = (systems_[name_char:uwp_char-1])
        uwp  = (systems_[uwp_char:remarks_char-1])
        remarks = (systems_[remarks_char:ix_char-1])
        ix = (systems_[ix_char:ex_char-1])
        ex = (systems_[ex_char:cx_char-1])
        cx = (systems_[cx_char:naval_char-1])      
        strangeness = (systems_[cx_char+3])      
        naval = (systems_[naval_char:base_char-1])    
        base = (systems_[base_char:zone_char-1])    
        zone = (systems_[zone_char:pbg_char-1])     
        pbg = (systems_[pbg_char:w_char-1]) 
        w = (systems_[w_char:a_char-1])   
        a = (systems_[a_char:stellar_char-1])      
        stellar = (systems_[stellar_char:])           

        
        sqlcommand = '''INSERT INTO tb_t5_systems    (  hex, 
                                                        name,
                                                        uwp,
                                                        remarks,
                                                        ix,
                                                        ex,
                                                        cx,
                                                        strangeness,
                                                        n,
                                                        bases,
                                                        zone,
                                                        pbg,
                                                        w,
                                                        allegiance,
                                                        stellar)
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
                        
        body_row =     (hex_,
                        name,
                        uwp,
                        remarks,
                        ix,
                        ex,
                        cx,
                        strangeness,
                        naval,
                        base,
                        zone,
                        pbg,
                        w,
                        a,
                        stellar)
                        
    
        c.execute(sqlcommand, body_row)   
        
        
        
        
        

   
# CLOSE OUT PROGRAM AND COMMIT SQLite COMMANDS
conn.commit()  
c.close()
conn.close()          