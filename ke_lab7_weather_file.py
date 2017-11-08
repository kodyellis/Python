# -*- coding: utf-8 -*-
"""
Created on Fri Nov 03 16:15:47 2017

@author: Kody Ellis
"""
import numpy
#file, string

def weatherStats(aWeatherFile, aDate = "11/3/2017"):
    """"This opens up a designated file that should be weather data.csv
    The program then starts to read the file. For every line in the file, if 
    it starts with a '#' or a non-numerical character the program skips it.
    
    
    If the file has a numerical chracter, it starts to append data to a list 
    using the split() function. The field parameter is for getting 
    certain types of data, as each increase in the field starting from 0 will
    return a new field of data. 
    
    
    For example is field = 2 then the field will
    return all data for relative humidity.
    """
    file_connector = open(aWeatherFile, "r")
    field_data = []


    #prints baromeric pressure
    #clears array of values
    for line in file_connector:
        if line[0] == "#" or (not line [0].isdigit()) :
            pass
        else:
            #only gets items from date
            if line.split()[0] == aDate:
                #split(",")[2] takes relative humidity
                field_data.append(float(line.split()[1].split(",")[1]))
                
    barometric_p = min(field_data)
    file_connector.close()
    
    #clears array of values
    field_data = []
    file_connector = open(aWeatherFile, "r")
    for line in file_connector:
   
        if line[0] == "#" or (not line [0].isdigit()) :
            pass
        else:
            #only gets items from date
            if line.split()[0] == aDate:
                field_data.append(float(line.split()[1].split(",")[2]))
                
    humid = max(field_data)
    file_connector.close()
        
    
    #clears array of values 
    field_data = []
    file_connector = open(aWeatherFile, "r")
    for line in file_connector:
        if line[0] == "#" or (not line [0].isdigit()) :
            pass
        else:
                #only gets items from date
            if line.split()[0] == aDate:
                field_data.append(float(line.split()[1].split(",")[3]))
    file_connector.close()   
    temperature = numpy.mean(field_data)
    
              
    
    #clears array of values            
    field_data = []
    file_connector = open(aWeatherFile, "r")
    for line in file_connector:
        if line[0] == "#" or (not line [0].isdigit()) :
            pass
        else:
            #only gets items from date
            if line.split()[0] == aDate:
                field_data.append(float(line.split()[1].split(",")[4]))
    file_connector.close()
    wind_direction = numpy.median(field_data)



    #clears array of values
    field_data = []
    file_connector = open(aWeatherFile, "r")
    for line in file_connector:
        if line[0] == "#" or (not line [0].isdigit()) :
            pass
        else:
                #only gets items from date
            if line.split()[0] == aDate:
                    field_data.append(float(line.split()[1].split(",")[5]))
                
    file_connector.close()
    wind_speed = numpy.mean(field_data)

    lineReturn = "Barometric Pressure:", barometric_p, "Relative Humidity:", \
    humid, "Temperature:", temperature, "Wind Direction:", wind_direction, \
    "Wind Speed:", wind_speed
    
    return lineReturn

print weatherStats("weather_data.csv")


 
