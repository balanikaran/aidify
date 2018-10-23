###################################
# Data by: Umang Goyal and Aditya Jain
###################################
# Author: Karan Balani (krnblni)
###################################

class Disease:
    def __init__(self, name, causes, symptoms, medicineSalts, precautions, timeDuration):
        self.name = name
        self.causes = causes
        self.symptoms = symptoms
        self.medicineSalts = medicineSalts
        self.precautions = precautions
        self.timeDuration = timeDuration

#-------------- Disease 1 --------------#
# Name: Pneumonia
#
# Causes: Bacteria, Viruses, Mycoplasma, Various Chemicals
#
# Symptoms: Cough, Fever, Rusty/Green Phlegm, Fast breathing, 
#           Shortness of breath, Shaking Chills, Fast Heartbeat, 
#           Chest Pain, Fatigue and weakness, Nausea, Vomiting, 
#           Sweating, Headache, Muscle pain
#
# Medical Salts: Penicillin-G
#
# Precautions: Hand hygiene, use of personal protective equipments, 
#              safe injection practices, 
#              respiratory hygiene/cough etiquette
#
# Time Duration: 3-5 days 
#---------------------------------------#
dPneumonia = Disease("Pneumonia", 
["Bacteria", "Viruses", "Mycoplasma", "Various Chemicals"], 
["Cough", "Fever", "Rusty/Green Phlegm", "Fast breathing", "Shortness of breath", 
"Shaking Chills", "Fast Heartbeat", "Chest Pain", "Fatigue and weakness", "Nausea", 
"Vomiting", "Sweating", "Headache", "Muscle pain"], 
["Penicillin-G"], ["Hand hygiene", "Use of personal protective equipments", 
"Safe injection practices", "Respiratory hygiene/cough etiquette"], "3-5 Days")


#-------------- Disease 2 --------------#
# Name: Cough
#
# Causes: Cold, Flu, Allergy, Hay Fever, Inhaled dust or smoke, 
#         Bronchiectasis, Postnasal drip
#
# Symptoms: A runny or stuffy nose, 
#           A feeling of liquid running down the back of your throat (postnasal drip), 
#           Frequent throat clearing and sore throat, 
#           Hoarseness complications, Dehydration, 
#           Severe Abdominal pain
#
# Medical Salts: Dextromethorphan (DM)
#
# Precautions: Cough/sneeze into a tissue or handkerchief, 
#              Wash your hands often with soap to avoid infection, 
#              Avoid touching your eyes, nose and mouth, 
#              Drink plenty of fluids and eat healthy to build immunity, 
#              Keep your distance from people to prevent spreading cold and cough
#
# Time Duration: 18 Days
#---------------------------------------#
dCough = Disease("Cough", 
["Cold", "Flu", "Allergy", "Hay Fever", "Inhaled dust or smoke", "Bronchiectasis", "Postnasal drip"], 
["A runny or stuffy nose", "A feeling of liquid running down the back of your throat (postnasal drip)", "Frequent throat clearing and sore throat", "Hoarseness complications", "Dehydration", "Severe Abdominal pain"], 
["Dextromethorphan (DM)"], 
["Cough/sneeze into a tissue or handkerchief", "Wash your hands often with soap to avoid infection", "Avoid touching your eyes, nose and mouth", "Drink plenty of fluids and eat healthy to build immunity", "Keep your distance from people to prevent spreading cold and cough"], 
"18 Days")

#-------------- Disease 3 --------------#
# Name: Diarrhea
#
# Causes: Contaminated food, Alcohol abuse, 
#         Diseases of the intestines, 
#         Eating foods that upset the digestive system, 
#         Infection by bacteria or other organisms, 
#         Laxative abuse, Medications, 
#         Allergies to certain foods, Diabetes Mellitus Type 2, 
#         Overactive thyroid (Hyperthyroidism), Radiation therapy, 
#         Some cancers
#
# Symptoms: Bloated stomach, Cramps, Thin or watery stools, 
#           The constant feeling that you need to have a bowel movement, 
#           Nausea, Vomiting
#
# Medical Salts: Imodium, Pepto-Bismol, Kaopectate
#
# Precautions: Rehydrate by adding powdered Gatorade to bottled water, 
#              Eat bland
#
# Time Duration: 2-3 Days
#---------------------------------------#

dDiarrhea = Disease("Diarrhea",
["Contaminated food", "Alcohol abuse", "Diseases of the intestines", "Eating foods that upset the digestive system", "Infection by bacteria or other organisms", "Laxative abuse", "Medications", "Allergies to certain foods", "Diabetes Mellitus Type 2", "Overactive thyroid (Hyperthyroidism)", "Radiation therapy", "Some cancers"],
["Bloated stomach, Cramps", "Thin or watery stools", "The constant feeling that you need to have a bowel movement", "Nausea", "Vomiting"],
["Imodium", "Pepto-Bismol", "Kaopectate"],
["Rehydrate by adding powdered Gatorade to bottled water", "Eat bland"],
"2-3 Days")

