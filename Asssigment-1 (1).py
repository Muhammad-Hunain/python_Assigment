#!/usr/bin/env python
# coding: utf-8

# In[22]:


print("Twinkle,twinkle,little star,\n         How I wonder What you are!\n         up above the world so high\nlike a daimond in the sky\nTwinkle,twinkle,little star,\n         How I wonder What you are! ");


# In[63]:


import sys
version = sys.version
print(version)


# In[64]:


from datetime import datetime
now = datetime.now()
print(now)


# In[61]:


Radius = input("Entert The radius");
convertRadius = int(Radius)
Pie = 3.142;
area_of_circle = Pie*(convertRadius * convertRadius);
print(area_of_circle)


# In[62]:


val1  = input("Enter the Number one")
convertval1 = int(val1)
val2  = input("Enter the Number two")
convertval2 = int(val2)

print(convertval1 + convertval2)


# In[91]:


fName = input("Enter First Name")
lName = input("Enter Last Name")
txt = fName[::-1] + " " +lName[::-1];
print(txt)

