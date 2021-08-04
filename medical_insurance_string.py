medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Add your code here
print(medical_data)
update_medical_data=medical_data.replace("#","$")
print(update_medical_data)

num_records=0
for n in update_medical_data.split(';'):
  num_records+=1
print("There are {} medical records in the data".format(num_records))

#Splitting Strings
medical_data_split=update_medical_data.split(';')
print(medical_data_split)

medical_records=[]
for k in medical_data_split:
  medical_records.append(k.split(","))
print(medical_records)

#cleaning data
medical_records_clean=[]
for w in medical_records:
  record_clean=[]
  for k in w:
    record_clean.append(k.strip())
  medical_records_clean.append(record_clean)

print(medical_records_clean)

#analyzing Data
for record in medical_records_clean:
  print(record[0].upper())

names=[]
ages=[]
bmis=[]
insurance_costs=[]

for x in medical_records_clean:
  names.append(x[0])
  ages.append(x[1])
  bmis.append(x[2])
  insurance_costs.append(x[3])

print(names)
print(ages)
print(bmis)
print(insurance_costs)


total_bmi=0
for bmi in bmis:
  total_bmi=total_bmi+float(bmi)
  
#average BMI
average_bmi=total_bmi/len(bmis)
print("Average BMI: {}".format(average_bmi))

#Extras
total_ins=0
for ins in insurance_costs:
  ins=ins.replace("$","")
  total_ins=total_ins+float(ins)
#average Insurance
average_ins=total_ins/len(insurance_costs)
print("Average Insurance Cost: {}".format(average_ins))
#all Data and their corresponding values
for ni  in range(0,len(medical_records_clean)):
  print("{} is {} years old woth a BMI of {} and insurance cost of {}".format(names[ni],ages[ni],bmis[ni],insurance_costs[ni]))

