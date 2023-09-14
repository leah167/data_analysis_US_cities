import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns
'''

Using the US_Cities.delimited.txt file and Pandas
1) Clean the data
2) Create a separate column for cites and states
3) Count how many cites have Republican and how many have Democrat Mayors
4) Which city has the highest budget and which has the lowest budget?
5) Create a column called ‘Budget per capita’, Which calculates how many dollars per person the city has.
6) return which cities have the lowest and highest Budget per capita

'''

df = pd.read_csv('/Users/leahsanchez/Workspace/intro_to_python/US_Cities_delimited.txt', delimiter='|')
df = pd.DataFrame(df)
print('Before cleaning:')
print(df)
# 1) Clean the data
print(df.dtypes)
df = df.set_index('Order')
print('Set Order as Index: ')
print(df)
df['Population'] = df['Population'].apply(lambda x: int(x.replace(",", '')))
df['Budget'] = [x[1::] for x in df['Budget']]
df['Budget'] = df['Budget'].apply(lambda x: int(x.replace(",", '')))
print('After cleaning:')
print(df)
print(df.dtypes)

# 2) Create a separate column for cites and states
split_cities = df['State_City'].str.split(',')
print('Split:')
print(split_cities)
df['City'] = split_cities.str[0] 
df['State'] = split_cities.str[1]
df.pop('State_City')
df=df[['City', 'State', 'Population', 'Budget', 'Mayor', 'Begin_Term', 'End_Term', 'Govern_Type', 'foo1', 'foo2']]
print('Part 2 completed: ')
print(df)

# 3) Count how many cites have Republican and how many have Democrat Mayors
df['Mayor'] = df['Mayor']
split_mayor = df['Mayor'].str.split()
print(split_mayor)
df['Party'] = split_mayor.str[-1]
df['Party'] = df['Party'].apply(lambda x: x.replace('(', ''))
df['Party'] = df['Party'].apply(lambda x: x.replace(')', ''))
print(df['Party'])
print(df['Party'].value_counts())
print('Number of cities with Republican Mayors: ')
print(df['Party'].value_counts().R)
print('Number of cities with Democrat Mayors: ')
print(df['Party'].value_counts().D)

# 4) Which city has the highest budget and which has the lowest budget?
# print(df.groupby(['Budget'])['City'].max()) --- Gives ascending list of budgets per city
# max_budget = df.loc[df['Budget'].idxmax()] --- Gives all associated row values for the max value in Budget
print('City with the highest budget: ')
df1=df[['City', 'Budget']][df['Budget'] == df['Budget'].max()]
print(df1)
print('City with the lowest budget: ')
df2=df[['City', 'Budget']][df['Budget'] == df['Budget'].min()]
print(df2)


# 5) Create a column called ‘Budget per capita’, Which calculates how many dollars per person the city has.
df['Budget per capita'] = (df['Budget'] / df['Population']).round(2)
print(df['Budget per capita'])
print('Part 5 completed: ')
print(df)

# 6) return which cities have the lowest and highest Budget per capita
print('City with the highest budget per capita: ')
df3=df[['City', 'Budget per capita']][df['Budget per capita'] == df['Budget per capita'].max()]
print(df3)
print('City with the lowest budget per capita: ')
df4=df[['City', 'Budget per capita']][df['Budget per capita'] == df['Budget per capita'].min()]
print(df4)

# Plot budget per city as a portion of the state (this will require some sorting) as a pie chart or otherwise
    # sort data frame by state
    # is unique
print(df['State'].value_counts())

df = df.set_index('City')

for i, state in enumerate(df['State'].unique(), 1):
    df[df['State']==state].plot(kind='pie', x='City', y='Budget', title=state)
    
plt.show()

# Plot proportions of Democrats vs Republicans as a pie chart.
Dem = df['Party'].value_counts().D
Repub = df['Party'].value_counts().R
lable = ['Democrat', 'Republican']
nums = [Dem, Repub]

fig, ax = plt.subplots()
ax.pie(nums, labels=lable)
plt.title('Proportions of Democrats v Republicans')

plt.show()





# # states are the first element in l
# titles = [l[1] for l in lst]

# labels = [l[0] for l in lst]
# # values = [l[3] for l in lst]
# cols = math.ceil(len(df['State'].value_counts()) / 4)
# rows = 4
# fig, axs = plt.subplots(nrows=rows, ncols=cols)

# lst = list(df.groupby('State'))
# print(lst)

# for i, l in enumerate(lst):
#     # basic math to get col and row
#     row = i // cols + 1
#     col = i % (rows + 1) + 1
#     d = l[0]
#     axs[i].plot.pie(d['Budget'], labels=labels, title=titles)
   
# data = df[df['State']==state] # filter by state
    # plt.subplot(1, 2, i)  # rows, columns, i: plot index beginning at 1
    # plt.pie(x='City', y='Budget', data=data)
    # plt.title(state)



# fig = plt.figure(figsize =(10, 7))
# plt.pie(x=lables,  data=nums, labels=lables)
# df.groupby(['Party']).sum().plot(kind='pie', y=df['Party'].value_counts())

