diseases=['pneumonia','cold']
symptoms=['cough, fever, rusty or green phlegm, fast breathing and shortness of breath, shaking chills, chest pain, fast heartbeat, fatigue and weakness, nausea and vomiting, diarrhea, sweating, headache, muscle pain','running or stuffing nose, frequent throat clearing, sore throat, feeling of liquid running down the back of your throat, hoarseness']
#example input
#fast heartbeat, hoarseness
def userinput():
    flag=0
    user_data=[]
    choice = str(input("Do you know your disease ? (y/n) >>> "))
    if (choice == 'y' or choice == 'Y'):
        user_input = str(input("\nEnter the name of your disease >>> "))
        flag=1
        user_data=user_input
    elif (choice == 'n' or choice == 'N'):
        user_input = str(input("\nEnter your symptoms (separated by commas ',') >>> "))
        user_data=user_input.split(",")
        flag=2

    else:
        print("\nERROR! Wrong input.")
        userinput()

    data=[flag,user_data]
    return data

def mapping(data):
    len_d=len(diseases)
    len_s=len(symptoms)
    flag=data[0]
    user_data=data[1]
    success=False
    disease_name=[]
    len_ud=len(user_data)
    if(flag == 1):
        for i in range(0,len_d):
            if (user_data[0] in diseases[i]):
                #print("\nDisease = {}".format(diseases[i]))
                #print("Symptoms: {}".format(symptoms[i]))
                success=True
                disease_name.append(diseases[i])


    elif (flag == 2):
        for i in range(0,len_s):
            for j in range(0,len(user_data)):
                if(user_data[j] in symptoms[i]):

                    #print("\nDisease = {}".format(diseases[i]))
                    #print("Symptoms: {}".format(symptoms[i]))
                    success = True
                    disease_name.append(diseases[i])

    if(success==False):
        print("Nothing Found ! Try again")

    return disease_name

def sorting(sort):
    data=sort
    len_d=len(data)
    len_diseases=len(diseases)
    data_send=[]
    if(len_d==1):
        for x in range(0,len_diseases):
            if(data[0]==diseases[x]):
                data_send.append(diseases[x])
    else:
        print("\n")
        for k in range(0,len_d):
            for l in range(0,len_diseases):
                if(data[k]==diseases[l]):
                    print("{}- {}".format(k+1,symptoms[l]))

        print("\nOut of the following symptoms select the ones which match yours the most")
        option=int(input("Enter the prefered option (1/2/3/.....) >>> "))
        data_send.append(diseases[option-1])

    return data_send

#example input
#fast heartbeat, hoarseness
data=userinput()
sort=mapping(data)
print(sorting(sort))
