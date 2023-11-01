from collections import defaultdict
from route.route import Route
import csv
import os

def get_from_file(file_path):
    file_name = file_path.split('/')[-1]
    if not 'paths' in file_name:
        raise Exception(f"File does not contain paths : {file_path}")
    route_list = list()
    with open(file_path,"r") as file:
        for line in file: route_list.append(Route(line))
    return route_list
# ===== #

def get_from_folder(folder_path, file_limit = None):
    route_list = list()
    for file_name in os.listdir(folder_path)[:file_limit]:
        file_path = f"{folder_path}/{file_name}"
        try: route_list += get_from_file(file_path)
        except Exception as e: print(str(e))
    return route_list
# ===== #

def get_timestamp(route):
    return route.metadata.logging_tstamp
# ===== #

def get_groups(item_list,group_function):
    groups = defaultdict(lambda: list())
    for item in item_list: groups[group_function(item)].append(item)
    for key in groups: 
        groups[key] = sorted(groups[key], key = get_timestamp)
    return dict(groups)
# ===== #

def get_samples(route_groups):
    ''' Returns a list of pairs (old_route, new_route) that
        can be used to initiate a remap process. '''
    samples = list()
    for group in route_groups.values():
        if len(group) < 2: continue
        for pair in zip(group,group[1:]):
            samples.append(pair)
        print(' ')
    return samples
# ===== #

def to_args(sample_pair):
    ''' Returns a list of lists. Each child lists contains
        arguments to initiate a remap at each hop of the 
        corresponding divergent range between old_route and
        new_route. 

        If there is no difference between the routes, 
        returns None. '''
    old_route, new_route = sample_pair
    diffs = Route.diff(old_route,new_route)
    if len(diffs) < 1: return None

    base_args = (["-d", str(new_route.dst),
                "-o", old_route.hopsstr,
                "-n", new_route.hopsstr])
    arg_list_all = list()

    for d in diffs:
        arg_list_cur = list()
        for hop in range(d.i2, d.j2+1):
            arg_list_cur.append(base_args + ["-t", str(hop)])
        arg_list_all.append(arg_list_cur)

    return arg_list_all
# ===== #

def csv_get_cols(file_path):
    cols = None
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        cols = { key : list() for key in header }
        for row in reader:
            for i,value in enumerate(row):
                cols[header[i]].append(value)
    return cols
# ===== #

def gen_cdf(elements):
    cdf_dict = defaultdict(lambda : 0)
    for e in elements: cdf_dict[float(e)] += 1
    for key in cdf_dict: cdf_dict[key] /= len(elements)
    sorted_pairs = [list(t) for t in sorted(cdf_dict.items())]
    for i in range(1,len(sorted_pairs)):
        sorted_pairs[i][1] += sorted_pairs[i-1][1]
    return dict(sorted_pairs)
# ===== #

def cdf_to_file(cdf_dict, file_path):
    with open(file_path, 'w+') as file:
        for value in cdf_dict:
            file.write(f'{value} {cdf_dict[value]}\n')
# ===== #

def cdf_from_file(file_path):
    cdf_dict = dict()
    with open(file_path, 'w+') as file:
        for line in file:
            key,value = line.split()
            cdf_dict[key] = value
    return cdf_dict
# ===== #