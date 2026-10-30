import pandas as pd 
import matplotlib.pyplot as plt
Student_data={
  'Name':['Muhammed','Yusuf','Ail'],
  'Age':[18,18,18],
  'Math':[77,88,99],
  'Physics':[99,88,77],
  'Chemistry':[77,99,66]

}
df=pd.DataFrame(Student_data)
print(df.head())
#حساب المتوسط والانحراف المعياري للمواد فقط
subjects=['Math','Physics','Chemistry']
means=df[subjects].mean()
stds=df[subjects].std()
print("Arithmetic mean for each subject= ")
print(means)
print('\n Standard deviation for each subject =')
print(stds)
#الرسم البياني
colors=('red','green','yellow')
plt.figure(figsize=(8,4))
bars=plt.bar(subjects,means,yerr=stds,color=colors,width=0.5)
#اضافة قيمة فوق كل عمودتلقائيا
plt.bar_label(bars,padding=3)
plt.title('Student data',fontsize=20)
plt.xlabel('The names of the subjects')
plt.ylabel('Average arithmetic for a students grades')
plt.grid(True)
plt.show()