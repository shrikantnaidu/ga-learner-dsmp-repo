# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
#Code starts here 
data['Gender'].replace('-','Agender',inplace=True)
gender_count = data['Gender'].value_counts()
gender_count.plot(kind='bar')
plt.show()


# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
print(alignment)
alignment.plot(kind='pie')
plt.title('Character Alignment')
plt.show()


# --------------
sc_df = data[['Strength','Combat']]
sc_covariance = sc_df.cov().iloc[0][1]
print('Covariance of sc =',sc_covariance)
sc_strength = sc_df['Strength'].std()
print(sc_strength)
sc_combat = sc_df['Combat'].std()
print(sc_combat)
sc_pearson = sc_covariance/(sc_strength*sc_combat)
print(sc_pearson)
ic_df = data[['Intelligence','Combat']]
ic_covariance = ic_df.cov().iloc[0][1]
print('Cov of ic=',ic_covariance)
ic_intelligence = ic_df['Intelligence'].std()
print(ic_intelligence)
ic_combat = ic_df['Combat'].std()
print(ic_combat)
ic_pearson = ic_covariance/(ic_intelligence*ic_combat)
print(ic_pearson)


# --------------
#Code starts here
total_high = data['Total'].quantile(q=0.99)
print(total_high)
super_best = data[data['Total']>total_high]
super_best_names =list( super_best['Name'])
print(super_best_names)



# --------------
#Code starts here
fig, (ax_1, ax_2 , ax_3) = plt.subplots(1,3)
data['Intelligence'].plot(kind='box', stacked=True, ax=ax_1)
ax_1.set_title('Intelligence')
data['Speed'].plot(kind='box', stacked=True, ax=ax_2)
ax_2.set_title('Speed')
data['Power'].plot(kind='box', stacked=True, ax=ax_3)
ax_3.set_title('Power')
plt.show()


