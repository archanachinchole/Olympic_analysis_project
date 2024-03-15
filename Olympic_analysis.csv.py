#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


df = pd.read_csv(r'C:\\Users\\Admin\\Desktop\\OLYMPIC\\athlete_events.csv')


# In[4]:


region_df = pd.read_csv(r'C:\\Users\\Admin\\Desktop\\OLYMPIC\\noc_regions.csv')


# In[5]:


df.tail()


# In[6]:


df.shape


# In[7]:


df[df['Season']=='Summer']


# In[8]:


df.shape


# In[9]:


df.tail()


# In[10]:


region_df.tail()


# In[11]:


df=df.merge(region_df,on="NOC",how='left')
df


# In[12]:


df.tail()


# In[13]:


df['region'].unique()


# In[14]:


df['region'].unique().shape


# In[15]:


df.isnull().sum()


# In[16]:


#columns_to_delete = ['region_x', 'notes_x','region_y','notes_y']
#df = df.drop(columns=columns_to_delete)


# In[17]:


df


# In[18]:


df.isnull().sum()


# In[19]:


df.duplicated().sum()


# In[20]:


df.drop_duplicates(inplace=True)


# In[21]:


df.duplicated().sum()


# In[22]:


df['Medal'].value_counts()


# In[23]:


df=pd.concat([df,pd.get_dummies(df['Medal'])],axis=1)


# In[24]:


df.shape


# In[25]:


df.groupby('NOC').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=False).reset_index()


# In[26]:


df[(df['NOC'] == 'IND') & (df['Medal'] == 'Gold')]


# In[27]:


Medal_tally=df.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal'])


# In[28]:


Medal_tally =Medal_tally.groupby('NOC').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=False).reset_index()


# In[29]:


Medal_tally['Total'] = Medal_tally['Gold'] + Medal_tally['Silver'] + Medal_tally['Bronze']


# In[30]:


Medal_tally['Total']


# In[31]:


Medal_tally[Medal_tally['NOC'] == 'IND']


# In[32]:


years=df['Year'].unique().tolist()


# In[33]:


years.sort()


# In[34]:


years.insert(0,'overall')


# In[35]:


years


# In[36]:


country=df['region'].unique().tolist()


# In[37]:


country = np.unique(df['region'].dropna().values).tolist()


# In[38]:


country.sort()


# In[39]:


country


# In[40]:


country.insert(0,'overall')


# In[41]:


country


# In[42]:


def featch_medal_tally(df,year,country):
    Medal_df=df.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal'])
    flag = 0
    if year == 'Overall' and country == 'Overall' :
        temp_df = Medal_df 
    if year == 'Overall' and country != 'Overall' :
        flag = 1
        temp_df = Medal_df[Medal_df['region'] == 'India']
    if year != 'Overall' and country == 'Overall' :
        temp_df = Medal_df[Medal_df['Year'] == int(Year)]
    if year != 'Overall' and country != 'Overall' :
        temp_df =  Medal_df[(Medal_df['Year'] == 2016) & (Medal_df['region'] == country)]
    
    if flag == 1:
        X = temp_df.groupby('Year').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=True).reset_index()
    else:
        X = temp_df.groupby('region').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=True).reset_index()

    X['Total'] = X['Gold'] + X['Silver'] + X['Bronze']
    
    
    print(X)


# In[55]:


featch_medal_tally(df,year = 'Overall' ,country = 'India')


# In[56]:


Medal_df = df.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal'])
Medal_df


# In[57]:


Medal_df[Medal_df['region'] == 'India']


# In[58]:


Medal_df[Medal_df['Year'] == 2016]


# In[59]:


Medal_df[(Medal_df['Year'] == 2016) & (Medal_df['region'] == 'India')]


# In[60]:


df


# In[61]:


df['Year'].unique().shape


# In[62]:


df['City'].unique()


# In[63]:


df['Sport'].unique().shape


# In[64]:


df['Event'].unique().shape


# In[65]:


df['Name'].unique().shape


# In[66]:


df['region'].unique().shape


# In[67]:


df.head()


# In[68]:


df.drop_duplicates(['Year','region'])['Year'].value_counts().reset_index().sort_values('Year')


# In[69]:


Nation_over_time=df.drop_duplicates(['Year','region'])['Year'].value_counts().reset_index().sort_values('Year')
Nation_over_time.rename(columns={'index':'Editions', 'Year': 'No. of  Countries'})


# In[70]:


Nation_over_time.rename(columns={'No. of  Countries':'Year', 'count': 'No. of  Countries'})


# In[71]:


import plotly.express as px


# In[72]:


fig = px.line(Nation_over_time, x="Year", y="count")
fig.show()


# In[73]:


