###################################
# Author: Karan Balani (krnblni)
###################################

import db

def findPrescription(disease):
    if disease == "Pneumonia":
        pass
    elif disease == "Cough":
        pass
    elif disease == "Diarrhea":
        pass
    elif disease == "Malaria":
        pass
    elif disease == "Chicken Pox":
        pass
    elif disease == "Jaundice":
        pass
    else:
        print("\n\nI N V A L I D   D I S E A S E   I N P U T\n\n")

def showPrescriptionToUser(dObject):
    print("\n\n**************************************************** Prescription ****************************************************")
    
    # printing name of the disease
    print("\n   NAME: \t\t{}".format(dObject.name))

    # printing causes of the diease
    print("\n   CAUSES: ", end = "")
    flag = 0
    for cause in dObject.causes:
        if flag == 0:
            print("\t\t{}".format(cause))
            flag = 1
        else:
            print("\t\t\t{}".format(cause))
    
    # printing symptoms of the disease
    print("\n   SYMPTOMS: ", end = "")
    flag = 0
    for symptom in dObject.symptoms:
        if flag == 0:
            print("\t\t{}".format(symptom))
            flag = 1
        else:
            print("\t\t\t{}".format(symptom))

    # printing medical salts for the disease
    print("\n   MEDICAL SALTS: ", end = "")
    flag = 0
    for medicalSalt in dObject.medicineSalts:
        if flag == 0:
            print("\t{}".format(medicalSalt))
            flag = 1
        else:
            print("\t\t\t{}".format(medicalSalt))

    # printing precautions for the disease
    print("\n   PRECAUTIONS: ", end = "")
    flag = 0
    for precaution in dObject.precautions:
        if flag == 0:
            print("\t{}".format(precaution))
            flag = 1
        else:
            print("\t\t\t{}".format(precaution))

    # printing time duration
    print("\n   TIME DURATION: \t{}".format(dObject.timeDuration))


    print("\n************************************************************************************************************************\n\n")

showPrescriptionToUser(db.dDiarrhea)