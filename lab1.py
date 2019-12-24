#!/usr/bin/env python
# coding: utf-8

# Создадим первую выборку

# In[17]:


import pandas as pd
from IPython import get_ipython

data = pd.read_csv('Data.csv')
data = data[data['Name'] == 'Courtney Lee']
first_selection = data['FieldGoalsPercentage'][~data['FieldGoalsPercentage'].isin([0, 100])]
first_selection


# И вторую
# 

# In[24]:


second_selection = data['FieldGoalsAttempted']
second_selection


# Теперь построим вариационный ряд для первой выборки

# In[36]:


def variation_series(selection, step):
    length = len(selection)
    maximum = selection.max()
    current = 0
    series = {}
    while current < maximum:
        key = '%s - %s' % (current, current + step)
        series[key] = [len(selection[(current <= selection) & (selection < current + step)]) / length]
        current += step
    return pd.DataFrame(series)

variation_series(first_selection, 10)


# 
# И для второй

# In[37]:


variation_series(second_selection, 5)


# 
# Выборочное среднее для первой

# In[38]:


first_selection.mean()


# 
# И для второй

# In[39]:


second_selection.mean()


# Выборочная дисперсия для первой

# In[47]:


import math

def central_moment(selection, k):
    length = len(selection)
    mean = selection.mean()
    sum = 0
    for item in selection:
        sum += math.pow(item - mean, k)
    return sum / length

central_moment(first_selection, 2)


# 
# И для второй

# In[48]:


central_moment(second_selection, 2)


# 
# Исправленная дисперсия для первой

# In[49]:


def corrected_variance(selection):
    length = len(selection)
    return (length / (length - 1)) * central_moment(selection, 2)

corrected_variance(first_selection)


# 
# И для второй

# In[50]:


corrected_variance(second_selection)


# Коэффициент ассиметрии для первой

# In[51]:


def asymmetry_coefficient(selection):
    moment3 = central_moment(selection, 3)
    moment2 = central_moment(selection, 2)
    return moment3 / math.pow(moment2, 3 / 2)

asymmetry_coefficient(first_selection)


# И для второй

# In[52]:


asymmetry_coefficient(second_selection)


# Эксцесс для первой выборки

# In[53]:


def excess(selection):
    moment4 = central_moment(selection, 4)
    moment2 = central_moment(selection, 2)
    return (moment4 / math.pow(moment2, 2)) - 3

excess(first_selection)


# И для второй

# In[54]:


excess(second_selection)


# Размах первой выборки

# In[55]:


def selection_range(selection):
    return selection.max() - selection.min()

selection_range(first_selection)


# Второй

# In[56]:


selection_range(second_selection)


# Медиана первой выборки

# In[57]:


first_selection.median()


# Второй

# In[58]:


second_selection.median()


# Квартили и квантиль уровня 1/3 первой выборки

# In[66]:


print('q = 1/4; Z = %s' % first_selection.quantile(.25))
print('q = 1/2; Z = %s' % first_selection.median())
print('q = 3/4; Z = %s' % first_selection.quantile(.75))
print('q = 1/3; Z = %s' % first_selection.quantile(1/3))


# Второй

# In[67]:


print('q = 1/4; Z = %s' % second_selection.quantile(.25))
print('q = 1/2; Z = %s' % second_selection.median())
print('q = 3/4; Z = %s' % second_selection.quantile(.75))
print('q = 1/3; Z = %s' % second_selection.quantile(1/3))


# Гистограмма, полигон частот и график плотности (вероятностей) нормального закона распределения для первой выборки

# In[ ]:


import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


