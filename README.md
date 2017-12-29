# IP-Grouping algorithm

A Python implementation of the IP-Grouping algorithm for IPv4, as decribed in *Michael Bargury, Roy Levin and Royi Ronen, Learning to Customize Network Security Rules, [arXiv:1712.09795 [cs.CR, cs.LG]](https://arxiv.org/abs/1712.09795).*

A usage example:
```python
from IpGrouping import FindMinCover

ips = ('10.0.0.3','10.0.0.5','10.0.0.6','10.0.0.7')
L=4  # maximum number of binary intervals
S=8  # maximum length of a binary interval

# run the algorithm
cover = FindMinCover(ips, L, S)

for i in cover: print(i)
# 10.0.0.6/31
# 10.0.0.5/32
# 10.0.0.3/32
```
