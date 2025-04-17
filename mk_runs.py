#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2022S1MSIP1mmCommissioning"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["mwc349a"] = [95961, 95965, ]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1['mwc349a']   = "pix_list=0,1,2,3 dv=50 dw=100"

#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2['mwc349a']   = "pix_list=0,2 bank=0"

#        common parameters per source on subsequent runs (run1c, run2c), e.g. bank=1 for WARES
pars3 = {}
pars3['mwc349a']   = "pix_list=1,3 bank=1"

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