df.drop_duplicates(['Year','Event'])['Year'].value_counts().reset_index().sort_values('Year')


# In[74]:


x=df.drop_duplicates(['Year','Sport','Event'])


# In[75]:


import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))


# In[76]:


sns.heatmap(x.pivot_table(index='Sport',columns='Year',values='Event',aggfunc='count').fillna(0).astype('int'), annot=True)


# In[77]:


df


# In[78]:


def most_sucessful(df,sport):
    temp_df = df.dropna(subset=['Medal'])
    
    if sport != 'overall':
        temp_df = temp_df [temp_df ['Sport'] == sport]
    
    x = temp_df['Name'].value_counts().reset_index().head(15).merge(df,left_on='Name',right_on='Name',how='left')[['Name','Sport','region']].drop_duplicates('Name')
    return x
    #temp_df['Name'].value_counts().reset_index().head(15).merge(df,left_on='index',right_on='Name',how='left')[['Name','Name_x','Sport','region']]drop_duplicates('Name')


# In[79]:


most_sucessful(df,'overall')


# # Country Wise

# - Countrywise medal tally per year(line plot)
# - What countries are good at heatmap
# - Most sucessfull Athletes(Top 10)

# In[52]:


temp_df = df.dropna(subset=['Medal'])
temp_df.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal'],inplace=True)


# In[53]:


new_df=temp_df[temp_df['region'] == 'India']
final_df =  new_df.groupby('Year').count()['Medal'].reset_index()


# In[80]:


import plotly.express as px


# In[81]:


fig = px.line(final_df, x="Year", y="Medal")
fig.show()


# In[82]:


new_df=temp_df[temp_df['region'] == 'UK']
plt.figure(figsize=(20,20))
sns.heatmap(new_df.pivot_table(index='Sport',columns='Year',values='Medal', aggfunc='count').fillna(0),annot=True)


# In[83]:


def most_sucessful(df,country):
    temp_df = df.dropna(subset=['Medal'])
    
    temp_df = temp_df [temp_df ['region'] == country]
    
    x = temp_df['Name'].value_counts().reset_index().head(15).merge(df,left_on='Name',right_on='Name',how='left')[['Name','Sport','region']].drop_duplicates('Name')
    return x
    #temp_df['Name'].value_counts().reset_index().head(15).merge(df,left_on='index',right_on='Name',how='left')[['Name','Name_x','Sport','region']]drop_duplicates('Name')


# In[84]:


most_sucessful(df,'USA')


# In[85]:


get_ipython().system('pip install scipy')


# In[86]:


import plotly.figure_factory as ff


# In[88]:


athlets_df = df.drop_duplicates(subset=['Name','region'])
athlets_df


# In[93]:


fig = ff.create_distplot([athlets_df['Age'].dropna()],['Age Distribution'],show_hist=False,show_rug=False)
fig.show()


# In[100]:


x1 =athlets_df['Age'].dropna()
x2 = athlets_df.loc[athlets_df['Medal'] == 'Gold']['Age'].dropna()
x3 = athlets_df.loc[athlets_df['Medal'] == 'Silver']['Age'].dropna()
x4 = athlets_df.loc[athlets_df['Medal'] == 'Bronze']['Age'].dropna()


# In[107]:


fig = ff.create_distplot([x1,x2,x3,x4],['Overall Age','Gold Medalist','Silver Medalist','Bronze Medalist'],show_hist=False,show_rug=False)
fig.show()


# In[108]:


famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']


# In[112]:


x= []
name = []
for sport in famous_sports:
    temp_df = athlets_df[athlets_df['Sport'] == sport]
    x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
    name.append(sport)
    


# In[113]:


fig = ff.create_distplot(x,name,show_hist=False,show_rug=False)


# In[115]:


fig.show()


# In[117]:


athlets_df['Medal'].fillna('No Medal',inplace=True)


# In[126]:


plt.figure(figsize=(10,10))
temp_df = athlets_df[athlets_df['Sport'] == 'Weightlifting']
sns.scatterplot(x=temp_df['Weight'], y=temp_df['Height'],hue=temp_df['Medal'],style=temp_df['Sex'])


# In[127]:


men = athlets_df[athlets_df['Sex'] == 'M'].groupby('Year').count()['Name'].reset_index()
women = athlets_df[athlets_df['Sex'] == 'F'].groupby('Year').count()['Name'].reset_index()


# In[130]:


final =men.merge(women,on='Year',how='left')
final.rename(columns={'Name_x':'Male','Name_y':'Female'},inplace=True)


# In[132]:


final.fillna(0,inplace=True)


# In[133]:


fig = px.line(final,x='Year',y=['Male','Female'])
fig.show()


# In[ ]:




