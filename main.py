#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 22:29:53 2023

@author: Adam Czerniewski


"""
import xlsxwriter
import math
import openpyxl
from simplifiedExcelUtil import ExcelUtil
from openpyxl.chart import LineChart, Reference


class linear:
    
    def __init__(self):
        
       
        self.excelUtil = ExcelUtil()
        print("y = mx + b") # Formula in use
        
        self.m = float(input("m = ")) # Input m
        self.b = float(input("b = ")) # Input b
        print("y = {}x + {}".format(self.m, self.b)) # Formula w/ user inputs
        
        
        
        # This is where the file will be written to, the last part (linearFunction) is the name of the file itself, we will append a date and time to the filename  
        self.filename = "/home/coco/pyApps/graphFunctions/linear/Graph-Linear-Functions/xlsxGraphs/linearFunction" 
        
        fileName = self.filename + ".xlsx" # Makes the file an xlsx file
        print("fileName = ", fileName) # Shows the name of the file
        self.excelUtil.createFile(fileName) # Creates the file      
    
        self.calcValues(self.m, self.b) 
    
    
    # This function calculates the y values of the inputted equation
    def calcValues(self, m, b):
        # Array contains x values from -10 to 10, once inputted in the linear function, it will output the y values
        self.x = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
        self.y = [] # y values will be calculated and appended to this array
        
        # Loop goes through each x value in the array and calculates the output
        for i in range(len(self.x)):
            y = self.m * self.x[i] + self.b # Calculate
            self.y.append(y) # Appends the calculated y values to the array
        
            # This writes the data to a specific column
            self.excelUtil.writeData(1,i,self.x[i])
            self.excelUtil.writeData(2,i,y)
         
        self.excelUtil.createExcelChart() 
        
        # Saves excel file    
        self.excelUtil.closeFile()
        
        # Debugs
        print("x values =",self.x)
        print("y values =",self.y)     

    
          



    

l = linear()