#-------------- Disease 4 --------------#
# Name: Malaria
#
# Causes: It is transmitted to humans through the bite of the Anopheles mosquito
#
# Symptoms: Fever and chills, Impaired consciousness, 
#           Prostration, Adopting a prone position, 
#           Multiple convulsions, 
#           Deep breathing and respiratory distress, 
#           Abnormal bleeding and signs of anemia , 
#           Clinical jaundice and evidence of vital organ dysfunction
#
# Medical Salts: Quinine (Qualaquin)
#
# Precautions: Apply insect repellent containing 30-35% DEET to exposed skin, 
#              Protect yourself day and night, because different mosquitoes feed at different times, 
#              Stay and sleep in screened-in or air-conditioned rooms
#
# Time Duration: 2 weeks
#---------------------------------------#

dMalaria = Disease("Malaria",
["It is transmitted to humans through the bite of the Anopheles mosquito"],
["Fever and chills", "Impaired consciousness", "Prostration", "Adopting a prone position", "Multiple convulsions", "Deep breathing and respiratory distress", "Abnormal bleeding and signs of anemia", "Clinical jaundice and evidence of vital organ dysfunction"],
["Quinine (Qualaquin)"],
["Apply insect repellent containing 30-35% DEET to exposed skin", "Protect yourself day and night, because different mosquitoes feed at different times", "Stay and sleep in screened-in or air-conditioned rooms"],
"2 weeks")

#-------------- Disease 5 --------------#
# Name: Chicken Pox
#
# Causes: The varicella-zoster virus (VZV) causes chickenpox
#
# Symptoms: Ever that lasts longer than 4 days, 
#           Fever that rises above 102°F (38.9°C), 
#           Any areas of the rash or any part of the body becomes very red, warm, or tender, or begins leaking pus, 
#           Extreme illness, Difficult waking up or confused demeanor, 
#           Difficulty walking, Stiff neck, Frequent vomiting, 
#           Difficulty breathing, Severe cough, 
#           Severe abdominal pain, 
#           Rash with bleeding or bruising (hemorrhagic rash)
#
# Medical Salts: Acetomenaphin
#
# Precautions: Do not scratch the itch
#
# Time Duration: 10-21 Days
#---------------------------------------#

dChickenPox = Disease("Chicken Pox",
["The varicella-zoster virus (VZV) causes chickenpox"],
["Ever that lasts longer than 4 days", "Fever that rises above 102°F (38.9°C)", "Any areas of the rash or any part of the body becomes very red, warm, or tender, or begins leaking pus", "Extreme illness", "Difficult waking up or confused demeanor", "Difficulty walking", "Stiff neck", "Frequent vomiting", "Difficulty breathing", "Severe cough", "Severe abdominal pain", "Rash with bleeding or bruising (hemorrhagic rash)"],
["Acetomenaphin"],
["Do not scratch the itch"],
"10-21 Days")

#-------------- Disease 6 --------------#
# Name: Jaundice
#
# Causes: Acute inflammation of the liver, 
#         Inflammation of the bile duct, 
#         Obstruction of the bile duct, 
#         Hemolytic anemia, 
#         Gilbert's syndrome
#
# Symptoms: Include a yellow tinge to the skin, 
#           Include whites of the eyes
#
# Medical Salts: Antiviral, Steroid medications
#
# Precautions: Drink at least eight glasses of fluids per day. Water and herbal tea are excellent options, 
#              Consider adding milk thistle to your routine. You can prepare a fresh tea or eat the seeds as a snack, 
#              Opt for fruits like papaya and mango, which are rich in digestive enzymes, 
#              Eat at least 2 1/2 cups of veggies and 2 cups of fruit per day, 
#              Look for high-fiber foods, such as oatmeal, berries, and almonds
#
# Time Duration: 2 weeks
#---------------------------------------#

dJaundice = Disease("Jaundice",
["Acute inflammation of the liver", "Inflammation of the bile duct", "Obstruction of the bile duct", "Hemolytic anemia", "Gilbert's syndrome"],
["Include a yellow tinge to the skin", "Include whites of the eyes"],
["Antiviral", "Steroid medications"],
["Drink at least eight glasses of fluids per day", "Water and herbal tea are excellent options", "Consider adding milk thistle to your routine", "You can prepare a fresh tea or eat the seeds as a snack", "Opt for fruits like papaya and mango, which are rich in digestive enzymes", "Eat at least 2 1/2 cups of veggies and 2 cups of fruit per day", "Look for high-fiber foods, such as oatmeal, berries, and almonds"],
"2 weeks")