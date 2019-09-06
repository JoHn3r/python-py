#!/usr/bin/env python

import yaml


mydata = yaml.safe_load(open("list.yml"))

for i in mydata:
    t = 0
    while t <= len(mydata[i]) - 1:
        print(i)
        print("contains: ")
        print(mydata[i][t])
        t += 1
    