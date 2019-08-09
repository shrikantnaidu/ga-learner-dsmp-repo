# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
p_a = len(df[df['fico']>700])/len(df['fico'])
print(p_a)
p_b = len(df[df['purpose'] == 'debt_consolidation'])/len(df['purpose'])
print(p_b)
df1=df[df['purpose'] == 'debt_consolidation']
p_a_b = (p_b*p_a)/p_a
print(p_a_b)
p_b_a = (p_a_b*p_b)/p_a
print(p_b_a)
result = p_b_a == p_a
print(result)

# code ends here


# --------------
# code starts here
prob_lp = len(df[df['paid.back.loan'] == 'Yes'])/len(df['paid.back.loan'])
print(prob_lp)
prob_cs = len(df[df['credit.policy'] == 'Yes'])/len(df['credit.policy'])
print(prob_cs)
new_df = df[df['paid.back.loan'] == 'Yes']
prob_pd_cs = new_df[new_df['credit.policy']== 'Yes'].shape[0]/new_df.shape[0]
print(prob_pd_cs)
bayes = (prob_pd_cs*prob_lp)/prob_cs
print(bayes)

# code ends here


# --------------
# code starts here
df1=df[df['paid.back.loan'] == 'No']
df2 = df1['purpose']
df2.value_counts().plot(kind='bar')
plt.show()
# code ends here


# --------------
# code starts here
inst_median = df['installment'].median()
inst_mean = df['installment'].mean()
df['installment'].hist()
df['log.annual.inc'].hist()
plt.show()




# code ends here


