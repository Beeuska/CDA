# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 18:17:02 2017

@author: harne
"""

total = 0
prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

for key in prices:
    print (key)
    print ("price: %s" % prices[key])
    print ("stock: %s" % stock[key])


for item in prices.keys():
    prices[item] *= stock[item]
    print (prices[item])
    total += prices[item]
    
print (total)