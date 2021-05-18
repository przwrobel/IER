# -*- coding: utf-8 -*-
"""
Created on Sat May  8 18:22:37 2021

@author: user
"""

from tableone import TableOne, load_dataset
import pandas as pd
import os
import scipy

#READING DATA
path = os.getcwd() + '\Data_IER.csv'
data=pd.read_csv(path,encoding='cp1252')


#SORTING INTO RELEVANT CATEGORIES
participants_2019 = data[data['year'].isin([2019])]

participants_2019_male= participants_2019[participants_2019['gender'].isin(['Male'])]
participants_2019_female= participants_2019[participants_2019['gender'].isin(['Female'])]

participants_2020 = data[data['year'].isin([2020])]

participants_2020_male= participants_2020[participants_2020['gender'].isin(['Male'])]
participants_2020_female= participants_2020[participants_2020['gender'].isin(['Female'])]

#CREATING TABLE ONE
columns = ['gender','bmi','living']
categorical = ['living']
groupby = 'gender'
mytable = TableOne(participants_2019 , columns=columns, categorical=categorical, groupby=groupby)
print(mytable.tabulate(tablefmt="latex"))
mytable_2 = TableOne(participants_2020 , columns=columns, categorical=categorical, groupby=groupby)
print(mytable_2.tabulate(tablefmt="latex"))

#FILTERING NECESSARY DATA AND CALCULATING WEEKEND/WEEKDAY AVERAGES
#Overall 2019 weekdays app
temp = participants_2019[~participants_2019[['stap_app_1_aantal','stap_app_2_aantal','stap_app_3_aantal','stap_app_4_aantal','stap_app_5_aantal','stap_app_6_aantal','stap_app_7_aantal']].isin(['nan']).any(axis=1)]
participants_2019_weekdays_app=temp[['stap_app_1_aantal','stap_app_2_aantal','stap_app_6_aantal','stap_app_7_aantal','stap_app_5_aantal']]
temp_avg=participants_2019_weekdays_app.mean(axis=1)
participants_2019_weekdays_app['avg']=temp_avg

#Overall 2020 weekdays app
temp = participants_2020[~participants_2020[['stap_app_1_aantal','stap_app_2_aantal','stap_app_3_aantal','stap_app_4_aantal','stap_app_5_aantal','stap_app_6_aantal','stap_app_7_aantal']].isin(['nan']).any(axis=1)]
participants_2020_weekdays_app=temp[['stap_app_1_aantal','stap_app_2_aantal','stap_app_6_aantal','stap_app_7_aantal','stap_app_5_aantal']]
temp_avg=participants_2020_weekdays_app.mean(axis=1)
participants_2020_weekdays_app['avg']=temp_avg

#Male 2019 weekdays app
temp = participants_2019_male[~participants_2019_male[['stap_app_1_aantal','stap_app_2_aantal','stap_app_3_aantal','stap_app_4_aantal','stap_app_5_aantal','stap_app_6_aantal','stap_app_7_aantal']].isin(['nan']).any(axis=1)]
participants_2019_male_weekdays_app=temp[['stap_app_1_aantal','stap_app_2_aantal','stap_app_6_aantal','stap_app_7_aantal','stap_app_5_aantal']]
temp_avg=participants_2019_male_weekdays_app.mean(axis=1)
participants_2019_male_weekdays_app['avg']=temp_avg

#Female 2019 weekdays app
temp = participants_2019_female[~participants_2019_female[['stap_app_1_aantal','stap_app_2_aantal','stap_app_3_aantal','stap_app_4_aantal','stap_app_5_aantal','stap_app_6_aantal','stap_app_7_aantal']].isin(['nan']).any(axis=1)]
participants_2019_female_weekdays_app=temp[['stap_app_1_aantal','stap_app_2_aantal','stap_app_6_aantal','stap_app_7_aantal','stap_app_5_aantal']]
temp_avg=participants_2019_female_weekdays_app.mean(axis=1)
participants_2019_female_weekdays_app['avg']=temp_avg

#Male 2020 weekdays app
temp = participants_2020_male[~participants_2020_male[['stap_app_1_aantal','stap_app_2_aantal','stap_app_3_aantal','stap_app_4_aantal','stap_app_5_aantal','stap_app_6_aantal','stap_app_7_aantal']].isin(['nan']).any(axis=1)]
participants_2020_male_weekdays_app=temp[['stap_app_1_aantal','stap_app_2_aantal','stap_app_6_aantal','stap_app_7_aantal','stap_app_5_aantal']]
temp_avg=participants_2020_male_weekdays_app.mean(axis=1)
participants_2020_male_weekdays_app['avg']=temp_avg

#Female 2020 weekdays app
temp = participants_2020_female[~participants_2020_female[['stap_app_1_aantal','stap_app_2_aantal','stap_app_3_aantal','stap_app_4_aantal','stap_app_5_aantal','stap_app_6_aantal','stap_app_7_aantal']].isin(['nan']).any(axis=1)]
participants_2020_female_weekdays_app=temp[['stap_app_1_aantal','stap_app_2_aantal','stap_app_6_aantal','stap_app_7_aantal','stap_app_5_aantal']]
temp_avg=participants_2020_female_weekdays_app.mean(axis=1)
participants_2020_female_weekdays_app['avg']=temp_avg

##################################################

#Overall 2019 weekends app
temp = participants_2019[~participants_2019[['stap_app_1_aantal','stap_app_2_aantal','stap_app_3_aantal','stap_app_4_aantal','stap_app_5_aantal','stap_app_6_aantal','stap_app_7_aantal']].isin(['nan']).any(axis=1)]
participants_2019_weekends_app=temp[['stap_app_3_aantal','stap_app_4_aantal']]
temp_avg=participants_2019_weekends_app.mean(axis=1)
participants_2019_weekends_app['avg']=temp_avg

#Overall 2020 weekends app
temp = participants_2020[~participants_2020[['stap_app_1_aantal','stap_app_2_aantal','stap_app_3_aantal','stap_app_4_aantal','stap_app_5_aantal','stap_app_6_aantal','stap_app_7_aantal']].isin(['nan']).any(axis=1)]
participants_2020_weekends_app=temp[['stap_app_3_aantal','stap_app_4_aantal']]
temp_avg=participants_2020_weekends_app.mean(axis=1)
participants_2020_weekends_app['avg']=temp_avg

#Male 2019 weekends app
temp = participants_2019_male[~participants_2019_male[['stap_app_1_aantal','stap_app_2_aantal','stap_app_3_aantal','stap_app_4_aantal','stap_app_5_aantal','stap_app_6_aantal','stap_app_7_aantal']].isin(['nan']).any(axis=1)]
participants_2019_male_weekends_app=temp[['stap_app_3_aantal','stap_app_4_aantal']]
temp_avg=participants_2019_male_weekends_app.mean(axis=1)
participants_2019_male_weekends_app['avg']=temp_avg

#Female 2019 weekends app
temp = participants_2019_female[~participants_2019_female[['stap_app_1_aantal','stap_app_2_aantal','stap_app_3_aantal','stap_app_4_aantal','stap_app_5_aantal','stap_app_6_aantal','stap_app_7_aantal']].isin(['nan']).any(axis=1)]
participants_2019_female_weekends_app=temp[['stap_app_3_aantal','stap_app_4_aantal']]
temp_avg=participants_2019_female_weekends_app.mean(axis=1)
participants_2019_female_weekends_app['avg']=temp_avg

#Male 2020 weekends app
temp = participants_2020_male[~participants_2020_male[['stap_app_1_aantal','stap_app_2_aantal','stap_app_3_aantal','stap_app_4_aantal','stap_app_5_aantal','stap_app_6_aantal','stap_app_7_aantal']].isin(['nan']).any(axis=1)]
participants_2020_male_weekends_app=temp[['stap_app_3_aantal','stap_app_4_aantal']]
temp_avg=participants_2020_male_weekends_app.mean(axis=1)
participants_2020_male_weekends_app['avg']=temp_avg

#Female 2020 weekends app
temp = participants_2020_female[~participants_2020_female[['stap_app_1_aantal','stap_app_2_aantal','stap_app_3_aantal','stap_app_4_aantal','stap_app_5_aantal','stap_app_6_aantal','stap_app_7_aantal']].isin(['nan']).any(axis=1)]
participants_2020_female_weekends_app=temp[['stap_app_3_aantal','stap_app_4_aantal']]
temp_avg=participants_2020_female_weekends_app.mean(axis=1)
participants_2020_female_weekends_app['avg']=temp_avg

###################################################

#Overall 2019 weekdays Omron
temp = participants_2019[~participants_2019[['stap_om_1_aantal','stap_om_2_aantal','stap_om_3_aantal','stap_om_4_aantal','stap_om_5_aantal','stap_om_6_aantal','stap_om_7_aantal']].isin(['nan']).any(axis=1)]
participants_2019_weekdays_om=temp[['stap_om_1_aantal','stap_om_2_aantal','stap_om_6_aantal','stap_om_7_aantal','stap_om_5_aantal']]
temp_avg=participants_2019_weekdays_om.mean(axis=1)
participants_2019_weekdays_om['avg']=temp_avg

#Overall 2020 weekdays Omron
temp = participants_2020[~participants_2020[['stap_om_1_aantal','stap_om_2_aantal','stap_om_3_aantal','stap_om_4_aantal','stap_om_5_aantal','stap_om_6_aantal','stap_om_7_aantal']].isin(['nan']).any(axis=1)]
participants_2020_weekdays_om=temp[['stap_om_1_aantal','stap_om_2_aantal','stap_om_6_aantal','stap_om_7_aantal','stap_om_5_aantal']]
temp_avg=participants_2020_weekdays_om.mean(axis=1)
participants_2020_weekdays_om['avg']=temp_avg

#Male 2019 weekdays Omron
temp = participants_2019_male[~participants_2019_male[['stap_om_1_aantal','stap_om_2_aantal','stap_om_3_aantal','stap_om_4_aantal','stap_om_5_aantal','stap_om_6_aantal','stap_om_7_aantal']].isin(['nan']).any(axis=1)]
participants_2019_male_weekdays_om=temp[['stap_om_1_aantal','stap_om_2_aantal','stap_om_6_aantal','stap_om_7_aantal','stap_om_5_aantal']]
temp_avg=participants_2019_male_weekdays_om.mean(axis=1)
participants_2019_male_weekdays_om['avg']=temp_avg

#Female 2019 weekdays Omron
temp = participants_2019_female[~participants_2019_female[['stap_om_1_aantal','stap_om_2_aantal','stap_om_3_aantal','stap_om_4_aantal','stap_om_5_aantal','stap_om_6_aantal','stap_om_7_aantal']].isin(['nan']).any(axis=1)]
participants_2019_female_weekdays_om=temp[['stap_om_1_aantal','stap_om_2_aantal','stap_om_6_aantal','stap_om_7_aantal','stap_om_5_aantal']]
temp_avg=participants_2019_female_weekdays_om.mean(axis=1)
participants_2019_female_weekdays_om['avg']=temp_avg

#Male 2020 weekdays Omron
temp = participants_2020_male[~participants_2020_male[['stap_om_1_aantal','stap_om_2_aantal','stap_om_3_aantal','stap_om_4_aantal','stap_om_5_aantal','stap_om_6_aantal','stap_om_7_aantal']].isin(['nan']).any(axis=1)]
participants_2020_male_weekdays_om=temp[['stap_om_1_aantal','stap_om_2_aantal','stap_om_6_aantal','stap_om_7_aantal','stap_om_5_aantal']]
temp_avg=participants_2020_male_weekdays_om.mean(axis=1)
participants_2020_male_weekdays_om['avg']=temp_avg

#Female 2020 weekdays Omron
temp = participants_2020_female[~participants_2020_female[['stap_om_1_aantal','stap_om_2_aantal','stap_om_3_aantal','stap_om_4_aantal','stap_om_5_aantal','stap_om_6_aantal','stap_om_7_aantal']].isin(['nan']).any(axis=1)]
participants_2020_female_weekdays_om=temp[['stap_om_1_aantal','stap_om_2_aantal','stap_om_6_aantal','stap_om_7_aantal','stap_om_5_aantal']]
temp_avg=participants_2020_female_weekdays_om.mean(axis=1)
participants_2020_female_weekdays_om['avg']=temp_avg

##################################################

#Overall 2019 weekends Omron
temp = participants_2019[~participants_2019[['stap_om_1_aantal','stap_om_2_aantal','stap_om_3_aantal','stap_om_4_aantal','stap_om_5_aantal','stap_om_6_aantal','stap_om_7_aantal']].isin(['nan']).any(axis=1)]
participants_2019_weekends_om=temp[['stap_om_3_aantal','stap_om_4_aantal']]
temp_avg=participants_2019_weekends_om.mean(axis=1)
participants_2019_weekends_om['avg']=temp_avg

#Overall 2020 weekends Omron
temp = participants_2020[~participants_2020[['stap_om_1_aantal','stap_om_2_aantal','stap_om_3_aantal','stap_om_4_aantal','stap_om_5_aantal','stap_om_6_aantal','stap_om_7_aantal']].isin(['nan']).any(axis=1)]
participants_2020_weekends_om=temp[['stap_om_3_aantal','stap_om_4_aantal']]
temp_avg=participants_2020_weekends_om.mean(axis=1)
participants_2020_weekends_om['avg']=temp_avg

