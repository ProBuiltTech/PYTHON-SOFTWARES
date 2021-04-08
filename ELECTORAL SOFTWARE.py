#================ WARNING ========================#
# Please do not try to edit this code else
# it will create issues but if you want some
# changes or an upgrade to be made please contact
# the developer at 08165335909
#=================================================#

data_base= {
    'PYTHON20201':0,
    'PYTHON20202':0,
    'PYTHON20203':0,
    'PYTHON20204':0,
    'PYTHON20205':0,
    'PYTHON20206':0,
    'PYTHON20207':0,
    'PYTHON20208':0,
    'PYTHON20209':0,
    'PYTHON20210':0,
    'PYTHON20211':0,
    'PYTHON20212':0,
    'PYTHON20213':0,
    'PYTHON20214':0,
    'PYTHON20215':0
}

print(f'''
===================================================
WELCOME MY NAME IS MEGNEX
I AM A VOTING SOFTWARE
Please before i proceed, please enter the Name of
the five candidates contesting for the election 
====================================================
''')

cand1= input(f'''
PLEASE ENTER THE NAME OF THE first candidate\n
''')
cand2= input (f'''
PLEASE ENTER THE NAME OF THE second candidate\n
''')
cand3= input (f'''
PLEASE ENTER THE NAME OF THE third candidate\n
''')
cand4= input (f'''
PLEASE ENTER THE NAME OF THE fourth candidate\n
''')
cand5= input (f'''
PLEASE ENTER THE NAME OF THE fifth candidate\n
''')


candidates= {
    cand1:0,
    cand2:0,
    cand3:0,
    cand4:0,
    cand5:0
}

con1= candidates[cand1]
con2= candidates[cand2]
con3= candidates[cand3]
con4= candidates[cand4]
con5= candidates[cand5]

election_time = 'OPEN'
while election_time == 'OPEN':
    voter_number= input('Please Enter Your Voter\'s Card Id\n')
    if voter_number=='ADMIN2020' or voter_number in data_base:
        if voter_number=='ADMIN2020'or data_base[voter_number]==0:
            vote= input(f'''
            CHOOSE A CANDIDATE
            1 for {cand1}
            2 for {cand2}
            3 for {cand3}
            4 for {cand4}
            5 for {cand5}
            ''')
            if vote=='1':
                con1+= 1
                print(f'''
                -----------------------
                |  vote was casted    |
                -----------------------
                ''')
                data_base[voter_number]=1
            elif vote=='2':
                con2+= 1
                print(f'''
                -----------------------
                |  vote was casted    |
                -----------------------
                ''')
                data_base[voter_number]=1
            elif vote=='3':
                con3+= 1
                print(f'''
                -----------------------
                |  vote was casted    |
                -----------------------
                ''')
                data_base[voter_number]=1
            elif vote=='4':
                con4+= 1
                print(f'''
                -----------------------
                |  vote was casted    |
                -----------------------
                ''')
                data_base[voter_number]=1
            elif vote=='5':
                con5+= 1
                print(f'''
                -----------------------
                |  vote was casted    |
                -----------------------
                ''')
                data_base[voter_number]=1
            elif vote=='CLOSEELECTION':
                
                max_value= 0
                zero_vote= []
                voted= []
                max_key= ''

                for x in data_base:
                    if data_base[x]==max_value:
                        zero_vote.append(x)
                    else:
                        voted.append(x)
                ele_sta= (f'''
                                [ ELECTION STATISTICS ]
                |-------------------------------------------------------------|
                    NUMBER OF VOTERS REGISTERED => {len(data_base)}
                    NUMBER OF REGISTERED VOTERS VOTED => {len(voted)}
                    NUMBER OF REGISTERED VOTERS NOT VOTED => {len(zero_vote)}
                |-------------------------------------------------------------|
                ''')
                
                file_w = open('ELECTION_STATISTICS.txt','w')
                file_w.write(ele_sta) 
                file_w.close()
                
                print(ele_sta)
                
                sta= (f'''
                           [ VOTING STATISTICS ]
                |--------------------------------------------|
                           {cand1} {con1} votes            
                           {cand2} {con2} votes
                           {cand3} {con3} votes
                           {cand4} {con4} votes
                           {cand5} {con5} votes
                |--------------------------------------------|
                ''')
                
                file_w = open('VOTING_STATISTICS.txt','w')
                file_w.write(sta) 
                file_w.close()
                
                print(sta)
                
                vote= {
                    cand1:con1,
                    cand2:con2,
                    cand3:con3,
                    cand4:con4,
                    cand5:con5
                }

                max_value= 0
                max_key= ''

                for x in vote:
                    if vote[x] > max_value:
                        max_value = vote[x]
                        max_key= x
                        
                res= (f'''
                                        [ VOTING RESULT ]
                |----------------------------------------------------------------|
                    {max_key} WON THE ELECTION WITH A TOTAL OF {max_value} VOTES
                    
                |----------------------------------------------------------------|
                ''')
                
                file_w = open('VOTING_RESULT.txt','w')
                file_w.write(res) 
                file_w.close()
                
                print(res)
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
        
#=========================================================#
# Date Created: 7th April 2021
#=========================================================#
input()