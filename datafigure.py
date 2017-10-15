import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json


#file = 'Code/user_study.json'
df = pd.read_json('user_study.json')
user_id = df['user_id'].head(10)
x =[]
y = []
for userid in user_id:
    minute = df[df['user_id'] == userid]['minutes'].sum()
    id = str(userid)
    y.append(minute)
    x.append(id)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set_title('StudyData')
ax.set_xlabel('User ID')
ax.set_ylabel('Study Time')
ax.plot(x,y)
plt.show()

