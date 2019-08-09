# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000
#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  
# path        [File location variable]
data = pd.read_csv(path)
data_sample = data.sample(n=sample_size,random_state=0)
sample_mean = data_sample['installment'].mean()
print(sample_mean)
sample_std = data_sample['installment'].std()
print(sample_std)
margin_of_error = (z_critical)*(sample_std/math.sqrt(sample_size))
print(margin_of_error)
confidence_interval = [sample_mean-margin_of_error,sample_mean+margin_of_error]
print(confidence_interval)
true_mean = data['installment'].mean()
print(true_mean)
#Code starts here



# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])

#Code starts here

#Creating different subplots
fig,axes=plt.subplots(3,1, figsize=(10,20))

#Running loop to iterate through rows
for i in range(len(sample_size)):
    
    #Initialising a list
    m=[]
    
    #Loop to implement the no. of samples
    for j in range(1000):
        
        #Finding mean of a random sample
        mean=data['installment'].sample(sample_size[i]).mean()
        
        #Appending the mean to the list
        m.append(mean)
        
        
    #Converting the list to series
    mean_series=pd.Series(m)   

    #Plotting the histogram for the series
    axes[i].hist(mean_series, normed=True)

    

#Displaying the plot
plt.show()


#Code ends here


# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest

#Code starts here
data['int.rate'] = data['int.rate'].str.replace('[^\d.]', '').astype(float)
data['int.rate'] = data['int.rate'].div(100)
z_statistic,p_value = ztest(x1=data[data['purpose']=='small_business']['int.rate'],value=data['int.rate'].mean(), alternative='larger')
print(z_statistic)
print(p_value)
if(p_value<0.05):
    print("Reject Null Hypothesis")
else:
    print("Accept Null Hypothesis")


# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here
x=data[data['paid.back.loan']=='No']['installment']
y=data[data['paid.back.loan']=='Yes']['installment']
z_statistic,p_value=ztest(x1=x,x2=y,alternative='two-sided')
print(z_statistic)
print(p_value)
if(p_value<0.05):
    print("Reject H0")
else:
    print("Accept H0")


# --------------
#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here
yes = data[data['paid.back.loan']=='Yes']['purpose'].value_counts()
no =  data[data['paid.back.loan']=='No']['purpose'].value_counts()
observed = pd.concat((yes.transpose(),no.transpose()),axis=1,keys=['Yes','No'])
chi2,p,dof,ex = chi2_contingency(observed)
print(chi2)
if chi2>critical_value:
    print("Reject H0")
else:
    print("Accept H0")


