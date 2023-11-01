import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('/home/giancarlo/remap_test/data/table_probcost.csv')

plt.yscale('log')
plt.hist(data['complete'], bins = 20)
plt.hist(data['local'], bins = 20, alpha = 0.5)
plt.savefig('/home/giancarlo/remap_test/teste.png')