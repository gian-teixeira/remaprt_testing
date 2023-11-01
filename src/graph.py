import plot
import pandas as pd
import numpy as np
from data import gen_cdf as CDF

# PROBCOST - local ========== #

prob_cost = pd.read_csv('/home/giancarlo/remap_test/data/probcost_radii.csv')

plot.plot_cdf(cdf_list = [CDF(prob_cost['avg']), 
                          CDF(prob_cost['min']), 
                          CDF(prob_cost['max'])],
              label = ['Average','Minimum','Maximum'],
              filename = './graphs/probcost_local.png',
              xlabel = 'Probing Cost')

# PROBCOST - local x complete ========== #

# Os valores do remaprt estão normais, mas os valores obtidos pela saída
# do fastmda são consideravelmente grandes em determinados casos
#   TODO : um histograma com as faixas de valores de cada remapeador

# ADDED HOPS ========== #

addhops = pd.read_csv('/home/giancarlo/remap_test/data/table_addhops.csv')

plot.plot_cdf(cdf_list = [CDF(addhops['abs'])],
              label = [None],
              filename = './graphs/addhops_abs.png',
              xlabel = 'Number of added hops')

plot.plot_cdf(cdf_list = [CDF(addhops['frac'])],
              label = [None],
              filename = './graphs/addhops_frac.png',
              xlabel = 'Fraction of added hops')

# ========== #

prob_cost_comp = pd.read_csv('/home/giancarlo/remap_test/data/table_probcost.csv')

plot.plot_cdf(cdf_list = [CDF(prob_cost['avg']), CDF(prob_cost_comp['complete'])],
              label = ['Local remapping', 'Complete remapping'],
              filename = './graphs/probcost_compare.png',
              xlabel = 'Probing cost ')

# CHANGE ZONE ========== #

zone = pd.read_csv('/home/giancarlo/remap_test/data/table_changezones.csv')

plot.plot_cdf(cdf_list = [CDF(zone['zone_count'])],
              label = [None],
              filename = './graphs/zonecount.png',
              xlabel = 'Number of local change zones')

# HOPS MEASURED ========== #

hm = pd.read_csv('/home/giancarlo/remap_test/data/table_hops_measured.csv')
hm_short = hm.loc[hm['path_len'] < 10]
hm_long = hm.loc[hm['path_len'] > 20]

rate = lambda df : (df['complete'] - df['local']) / df['complete']
hm_rate = rate(hm)
hm_short_rate = rate(hm_short)
hm_long_rate = rate(hm_long)

plot.plot_cdf(cdf_list = [CDF(hm['local']), CDF(hm['complete'])],
              label = ['Local remapping', 'Complete remapping'],
              filename = './graphs/hop_measured.png',
              xlabel = 'Number of hops measured')

plot.plot_cdf(cdf_list = [CDF(hm_rate*100), CDF(hm_short_rate*100), CDF(hm_long_rate*100)],
              label = ['All paths', 'Short paths', 'Long paths'],
              filename = './graphs/hop_measured_rel.png',
              xlabel = 'Probing cost savings (%)',
              legend_loc = 2)