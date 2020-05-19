#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 11:24:30 2020

@author: rkdommata
task2: open file and calc results 
"""
def calc(opertype, num1,num2):
    print(opertype)
    print(num1)
    print(num2)
    if opertype=='*':
        return num1 * num2
    elif opertype=='+':
        return num1+num2
    elif opertype=='-':
        return num1-num2
    elif opertype=='/':
        return num1/num2
    
with open("inputcalc.txt",'r') as f:
    input_calc=f.read().splitlines()
sum=0

for line in input_calc:
    line_split=line.split()
    sum+=calc(line_split[1], int(line_split[2]), int(line_split[3]))
    
print(sum)



