from itertools import combinations
from route.route import Route
import subprocess
import os
import util
import typing as tp

def hopsstr(route : Route) -> str:
    hops = list()
    for hop in route.hops:
       ifaces = [iface.__str__() for iface in hop]
       hops.append(";".join(ifaces))
    return "|".join(hops)
# ===== #

class ChangeZone:
    def __init__(self, old_route, new_route, start, end):
        self.start = start
        self.end = end
        self.base_args = (["-d", str(new_route.dst),
                           "-o", hopsstr(old_route),
                           "-n", hopsstr(new_route)])
    
    def __len__(self):
        return self.end - self.start + 1
    
    def to_args(self):
        arg_list = []
        for hop in range(self.start,self.end):
            arg_list.append(self.base_args + ["-t", str(hop+1)])
        return arg_list

    @staticmethod
    def from_sample(sample_pair):
        old_route, new_route = sample_pair
        diffs = Route.diff(old_route,new_route)
        if len(diffs) < 1: return None

        zone_list = []
        for d in diffs:
            zone_list.append(ChangeZone(old_route,new_route,d.i2,d.j2))
        
        return zone_list


def to_args(sample_pair : tp.Tuple[Route,Route]) -> tp.List[Route]:
    ''' Returns a list of lists. Each child lists contains
        arguments to initiate a remap at each hop of the 
        corresponding divergent range between old_route and
        new_route. 
        
        If there is no difference between the routes, 
        returns None. '''
    old_route, new_route = sample_pair
    diffs = Route.diff(old_route,new_route)
    if len(diffs) < 1: return None,None

    base_args = (["-d", str(new_route.dst),
                  "-o", hopsstr(old_route),
                  "-n", hopsstr(new_route)])
    arg_list = []

    change_zone_hop_count = 0
    for d in diffs:
        change_zone_hop_count += d.j2 - d.i2 + 1
        mid = (d.i2+d.j2)+1
        arg_list.append(base_args + ["-t", str(mid)])

    return arg_list, change_zone_hop_count

    '''
    arg_list_all = list()

    change_zone_hop_count = 0
    for d in diffs:
        arg_list_cur = list()
        change_zone_hop_count += d.j2 - d.i2 + 1
        for hop in range(d.i2, d.j2+1):
            arg_list_cur.append(base_args + ["-t", str(hop)])
        arg_list_all.append(arg_list_cur)

    return arg_list_all, change_zone_hop_count
    '''
# ===== #

def get_samples(route_groups : tp.Dict[str,tp.List[Route]]
                ) -> tp.List[tp.Tuple[Route,Route]]:
    ''' Returns a list of pairs (old_route, new_route) that
        can be used to initiate a remap process. '''
    samples = list()
    for group in route_groups.values():
        if len(group) < 2: continue
        for pair in combinations(group,2):
            samples.append(pair)
    return samples
# ===== #

class Remapper:
    def __init__(self, exec_path, net_iface, log_file):
        self.base_args = ([
            "sudo", exec_path, 
            "-i", net_iface,
            "-x", str(10),
            "-l", log_file
        ])
    # ===== #

    def remap(self, sample_args):
        cmd = self.base_args + sample_args
        process = subprocess.run(cmd, stdout = subprocess.PIPE)
        if process.returncode : return None, None
        return process.stdout.decode().rstrip(), ' '.join(cmd)
    # ===== #
# ===== #
