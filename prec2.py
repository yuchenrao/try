#!/usr/bin/python
#!/usr/bin/env python

# 1 is on and 0 is off

import sys

#print sys.argv

# list1 = []

'''def try1():
    list1 = []
    for i in range(num_lights):
        list1.append(1)
    return'''

num_lights = int(sys.argv[-1])
print "Number of lights = ", num_lights

list1 = [1]*num_lights
print list1


def process_lights():
    for n in range(2, num_lights+1):
        for i in range(len(list1)):
            if (i+1) % n == 0:
                if list1[i] == 0:
                    list1[i] = 1
                elif list1[i] == 1:
                    list1[i] = 0
    return list1

list1 = process_lights()
print list1

for l in range(len(list1)):
    list2 = []
    if list1[l] == 1:
        print 'a'
        print l
        list2.append(l+1)
print list2
# Why no list2?
