import json,os
print('_____welcome to employe management system ______!!!')
d,asks = {},['name','salary','age','gender']
                                    # this is creating the json File
if not os.path.isfile('database.json'):
    open('database.json','w')

def maintan_data():                 # this is data management function
    dataFile=open('database.json','w')
    hold=json.dumps(d,indent=4)
    dataFile.write(hold)

def create(name):                   # this is create user data function 
    global d
    d2={}
    for ask in asks:
        if ask == 'gender':
            while True:
                gnd=input('enter the gender M/F:')
                if gnd =='M' or gnd=='F' or gnd =='m' or gnd=='f':
                    d2[ask]=gnd.upper()
                    print(ask,'this is running dkkkkkkkkkkkkkkkkkk')
                    break
                else:
                    print("\t wrong!!!!! ~~~~ enter 'M' or 'F' only")
                    pass
        else:
            print('enter the',ask)
            r=input('____________:')
            d2[ask]=r

    print('\n \t successfully add your data !!\n')    
    d[name]=d2
    maintan_data()

def update_Data(name):              # this is update user data function
    global d
    datafile2=open('database.json','r')
    hold2=datafile2.read()
    x=json.loads(hold2)
    li=[k for k in x.keys()]
    if name in li:
        li2=[k2 for k2 in d[name].keys()]
        print(li2)
        ch=input('what you want to change :')
        if ch in li2:
            ans=input('enter the new value :')
            d[name][ch]=ans
            print('\n \tsuccessfully update your data !!\n') 
        else:print('you enter something wrong')
    maintan_data()

def delete_Data(name):              # this is delete user data function
    global d
    datafile2=open('database.json','r')
    hold2=datafile2.read()
    x=json.loads(hold2)
    del d[name]
    print('\n \t successfully delete your data !!\n') 
    maintan_data()

def read_Data(name):                #this is read function
    print(d[name])
                        
while True:                         #this is starting 
    f3=open('database.json')
    s=f3.read()
    f3.close()
    if len(s)>1:                    #this is loading data for the json file
        def add():
            global d
            f4=open('database.json')
            h5=f4.read()
            l=json.loads(h5)
            f4.close()
            d=l
        add()
    print('\n 1) Add_Data \n 2) Edit_Data \n 3) Remove_Data \n 4) Read_Data \n 5) Exit \n')
    c=input('enter :')
    if c=='exit' or c=='5':
        print('<<<<<<<<<<come again>>>>>>>>>>>')
        break
    name=input('\n enter the gmail :') 
    name=name.lower()
    if c=='1' :
        n=name[-10:]
        if name not in d:
            if n=='@gmail.com':create(name)
            else:print('this gmail is invalid','\U0001F630','\U0001F630',' \n \tex :ramu@gmail.com like this ')
        else:print('this gmail is already avalable')
    elif c=='2' :
        if name in d:update_Data(name)
        else:print('this gmail not avalable\n')
    elif c=='3' :
        if name in d:delete_Data(name)
        else:print('this gmail not avalable \n')
    elif c=='4' :
        if name in d:read_Data(name)
        else:print('this gmail not avalable\n')
    if 'total'==name:
        print(d)