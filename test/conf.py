#!/usr/bin/env python

import sys, os, time
from cothread.catools import caget, caput

TEST_CONF_VERSION = 1

# set up directories
if not 'HLA_ROOT' in os.environ:
    #rt,ext = os.path.splitext(os.path.realpath(sys.argv[0]))
    rt,ext = os.path.splitext(os.path.realpath(__file__))
    HLA_ROOT = os.path.split(os.path.split(rt)[0])[0]
    os.environ['HLA_ROOT'] = HLA_ROOT
else:
    HLA_ROOT = os.environ['HLA_ROOT']
    
print "= HLA root directory: ", HLA_ROOT
sys.path.append(os.path.join(HLA_ROOT, 'src'))
sys.path.append(os.path.join(HLA_ROOT, 'src', 'hla'))
sys.path.append(os.path.join(HLA_ROOT, 'test'))

__RT=os.environ['HLA_ROOT']

HLAPKL  = os.path.join(__RT, 'machine', 'nsls2', 'hla.pkl')
CFAPKL  = os.path.join(__RT, 'machine', 'nsls2', 'chanfinder.pkl')
LATCONF = os.path.join(__RT, 'machine', 'nsls2', 'lat_conf_table.txt')

ORMX = os.path.join(__RT, 'machine', 'nsls2', 'ormx.pkl')
ORMY = os.path.join(__RT, 'machine', 'nsls2', 'ormy.pkl')
ORM_PKL = os.path.join(__RT, 'machine', 'nsls2', 'orm.pkl')

def wait_for_svr(val = [0], newval = 2):
    wt = 0
    while True:
        if caget('SVR:LOCKED') in val:
            caput('SVR:LOCKED', newval, wait=True)
            if wt > 0: print ''
            break
        if wt == 0: sys.stdout.write("\nWaiting for SVR:LOCKED released ")
        else: sys.stdout.write('.'),
        sys.stdout.flush()
        wt = wt + 1
        time.sleep(30)
    pass

def reset_svr(val = 0):
    caput('SVR:LOCKED', val, wait=True)


def hg_parent_rev():
    import commands
    stat, out = commands.getstatusoutput("hg summary")
    if stat == 0:
        for s in out.split('\n'):
            if s[:7] == 'parent:':
                return int(s.split(":")[1])
    return 0