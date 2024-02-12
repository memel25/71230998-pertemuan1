#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y,'b',x,z,'r')
plt.xlabel('Radians');
plt.ylabel('Value');
plt.title('Plotting Demonstration')
plt.legend(['Sin','Cos'])
plt.grid()


# In[5]:


hrg_dulu = 650000
hrg_skrg = 658000
gram = 25

hrga_beligram = gram * hrg_dulu
hrga_jualgram = gram * hrg_skrg
untung_rupiah = hrga_jualgram - hrga_beligram
print("keuntungan : Rp.", untung_rupiah)

untung_persen = (untung_rupiah / hrga_jualgram) * 100
print("keuntungan : ", untung_persen, "%")

belilagi = 15
gram = gram + belilagi
beli_emaslagi = belilagi * hrg_skrg
hrga_beligram = hrga_beligram + beli_emaslagi
hrg_skrg = 715000
hrga_jualgram = gram * hrg_skrg
untung_rupiah = hrga_jualgram - hrga_beligram
print("keuntungan : Rp.", untung_rupiah)

untung_persen =(untung_rupiah / hrga_jualgram) * 100
print("keuntungan : ", untung_persen, "%")


# In[ ]:


u_awal = 200000000
u_minim = 400000000
b = 0.1
tahun = 0
n = 1
while u_awal <= u_minim:
    u_awal = u_awal * (1*b/n)
    tahun += 1
    print("Uang Erika setelah", tahun, "tahun yaitu Rp", round(u_awal))

print("Untuk mencapai minimal Rp 400.000.000, erika membutuhkan", Tahun, "tahun")


# In[ ]:




