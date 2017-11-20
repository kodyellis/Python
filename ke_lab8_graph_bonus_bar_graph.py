# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 13:24:25 2017

@author: Kody Ellis
"""

#Kody Ellis
#Lab 8 Bonus Bar graph
import numpy as np 

def WeatherStats(aWeatherFile):
    barometric_p = []
    relative_humidity = []
    temperature = []
    wind_direction = []
    wind_speed = []
    
    fileHandle = open(aWeatherFile, "r")
    for item in fileHandle:
        if (item[0] == "#") or (not(item[0].isdigit())):
            pass
        else:
            second = item.split()[1] 
            if second.split(',')[1] == 'NaN':
                pass
            else:
                barometric_p.append(float(second.split(',')[1])) 
            
            if second.split(',')[2] == 'NaN':
                pass
            else:
                relative_humidity.append(float(second.split(',')[2])) 
                
            if second.split(',')[3] == 'NaN':
                pass
            else:
                temperature.append(float(second.split(',')[3])) 
            
            if second.split(',')[4] == 'NaN':
                pass
            else:
                wind_direction.append(float(second.split(',')[4])) 
            
            if second.split(',')[5] == 'NaN':
                pass
            else:
                wind_speed.append(float(second.split(',')[5])) 
    
    if len(barometric_p) ==  0:
        fileHandle.close()
        return None 
    else:

        out5 = sum(wind_speed)/len(wind_speed)
        
        fileHandle.close()
        return(out5)


import glob 
file_list = glob.glob('Augspurger/*')

monthly_bp_average = []  
fall_season_monthly_bp_average = []
winter_season_monthly_bp_average = []
spring_season_monthly_bp_average = []
summer_season_monthly_bp_average = []

#tupless
fall = ("9","10","11")
winter = ("12","01","02")
spring = ("03","04","05")
summer = ("06","07","08")

fall_string = 'Monthly Wind Speed Average Sep to Nov 2016 - 2017'
winter_string = 'Monthly Wind Speed Average Dec to Feb 2016 - 2017'
spring_string = 'Monthly Wind Speed Average Mar to May 2016 - 2017'
summer_string = 'Monthly Wind Speed Average Jun to Aug 2016 - 2017'

def season_to_list(list1,season):
    for individual_file in file_list:
        flag = individual_file.split('_')[2].split('_')[0].split('.')[0] #finally gets 01, 02, etc
        if flag in season:
            out = WeatherStats(individual_file)
            list1.append(out)

#gets data from each season
season_to_list(fall_season_monthly_bp_average, fall)
season_to_list(winter_season_monthly_bp_average, winter)
season_to_list(spring_season_monthly_bp_average, spring)
season_to_list(summer_season_monthly_bp_average, summer)

#gets averages of all seasons
fall_avg = np.mean(fall_season_monthly_bp_average)
winter_avg = np.mean(winter_season_monthly_bp_average)
spring_avg = np.mean(spring_season_monthly_bp_average)
summer_avg = np.mean(summer_season_monthly_bp_average)

month_avg = [fall_avg, winter_avg,spring_avg,summer_avg]

import matplotlib.pyplot as plt

def bar_graph(word, month_avg):
    months = ("Fall", "Winter", "Summer", "Spring")
    y_pos = np.arange(len(months))    
    plt.bar(y_pos, month_avg, align='center', alpha=0.5)
    plt.xticks(y_pos,months)
    plt.ylabel('Wind Speed Average')
    plt.title(word)
    plt.savefig('average_bar_temp.png')
    plt.show()
    
bar_graph(fall_string, month_avg)