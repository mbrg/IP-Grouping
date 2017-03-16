# IP-Grouping

A Python implementation of the IP-Grouping algorithm.

Usage example:
```
from IpGrouping import FindMinCover
ips = ('10.0.0.3','10.0.0.5','10.0.0.6','10.0.0.7')
L=4  # maximum number of binary intervals
S=8  # maximum length of a binary interval
cover = FindMinCover(ips, L, S)

for i in cover: print(i)
# 10.0.0.6/31
# 10.0.0.5/32
# 10.0.0.3/32
```