#Male 2019 weekends Omron
temp = participants_2019_male[~participants_2019_male[['stap_om_1_aantal','stap_om_2_aantal','stap_om_3_aantal','stap_om_4_aantal','stap_om_5_aantal','stap_om_6_aantal','stap_om_7_aantal']].isin(['nan']).any(axis=1)]
participants_2019_male_weekends_om=temp[['stap_om_3_aantal','stap_om_4_aantal']]
temp_avg=participants_2019_male_weekends_om.mean(axis=1)
participants_2019_male_weekends_om['avg']=temp_avg

#Female 2019 weekends Omron
temp = participants_2019_female[~participants_2019_female[['stap_om_1_aantal','stap_om_2_aantal','stap_om_3_aantal','stap_om_4_aantal','stap_om_5_aantal','stap_om_6_aantal','stap_om_7_aantal']].isin(['nan']).any(axis=1)]
participants_2019_female_weekends_om=temp[['stap_om_3_aantal','stap_om_4_aantal']]
temp_avg=participants_2019_female_weekends_om.mean(axis=1)
participants_2019_female_weekends_om['avg']=temp_avg

#Male 2020 weekends Omron
temp = participants_2020_male[~participants_2020_male[['stap_om_1_aantal','stap_om_2_aantal','stap_om_3_aantal','stap_om_4_aantal','stap_om_5_aantal','stap_om_6_aantal','stap_om_7_aantal']].isin(['nan']).any(axis=1)]
participants_2020_male_weekends_om=temp[['stap_om_3_aantal','stap_om_4_aantal']]
temp_avg=participants_2020_male_weekends_om.mean(axis=1)
participants_2020_male_weekends_om['avg']=temp_avg

#Female 2020 weekends Omron
temp = participants_2020_female[~participants_2020_female[['stap_om_1_aantal','stap_om_2_aantal','stap_om_3_aantal','stap_om_4_aantal','stap_om_5_aantal','stap_om_6_aantal','stap_om_7_aantal']].isin(['nan']).any(axis=1)]
participants_2020_female_weekends_om=temp[['stap_om_3_aantal','stap_om_4_aantal']]
temp_avg=participants_2020_female_weekends_om.mean(axis=1)
participants_2020_female_weekends_om['avg']=temp_avg

###################################################

#UNPAIRED T-TESTS (RESULTS ARE WRITTEN TO "results.txt")

f = open("results.txt", "w")

