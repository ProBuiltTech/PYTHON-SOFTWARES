#================ WARNING ========================#
# Please do not try to edit this code else
# it will create issues but if you want some
# changes or an upgrade to be made please contact
# the developer at 08165335909
#=================================================#

voting_id= {
    'PYTHON20201':0,
    'PYTHON20202':0,
    'PYTHON20203':0,
    'PYTHON20204':0,
    'PYTHON20205':0,
    'PYTHON20206':0,
    'PYTHON20207':0,
    'PYTHON20208':0
}


print(f'''
=====================================
WELCOME MY NAME CYNEX
I AM A VOTING SOFTWARE:
please i only accept two candidates
=====================================
''')
cand1= input(f'''
----------------------------------------------
PLEASE ENTER THE NAME OF THE first candidate\n
----------------------------------------------
''')
cand2= input (f'''
-----------------------------------------------
PLEASE ENTER THE NAME OF THE second candidate\n
-----------------------------------------------
''')

candidates= {
    cand1:0,
    cand2:0
}
con1= candidates[cand1]
con2= candidates[cand2]
election_time = 'OPEN'
while election_time == 'OPEN':
    voter_number= input('enter your election number\n')
    if voter_number in voting_id or voter_number=='ADMIN2020' :
        if voter_number=='ADMIN2020' or voting_id[voter_number]==0:
            vote= input(f'''
            CHOOSE A CANDIDATE
            Y for {cand1}
            N for {cand2}
            ''')
            if vote=='Y':
                con1+= 1
                print(f'''
                -----------------------
                |  vote was casted    |
                -----------------------
                ''')
                voting_id[voter_number]=1
            elif vote=='N':
                con2+= 1
                print(f'''
                -----------------------
                |  vote was casted    |
                -----------------------
                ''')
                voting_id[voter_number]=1
            elif vote=='CLOSEELECTION':
                
                max_value= 0
                zero_vote= []
                voted= []
                max_key= ''

                for x in voting_id:
                    if voting_id[x]==max_value:
                        zero_vote.append(x)
                    else:
                        voted.append(x)
                        
                esta= (f'''
                                [ ELECTION STATISTICS ]
                |-------------------------------------------------------------|
                    NUMBER OF VOTERS REGISTERED => {len(voting_id)}
                    NUMBER OF REGISTERED VOTERS VOTED => {len(voted)}
                    NUMBER OF REGISTERED VOTERS NOT VOTED => {len(zero_vote)}
                |-------------------------------------------------------------|
                ''')
                print(esta)
                
                file_w = open('ELECTION_STATISTICS1.txt','w')
                file_w.write(esta) 
                file_w.close()
                
                vsta= (f'''
                       [ VOTING STATISTICS ]
                |-----------------------------------|
                       {cand1} {con1} votes            
                       {cand2} {con2} votes            
                |-----------------------------------|
                ''')
                file_w = open('VOTING_STATISTICS1.txt','w')
                file_w.write(vsta) 
                file_w.close()
                
                print(vsta)
                
                if con1 > con2:
                    res=(f'''
                            [ VOTING RESULT ]
                   |---------------------------------|
                      {cand1} WON THE ELECTION  
                   |---------------------------------|
                    ''')
                    file_w = open('VOTING_RESULT.txt','w')
                    file_w.write(res) 
                    file_w.close()
                
                    print(res)
                elif con1==con2:
                    draw=(f'''
                       |---------------------------|
                          NO ONE WON THE ELECTION 
                       |---------------------------|
                        ''')
                    file_w = open('ELECTION_RESULT.txt','w')
                    file_w.write(draw) 
                    file_w.close()

                    print(draw)
                else:
                    res1=(f'''
                   |----------------------------------|
                        {cand2} WON THE ELECTION 
                   |----------------------------------|
                    ''')
                    file_w = open('VOTING_RESULT.txt','w')
                    file_w.write(res1) 
                    file_w.close()

                    print(res1)
                election_time= 'CLOSED'
            else:
                print(f'''
                |----------------------------------|
                   YOUR VOTE WASN\'t CASTED:
                   
                    please try again and input the
                    right command to vote
                |----------------------------------|
                ''')
        else:
            print(f'''
            |-----------------------------|
                YOU HAVE VOTED BEFORE 
            |-----------------------------|
            ''')
    else:
        print(f'''
        |----------------------------------|
            Wrong Voter\'s Id Number
        |----------------------------------|
        ''')
        
#==========================================================#
# This software was created by VICTOR WILIKS
# Telephone: 01865335909
#==========================================================#
input()