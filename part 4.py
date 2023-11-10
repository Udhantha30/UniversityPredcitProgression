#difine variables
pro=0
tra=0
ret=0
exc=0
#difine dictionary
outcomedic={}

#difining the outcomefunction
def function():
    global cred_pas,defer,fail,st_username,exc,pro,tra,ret
    if fail>=80:
        print("Exclude")
        #adding the key and value to dictionary      
        outcomedic[st_username]=f"Exclude-{cred_pas},{defer},{fail}\n"
        exc=exc+1

    elif cred_pas==120:
        print('Progress')
        outcomedic[st_username]=f"Progress-{cred_pas},{defer},{fail}\n"
        pro=pro+1

    elif cred_pas==100:
        print("Progress(module trailer)")
        outcomedic[st_username]=f"Progress(module trailer)-{cred_pas},{defer},{fail}\n"
        tra=tra+1
        
    else:
        print("Do not progress-module retriever")
        outcomedic[st_username]=f"Do not progress-module retriever-{cred_pas},{defer},{fail}\n"
        ret=ret+1

#main while loop
x=0
while x!=1:
    #taking input for user name
    st_username=input("Enter Your User Name: ")
    #looping to get correct input
    while True:
        #using tryblock to get correct input
        try:
            #taking input for credit pass
            cred_pas=int(input("Please enter your credits at pass: "))
        except ValueError:
            print('Integer required')
            continue
        #checking input in the range
        if not cred_pas in (0,20,40,60,80,100,120):
            print('Out of range')
            continue
        break
    while True:

        try:
            defer=int(input("Please enter your credit at defer: "))
        except ValueError:
            print('Integer required')
            continue
        if not defer in (0,20,40,60,80,100,120):
            print('Out of range')
            continue
        break

    while True:

        try:
            fail=int(input("Please enter your credit at fail: "))
        except ValueError:
             print('Integer required')
             continue

        if not fail in (0,20,40,60,80,100,120):
            print('Out of range')
            continue
        break
    #getting sum of credit pass, defer pass and fail pass
    total=cred_pas+defer+fail
    #checking the sum of credit pass, defer pass and fail pass are in the range
    if total!=120:
        print("Total incorrect")
        continue
    #calling the function
    function()
    
    x=1
    print('Would you like to enter another set of data?')
   
    while x!=0:
          #taking input for yes or quit
          y_n=input("Enter 'y' for yes or 'q' to quit and view results: ")
          if y_n=='y':
           x=0
                   
          elif y_n=='q':
            print("Exitting program...\n")
            break
          else:
            print("Invalid input")
            continue
#printing the histogram         
print('Histogram')
print("Progress ",pro,":", "*"*pro)
print("Trailer ",tra,":", "*"*tra)
print("Retriever ",ret,":", "*"*ret)
print("Exclude ",exc,":", "*"*exc)
outcomes=exc+pro+ret+tra
print(outcomes,"outcomes in total.\n")

print("\n")
#printing keys and values in the dictionary using the for loop
for (k,v) in outcomedic.items():
    print(k,":",v)
