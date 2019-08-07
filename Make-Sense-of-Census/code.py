# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path, delimiter=",", skip_header=1)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census=np.array([])
census = np.concatenate((data,new_record),axis=0)

#Code starts here



# --------------
#Code starts here
age = np.array(census[:,0])
max_age=np.max(age)
print(max_age)
min_age=np.min(age)
print(min_age)
age_mean=np.mean(age)
print(age_mean)
age_std=np.std(age)
print(age_std)



# --------------
#Code starts here
race_0=np.array(census[census[:,2]==0])
race_1=np.array(census[census[:,2]==1])
race_2=np.array(census[census[:,2]==2])
race_3=np.array(census[census[:,2]==3])
race_4=np.array(census[census[:,2]==4])

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

L=[len_0,len_1,len_2,len_3,len_4]
print(L)
minority_no= min(L)
minority_race=L.index(6)
print(minority_race)



# --------------
#Code starts here

#Subsetting the array based on the age 
senior_citizens=census[census[:,0]>60]

#Calculating the sum of all the values of array
working_hours_sum=senior_citizens.sum(axis=0)[6]

#Finding the length of the array
senior_citizens_len=len(senior_citizens)

#Finding the average working hours
avg_working_hours=working_hours_sum/senior_citizens_len

#Printing the average working hours
print((avg_working_hours))

#Code ends here


# --------------
#Code starts here
high = census[census[:,1]>10]
low = census[census[:,1]<=10]
print(high)
print(low)
avg_pay_high = high[:,7].mean()
avg_pay_low = low[:,7].mean()
print(avg_pay_high)
print(avg_pay_low)



