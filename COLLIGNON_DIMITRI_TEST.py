#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
variable = pd.read_csv(r"/home/jovyan/mower_market_snapshot.csv", delimiter=";")
variable.head()

#Question 1
# In[23]:


import pandas as pd
variable = pd.read_csv(r"/home/jovyan/mower_market_snapshot.csv", delimiter=";")
variable.head(1400)


# In[24]:


import pandas as pd
variable = pd.read_csv(r"/home/jovyan/mower_market_snapshot.csv", delimiter=";")
variable

#Question 2
# In[33]:


variable.sort_values("capacity")


# In[34]:


variable.sort_values(by='capacity', ascending=False).head()


# In[35]:


variable.sort_values(by='capacity', ascending=True).head()


# In[36]:


variable.sort_values(by='capacity', ascending=True)


# In[37]:


variable.loc[0, :]


# In[40]:


variable.loc[:, "capacity" : "id"]


# In[41]:


variable.loc[:, "capacity" : "price"]


# In[42]:


variable.loc[0, "capacity" : "price"]


# In[43]:


variable.loc[10, "capacity" : "price"]


# In[44]:


variable


# In[47]:


variable.loc[variable.quality=='Low',:]


# In[53]:


variable.iloc[:, 0:5].head(10)


# In[55]:


variable.loc[:, "capacity" : "price"].head(10)


# In[71]:


variable.loc[:, "prod_cost"]


# In[72]:


variable.iloc[:, 5]


# In[78]:


variable.iloc[:, 5]


# In[82]:


variable.iloc[:, 5]


# In[91]:


variable.loc[variable.prod_cost=='0',:]

#Question 3
# In[92]:


variable.loc[variable.prod_cost=='-64',:]


# In[102]:


variable.groupby(['prod_cost']).mean()


# In[106]:


variable.groupby(['prod_cost']).mean()


# In[4]:


import pandas as pd
variable = pd.read_csv(r"/home/jovyan/mower_market_snapshot.csv", delimiter=";")
variable

#Question 4
# In[6]:


variable.isnull().sum()


# In[9]:


variable.loc[:, "prod_cost"]


# In[13]:


import pandas as pd
import numpy as np
variable = pd.read_csv(r"/home/jovyan/mower_market_snapshot.csv", delimiter=";")
variable


# In[21]:


variable.loc[0,"prod_cost"]

#Question 5
# In[37]:


moy = 0.0
cost = pd.to_numeric(variable.loc[:,'prod_cost'], errors='coerce')
cost = cost.replace(np.nan, 0, regex=True)

for i in cost:
    moy +=i
    
moy = moy / 1400


# In[115]:


variable.loc[:, "prod_cost"] = variable.loc[:, "prod_cost"].replace(np.nan, moy, regex=True)
variable.loc[:, "prod_cost"]


# In[113]:


variable['warranty'].unique()


# In[111]:


variable.loc[:, "warranty"]


# In[60]:


variable['warranty'].replace(['3ans','3 ans.','3_ans','3 anss','3ans.', '3 ans', '3_ans.','3_anss', '3anss'],'3', inplace=True)
variable['warranty'].replace(['2 ans', '2 anss', '2anss', '2_ans', '2ans','2_ans.', '2 ans.', '2_anss', '2ans.'],'2', inplace=True)
variable['warranty'].replace(['1 an', '1an', '1_an.','1ans', '1an.', '1_ans', '1_an', '1 an.', '1 ans'],'1', inplace=True)
variable.loc[:, "warranty"]


# In[64]:


variable = pd.read_csv(r"/home/jovyan/mower_market_snapshot.csv", delimiter=";")
variable


# In[72]:


for length in variable.price:
    if length >= 0 and length <= 300:
        variable['price'].replace(length,"0-300", inplace=True)
    elif length > 300 and length <= 500:
        variable['price'].replace(length,"301-500", inplace=True)
    elif length > 501:
        variable['price'].replace(length,"501-++", inplace=True)


# In[73]:


variable['price']


# In[74]:


variable


# In[75]:


variable['product_type'].unique()


# In[78]:


variable


# In[83]:


variable = pd.read_csv(r"/home/jovyan/mower_market_snapshot.csv", delimiter=";")


# In[84]:


variable


# In[85]:


prodtype= variable['product_type'].unique()

for i in range(len(prodtype)):
    variable.loc[:,'product_type'] = variable.loc[:,'product_type'].replace(prodtype[i], (i+1), inplace=True)

variable['product_type'].unique()


# In[86]:


variable


# In[87]:


variable.isnull().sum()


# In[88]:


variable = pd.read_csv(r"/home/jovyan/mower_market_snapshot.csv", delimiter=";")


# In[89]:


variable


# In[90]:


prodtype= variable['product_type'].unique()

for i in range(len(prodtype)):
    variable.loc[:,'product_type'] = variable.loc[:,'product_type'].replace(prodtype[i], (i+1), regex=True)

variable['product_type'].unique()


# In[91]:


variable['product_type']


# In[92]:


variable


# In[93]:


variable.insert(7, "auto-portee",0, allow_duplicates=False)
variable.insert(8, "electrique", 0, allow_duplicates=False)
variable.insert(9, "essence", 0, allow_duplicates=False)


# In[94]:


variable


# In[96]:


variable = pd.read_csv(r"/home/jovyan/mower_market_snapshot.csv", delimiter=";")


# In[97]:


variable.insert(7, "auto-portee",0, allow_duplicates=False)
variable.insert(8, "electrique", 0, allow_duplicates=False)
variable.insert(9, "essence", 0, allow_duplicates=False)


# In[98]:


variable


# In[99]:


