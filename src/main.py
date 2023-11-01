import remap
from remap import ChangeZone
from sys import argv
from tqdm import tqdm
import arg_parser
import data

# TODO : get the with a command line input

folder = '/home/elverton/remap_project/run/output/eno8303_100_local'

args = arg_parser.get_args()

route_list = data.get_from_folder(args.path_folder)
route_groups = data.get_groups(route_list, lambda x: f"{x.src} {x.dst}")
samples = data.get_samples(route_groups)
remapper = remap.Remapper('/home/giancarlo/remaprt/src/remaproute',
                          net_iface = args.iface,
                          log_file = args.log_file)

# Preparing output files
table_addhops = open('/home/giancarlo/remap_test/data/table_addhops.csv',"w+")
table_changezones = open('data/table_changezones.csv',"w+")
table_hops_measured = open('data/table_hops_measured.csv',"w+")

probcost_radii = open('/home/giancarlo/remap_test/data/probcost_radii.csv',"w+")
probcost_radii.write("min,max,avg\n")

table_probcost = open('/home/giancarlo/remap_test/data/table_probcost.csv',"w+")
table_probcost.write("local,complete\n")

table_addhops.write("abs,frac\n")
table_changezones.write("zone_count\n")
table_hops_measured.write("path_len,local,complete\n")

# O problema é que estou considerando as change zones de forma errada
# Não posso somar as sondas de cada uma 

for sample in tqdm(samples):
    zone_list = ChangeZone.from_sample(sample)
    if not zone_list: continue

    zone_len_sum = 0
    zone_prob_sum = 0
    prob_cost_min = float('inf')
    prob_cost_max = float('-inf')
    radii_probcost_sum = 0
    nradii = 0
    zone_hops = set()

    cmd = str
    first = True
    for zone in zone_list:
        arg_list = zone.to_args()

        for arg in arg_list:
            output,cmd = remapper.remap(arg)
            try: output = output.split(' ')
            except: continue
            if len(output) != 7: continue
            
            prob_number = int(output[0])
            added_hops = int(output[5])
            path_length = int(output[6])

            if prob_number == 6:
                continue
            
            table_addhops.write("%d,%f\n"%(added_hops, added_hops/path_length))

            if first: 
                zone_prob_sum += prob_number
                first = False
            
            prob_cost_min = min(prob_cost_min, prob_number)
            prob_cost_max = max(prob_cost_max, prob_number)
            radii_probcost_sum += prob_number
            nradii += 1
        
        zone_len_sum += len(zone)
        zone_hops |= set(range(zone.start,zone.end))
        if -1 in zone_hops: zone_hops.remove(-1)

    if nradii > 0:
        probcost_radii.write("%.0f,%.0f,%f\n" % (
            prob_cost_min, 
            prob_cost_max,
            radii_probcost_sum / nradii
        ))
        table_probcost.write("%.0f,%.0f\n" % (
            radii_probcost_sum / nradii,
            sample[1].metadata.nprobes
        ))

    table_changezones.write("%d\n"%(len(zone_list)))
    table_hops_measured.write("%d,%d,%d\n"% \
        (len(sample[1]),len(zone_hops),len(sample[1])))

# Closing output files
table_addhops.close()
table_probcost.close()