#OVERALL
###################################################
f.write("Overall weekdays app \n")
temp_test=str(scipy.stats.ttest_ind(participants_2019_weekdays_app['avg'],participants_2020_weekdays_app['avg'],axis=0,equal_var=False))
f.write(temp_test)
f.write("\n")
f.write("mean_2019=")
f.write(str(participants_2019_weekdays_app['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_2020=")
f.write(str(participants_2020_weekdays_app['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_2019=")
f.write(str(participants_2019_weekdays_app['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_2020=")
f.write(str(participants_2020_weekdays_app['avg'].std(axis=0)))
f.write("\n \n")

f.write("Overall weekdays Omron \n")
temp_test=str(scipy.stats.ttest_ind(participants_2019_weekdays_om['avg'],participants_2020_weekdays_om['avg'],axis=0,equal_var=False))
f.write(temp_test)
f.write("\n")
f.write("mean_2019=")
f.write(str(participants_2019_weekdays_om['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_2020=")
f.write(str(participants_2020_weekdays_om['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_2019=")
f.write(str(participants_2019_weekdays_om['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_2020=")
f.write(str(participants_2020_weekdays_om['avg'].std(axis=0)))
f.write("\n \n")

f.write("Overall weekends app \n")
temp_test=str(scipy.stats.ttest_ind(participants_2019_weekends_app['avg'],participants_2020_weekends_app['avg'],axis=0,equal_var=False))
f.write(temp_test)
f.write("\n")
f.write("mean_2019=")
f.write(str(participants_2019_weekends_app['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_2020=")
f.write(str(participants_2020_weekends_app['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_2019=")
f.write(str(participants_2019_weekends_app['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_2020=")
f.write(str(participants_2020_weekends_app['avg'].std(axis=0)))
f.write("\n \n")

f.write("Overall weekends Omron \n")
temp_test=str(scipy.stats.ttest_ind(participants_2019_weekends_om['avg'],participants_2020_weekends_om['avg'],axis=0,equal_var=False))
f.write(temp_test)
f.write("\n")
f.write("mean_2019=")
f.write(str(participants_2019_weekends_om['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_2020=")
f.write(str(participants_2020_weekends_om['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_2019=")
f.write(str(participants_2019_weekends_om['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_2020=")
f.write(str(participants_2020_weekends_om['avg'].std(axis=0)))
f.write("\n \n")
#########################################

#MALE
#########################################
f.write("Male weekdays app \n")
temp_test=str(scipy.stats.ttest_ind(participants_2019_male_weekdays_app['avg'],participants_2020_male_weekdays_app['avg'],axis=0,equal_var=False))
f.write(temp_test)
f.write("\n")
f.write("mean_2019=")
f.write(str(participants_2019_male_weekdays_app['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_2020=")
f.write(str(participants_2020_male_weekdays_app['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_2019=")
f.write(str(participants_2019_male_weekdays_app['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_2020=")
f.write(str(participants_2020_male_weekdays_app['avg'].std(axis=0)))
f.write("\n \n")

f.write("Male weekdays Omron \n")
temp_test=str(scipy.stats.ttest_ind(participants_2019_male_weekdays_om['avg'],participants_2020_male_weekdays_om['avg'],axis=0,equal_var=False))
f.write(temp_test)
f.write("\n")
f.write("mean_2019=")
f.write(str(participants_2019_male_weekdays_om['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_2020=")
f.write(str(participants_2020_male_weekdays_om['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_2019=")
f.write(str(participants_2019_male_weekdays_om['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_2020=")
f.write(str(participants_2020_male_weekdays_om['avg'].std(axis=0)))
f.write("\n \n")

f.write("Male weekends app \n")
temp_test=str(scipy.stats.ttest_ind(participants_2019_male_weekends_app['avg'],participants_2020_male_weekends_app['avg'],axis=0,equal_var=False))
f.write(temp_test)
f.write("\n")
f.write("mean_2019=")
f.write(str(participants_2019_male_weekends_app['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_2020=")
f.write(str(participants_2020_male_weekends_app['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_2019=")
f.write(str(participants_2019_male_weekends_app['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_2020=")
f.write(str(participants_2020_male_weekends_app['avg'].std(axis=0)))
f.write("\n \n")

f.write("Male weekends Omron \n")
temp_test=str(scipy.stats.ttest_ind(participants_2019_male_weekends_om['avg'],participants_2020_male_weekends_om['avg'],axis=0,equal_var=False))
f.write(temp_test)
f.write("\n")
f.write("mean_2019=")
f.write(str(participants_2019_male_weekends_om['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_2020=")
f.write(str(participants_2020_male_weekends_om['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_2019=")
f.write(str(participants_2019_male_weekends_om['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_2020=")
f.write(str(participants_2020_male_weekends_om['avg'].std(axis=0)))
f.write("\n \n")
#########################################

#FEMALE
#########################################
f.write("Female weekdays app \n")
temp_test=str(scipy.stats.ttest_ind(participants_2019_female_weekdays_app['avg'],participants_2020_female_weekdays_app['avg'],axis=0,equal_var=False))
f.write(temp_test)
f.write("\n")
f.write("mean_2019=")
f.write(str(participants_2019_female_weekdays_app['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_2020=")
f.write(str(participants_2020_female_weekdays_app['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_2019=")
f.write(str(participants_2019_female_weekdays_app['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_2020=")
f.write(str(participants_2020_female_weekdays_app['avg'].std(axis=0)))
f.write("\n \n")

f.write("Female weekdays Omron \n")
temp_test=str(scipy.stats.ttest_ind(participants_2019_female_weekdays_om['avg'],participants_2020_female_weekdays_om['avg'],axis=0,equal_var=False))
f.write(temp_test)
f.write("\n")
f.write("mean_2019=")
f.write(str(participants_2019_female_weekdays_om['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_2020=")
f.write(str(participants_2020_female_weekdays_om['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_2019=")
f.write(str(participants_2019_female_weekdays_om['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_2020=")
f.write(str(participants_2020_female_weekdays_om['avg'].std(axis=0)))
f.write("\n \n")

f.write("Female weekends app \n")
temp_test=str(scipy.stats.ttest_ind(participants_2019_female_weekends_app['avg'],participants_2020_female_weekends_app['avg'],axis=0,equal_var=False))
f.write(temp_test)
f.write("\n")
f.write("mean_2019=")
f.write(str(participants_2019_female_weekends_app['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_2020=")
f.write(str(participants_2020_female_weekends_app['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_2019=")
f.write(str(participants_2019_female_weekends_app['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_2020=")
f.write(str(participants_2020_female_weekends_app['avg'].std(axis=0)))
f.write("\n \n")

f.write("Female weekends Omron \n")
temp_test=str(scipy.stats.ttest_ind(participants_2019_female_weekends_om['avg'],participants_2020_female_weekends_om['avg'],axis=0,equal_var=False))
f.write(temp_test)
f.write("\n")
f.write("mean_2019=")
f.write(str(participants_2019_female_weekends_om['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_2020=")
f.write(str(participants_2020_female_weekends_om['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_2019=")
f.write(str(participants_2019_female_weekends_om['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_2020=")
f.write(str(participants_2020_female_weekends_om['avg'].std(axis=0)))
f.write("\n \n")
#########################################

#INTERNAL TESTS
#########################################
f.write("Internal weekdays app 2019 \n")
temp_test=str(scipy.stats.ttest_ind(participants_2019_female_weekdays_app['avg'],participants_2019_male_weekdays_app['avg'],axis=0,equal_var=False))
f.write(temp_test)
f.write("\n")
f.write("mean_female=")
f.write(str(participants_2019_female_weekdays_app['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_male=")
f.write(str(participants_2019_male_weekdays_app['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_female=")
f.write(str(participants_2019_female_weekdays_app['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_male=")
f.write(str(participants_2019_male_weekdays_app['avg'].std(axis=0)))
f.write("\n \n")

f.write("Internal weekdays Omron 2019 \n")
temp_test=str(scipy.stats.ttest_ind(participants_2019_female_weekdays_om['avg'],participants_2019_male_weekdays_om['avg'],axis=0,equal_var=False))
f.write(temp_test)
f.write("\n")
f.write("mean_female=")
f.write(str(participants_2019_female_weekdays_om['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_male=")
f.write(str(participants_2019_male_weekdays_om['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_female=")
f.write(str(participants_2019_female_weekdays_om['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_male=")
f.write(str(participants_2019_male_weekdays_om['avg'].std(axis=0)))
f.write("\n \n")

f.write("Internal weekdays app 2020 \n")
temp_test=str(scipy.stats.ttest_ind(participants_2020_female_weekdays_app['avg'],participants_2020_male_weekdays_app['avg'],axis=0,equal_var=False))
f.write(temp_test)
f.write("\n")
f.write("mean_female=")
f.write(str(participants_2020_female_weekdays_app['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_male=")
f.write(str(participants_2020_male_weekdays_app['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_female=")
f.write(str(participants_2020_female_weekdays_app['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_male=")
f.write(str(participants_2020_male_weekdays_app['avg'].std(axis=0)))
f.write("\n \n")

f.write("Internal weekdays Omron 2020 \n")
temp_test=str(scipy.stats.ttest_ind(participants_2020_female_weekdays_om['avg'],participants_2020_male_weekdays_om['avg'],axis=0,equal_var=False))
f.write(temp_test)
f.write("\n")
f.write("mean_female=")
f.write(str(participants_2020_female_weekdays_om['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_male=")
f.write(str(participants_2020_male_weekdays_om['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_female=")
f.write(str(participants_2020_female_weekdays_om['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_male=")
f.write(str(participants_2020_male_weekdays_om['avg'].std(axis=0)))
f.write("\n \n")

f.write("Internal weekends app 2019 \n")
temp_test=str(scipy.stats.ttest_ind(participants_2019_female_weekends_app['avg'],participants_2019_male_weekends_app['avg'],axis=0,equal_var=False))
f.write(temp_test)
f.write("\n")
f.write("mean_female=")
f.write(str(participants_2019_female_weekends_app['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_male=")
f.write(str(participants_2019_male_weekends_app['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_female=")
f.write(str(participants_2019_female_weekends_app['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_male=")
f.write(str(participants_2019_male_weekends_app['avg'].std(axis=0)))
f.write("\n \n")

f.write("Internal weekends Omron 2019 \n")
temp_test=str(scipy.stats.ttest_ind(participants_2019_female_weekends_om['avg'],participants_2019_male_weekends_om['avg'],axis=0,equal_var=False))
f.write(temp_test)
f.write("\n")
f.write("mean_female=")
f.write(str(participants_2019_female_weekends_om['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_male=")
f.write(str(participants_2019_male_weekends_om['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_female=")
f.write(str(participants_2019_female_weekends_om['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_male=")
f.write(str(participants_2019_male_weekends_om['avg'].std(axis=0)))
f.write("\n \n")

f.write("Internal weekends app 2020 \n")
temp_test=str(scipy.stats.ttest_ind(participants_2020_female_weekends_app['avg'],participants_2020_male_weekends_app['avg'],axis=0,equal_var=False))
f.write(temp_test)
f.write("\n")
f.write("mean_female=")
f.write(str(participants_2020_female_weekends_app['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_male=")
f.write(str(participants_2020_male_weekends_app['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_female=")
f.write(str(participants_2020_female_weekends_app['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_male=")
f.write(str(participants_2020_male_weekends_app['avg'].std(axis=0)))
f.write("\n \n")

f.write("Internal weekends Omron 2020 \n")
temp_test=str(scipy.stats.ttest_ind(participants_2020_female_weekends_om['avg'],participants_2020_male_weekends_om['avg'],axis=0,equal_var=False))
f.write(temp_test)
f.write("\n")
f.write("mean_female=")
f.write(str(participants_2020_female_weekends_om['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_male=")
f.write(str(participants_2020_male_weekends_om['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_female=")
f.write(str(participants_2020_female_weekends_om['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_male=")
f.write(str(participants_2020_male_weekends_om['avg'].std(axis=0)))
f.write("\n \n")

#########################################

#WEEKDAY VS WEEKEND

#########################################
f.write("Weekend vs weekdays overall app 2019 \n")
temp_test=str(scipy.stats.ttest_rel(participants_2019_weekdays_app['avg'],participants_2019_weekends_app['avg'],axis=0))
f.write(temp_test)
f.write("\n")
f.write("mean_weekdays=")
f.write(str(participants_2019_weekdays_app['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_weekends=")
f.write(str(participants_2019_weekends_app['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_weekdays=")
f.write(str(participants_2019_weekdays_app['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_weekends=")
f.write(str(participants_2019_weekends_app['avg'].std(axis=0)))
f.write("\n \n")

f.write("Weekend vs weekdays overall Omron 2019 \n")
temp_test=str(scipy.stats.ttest_rel(participants_2019_weekdays_om['avg'],participants_2019_weekends_om['avg'],axis=0))
f.write(temp_test)
f.write("\n")
f.write("mean_weekdays=")
f.write(str(participants_2019_weekdays_om['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_weekends=")
f.write(str(participants_2019_weekends_om['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_weekdays=")
f.write(str(participants_2019_weekdays_om['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_weekends=")
f.write(str(participants_2019_weekends_om['avg'].std(axis=0)))
f.write("\n \n")

f.write("Weekend vs weekdays overall app 2020 \n")
temp_test=str(scipy.stats.ttest_rel(participants_2020_weekdays_app['avg'],participants_2020_weekends_app['avg'],axis=0))
f.write(temp_test)
f.write("\n")
f.write("mean_weekdays=")
f.write(str(participants_2020_weekdays_app['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_weekends=")
f.write(str(participants_2020_weekends_app['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_weekdays=")
f.write(str(participants_2020_weekdays_app['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_weekends=")
f.write(str(participants_2020_weekends_app['avg'].std(axis=0)))
f.write("\n \n")

f.write("Weekend vs weekdays overall Omron 2020 \n")
temp_test=str(scipy.stats.ttest_rel(participants_2020_weekdays_om['avg'],participants_2020_weekends_om['avg'],axis=0))
f.write(temp_test)
f.write("\n")
f.write("mean_weekdays=")
f.write(str(participants_2020_weekdays_om['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_weekends=")
f.write(str(participants_2020_weekends_om['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_weekdays=")
f.write(str(participants_2020_weekdays_om['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_weekends=")
f.write(str(participants_2020_weekends_om['avg'].std(axis=0)))
f.write("\n \n")

f.write("Weekend vs weekdays males app 2019 \n")
temp_test=str(scipy.stats.ttest_rel(participants_2019_male_weekdays_app['avg'],participants_2019_male_weekends_app['avg'],axis=0))
f.write(temp_test)
f.write("\n")
f.write("mean_weekdays=")
f.write(str(participants_2019_male_weekdays_app['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_weekends=")
f.write(str(participants_2019_male_weekends_app['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_weekdays=")
f.write(str(participants_2019_male_weekdays_app['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_weekends=")
f.write(str(participants_2019_male_weekends_app['avg'].std(axis=0)))
f.write("\n \n")

f.write("Weekend vs weekdays males Omron 2019\n")
temp_test=str(scipy.stats.ttest_rel(participants_2019_male_weekdays_om['avg'],participants_2019_male_weekends_om['avg'],axis=0))
f.write(temp_test)
f.write("\n")
f.write("mean_weekdays=")
f.write(str(participants_2019_male_weekdays_om['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_weekends=")
f.write(str(participants_2019_male_weekends_om['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_weekdays=")
f.write(str(participants_2019_male_weekdays_om['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_weekends=")
f.write(str(participants_2019_male_weekends_om['avg'].std(axis=0)))
f.write("\n \n")

f.write("Weekend vs weekdays males app 2020\n")
temp_test=str(scipy.stats.ttest_rel(participants_2020_male_weekdays_app['avg'],participants_2020_male_weekends_app['avg'],axis=0))
f.write(temp_test)
f.write("\n")
f.write("mean_weekdays=")
f.write(str(participants_2020_male_weekdays_app['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_weekends=")
f.write(str(participants_2020_male_weekends_app['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_weekdays=")
f.write(str(participants_2020_male_weekdays_app['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_weekends=")
f.write(str(participants_2020_male_weekends_app['avg'].std(axis=0)))
f.write("\n \n")

f.write("Weekend vs weekdays males Omron 2020 \n")
temp_test=str(scipy.stats.ttest_rel(participants_2020_male_weekdays_om['avg'],participants_2020_male_weekends_om['avg'],axis=0))
f.write(temp_test)
f.write("\n")
f.write("mean_weekdays=")
f.write(str(participants_2020_male_weekdays_om['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_weekends=")
f.write(str(participants_2020_male_weekends_om['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_weekdays=")
f.write(str(participants_2020_male_weekdays_om['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_weekends=")
f.write(str(participants_2020_male_weekends_om['avg'].std(axis=0)))
f.write("\n \n")

f.write("Weekend vs weekdays females app 2019 \n")
temp_test=str(scipy.stats.ttest_rel(participants_2019_female_weekdays_app['avg'],participants_2019_female_weekends_app['avg'],axis=0))
f.write(temp_test)
f.write("\n")
f.write("mean_weekdays=")
f.write(str(participants_2019_female_weekdays_app['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_weekends=")
f.write(str(participants_2019_female_weekends_app['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_weekdays=")
f.write(str(participants_2019_female_weekdays_app['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_weekends=")
f.write(str(participants_2019_female_weekends_app['avg'].std(axis=0)))
f.write("\n \n")

f.write("Weekend vs weekdays females Omron 2019\n")
temp_test=str(scipy.stats.ttest_rel(participants_2019_female_weekdays_om['avg'],participants_2019_female_weekends_om['avg'],axis=0))
f.write(temp_test)
f.write("\n")
f.write("mean_weekdays=")
f.write(str(participants_2019_female_weekdays_om['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_weekends=")
f.write(str(participants_2019_female_weekends_om['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_weekdays=")
f.write(str(participants_2019_female_weekdays_om['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_weekends=")
f.write(str(participants_2019_female_weekends_om['avg'].std(axis=0)))
f.write("\n \n")

f.write("Weekend vs weekdays females app 2020\n")
temp_test=str(scipy.stats.ttest_rel(participants_2020_female_weekdays_app['avg'],participants_2020_female_weekends_app['avg'],axis=0))
f.write(temp_test)
f.write("\n")
f.write("mean_weekdays=")
f.write(str(participants_2020_female_weekdays_app['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_weekends=")
f.write(str(participants_2020_female_weekends_app['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_weekdays=")
f.write(str(participants_2020_female_weekdays_app['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_weekends=")
f.write(str(participants_2020_female_weekends_app['avg'].std(axis=0)))
f.write("\n \n")

f.write("Weekend vs weekdays females Omron 2020 \n")
temp_test=str(scipy.stats.ttest_rel(participants_2020_female_weekdays_om['avg'],participants_2020_female_weekends_om['avg'],axis=0))
f.write(temp_test)
f.write("\n")
f.write("mean_weekdays=")
f.write(str(participants_2020_female_weekdays_om['avg'].mean(axis=0)))
f.write("\n")
f.write("mean_weekends=")
f.write(str(participants_2020_female_weekends_om['avg'].mean(axis=0)))
f.write("\n")
f.write("stdev_weekdays=")
f.write(str(participants_2020_female_weekdays_om['avg'].std(axis=0)))
f.write("\n")
f.write("stdev_weekends=")
f.write(str(participants_2020_female_weekends_om['avg'].std(axis=0)))
f.write("\n \n")

f.close()