variable = pd.read_csv(r"/home/jovyan/mower_market_snapshot.csv", delimiter=";")


# In[101]:


prodtype= variable['product_type'].unique()

for i in range(len(prodtype)):
    variable.loc[:,'product_type'] = variable.loc[:,'product_type'].replace(prodtype[i], (i+1), regex=True)


# In[102]:


variable


# In[103]:


variable.insert(7, "auto-portee",0, allow_duplicates=False)
variable.insert(8, "electrique", 0, allow_duplicates=False)
variable.insert(9, "essence", 0, allow_duplicates=False)


# In[104]:


variable


# In[108]:


tab = variable.loc[:,'product_type']
for i in range(len(variable.loc[:,'product_type'])):
    if tab[i] == 1:
        variable.loc[:,'auto-portee'][i] = 1
    elif tab[i] == 2:
        variable.loc[:,'electrique'][i] = 1
    elif tab[i] == 3:
        variable.loc[:,'essence'][i] = 1


# In[107]:


variable


# In[116]:


variable = pd.read_csv(r"/home/jovyan/mower_market_snapshot.csv", delimiter=";")
variable

#Question 5
# In[118]:


moy = 0.0
cost = pd.to_numeric(variable.loc[:,'prod_cost'], errors='coerce')
cost = cost.replace(np.nan, 0, regex=True)

for i in cost:
    moy +=i
    
moy = moy / 1400

variable.loc[:, "prod_cost"] = variable.loc[:, "prod_cost"].replace(np.nan, moy, regex=True)
variable.loc[:, "prod_cost"]
variable

#Question 6
# In[119]:


variable['warranty'].unique()
variable.loc[:, "warranty"]

#Question 7-8
# In[120]:


variable['warranty'].replace(['3ans','3 ans.','3_ans','3 anss','3ans.', '3 ans', '3_ans.','3_anss', '3anss'],'3', inplace=True)
variable['warranty'].replace(['2 ans', '2 anss', '2anss', '2_ans', '2ans','2_ans.', '2 ans.', '2_anss', '2ans.'],'2', inplace=True)
variable['warranty'].replace(['1 an', '1an', '1_an.','1ans', '1an.', '1_ans', '1_an', '1 an.', '1 ans'],'1', inplace=True)
variable

#Question 9
# In[121]:


for length in variable.price:
    if length >= 0 and length <= 300:
        variable['price'].replace(length,"0-300", inplace=True)
    elif length > 300 and length <= 500:
        variable['price'].replace(length,"301-500", inplace=True)
    elif length > 501:
        variable['price'].replace(length,"501-++", inplace=True)
variable

#Question 10
# In[122]:


variable['product_type'].unique()


# In[124]:


prodtype= variable['product_type'].unique()

for i in range(len(prodtype)):
    variable.loc[:,'product_type'] = variable.loc[:,'product_type'].replace(prodtype[i], (i+1), regex=True)

variable

#Question 11
# In[125]:


variable.insert(7, "auto-portee",0, allow_duplicates=False)
variable.insert(8, "electrique", 0, allow_duplicates=False)
variable.insert(9, "essence", 0, allow_duplicates=False)
variable


# In[127]:


tab = variable.loc[:,'product_type']
for i in range(len(variable.loc[:,'product_type'])):
    if tab[i] == 1:
        variable.loc[:,'auto-portee'][i] = 1
    elif tab[i] == 2:
        variable.loc[:,'electrique'][i] = 1
    elif tab[i] == 3:
        variable.loc[:,'essence'][i] = 1
variable

/*-------------------------------------------------------------*\
\*------------------    Tableau Final     ---------------------*/
\*-------------------------------------------------------------*/
# In[128]:


variable


# In[129]:


def ReadCSV():
    return pd.read_csv(r"/home/jovyan/mower_market_snapshot.csv", delimiter=";")

ReadCSV()


# In[142]:


def Auditprodcost(variable, value):
    
    return var.loc[variable.prod_cost==value,:]
    
display(Auditprodcost(variable, '-64'))
display(Auditprodcost(variable, '0'))


# In[143]:


def Sommenull(variable):
    return variable.isnull().sum()

Sommenull(variable)


# In[146]:


def Moyenneprodcost(variable):
    moy = 0.0
    cost = pd.to_numeric(variable.loc[:,'prod_cost'], errors='coerce')
    cost = cost.replace(np.nan, 0, regex=True)
    for i in cost:
        moy +=i
    
    moy = moy / 1400
    return variable
    
Moyenneprodcost(variable)


# In[148]:


def Uniquewarranty(variable):
   return variable['warranty'].unique()
Uniquewarranty(variable)


# In[149]:


def Valwarranty(variable):
    
    variable['warranty'].replace(['3ans','3 ans.','3_ans','3 anss','3ans.', '3 ans', '3_ans.','3_anss', '3anss'],'3', inplace=True)
    variable['warranty'].replace(['2 ans', '2 anss', '2anss', '2_ans', '2ans','2_ans.', '2 ans.', '2_anss', '2ans.'],'2', inplace=True)
    variable['warranty'].replace(['1 an', '1an', '1_an.','1ans', '1an.', '1_ans', '1_an', '1 an.', '1 ans'],'1', inplace=True)
    
    return variable

Valwarranty(variable)


# In[151]:


def Pricecategorie(variable):
    for length in variable.price:
        if length >= 0 and length <= 300:
            variable['price'].replace(length,"0-300", inplace=True)
        elif length > 300 and length <= 500:
            variable['price'].replace(length,"301-500", inplace=True)
        elif length > 501:
            variable['price'].replace(length,"501-++", inplace=True)
            
        return variable

display(Pricecategorie(variable))


# In[ ]:




