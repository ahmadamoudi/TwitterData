#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: @AhmadAmoudii
"""

#Collecting Data from Twitter 

# importing required libraries
import tweepy
import csv
import datetime
import time


#define and store your credintials
consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

#Tweepy auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Enter the keyword (kw) that you want to collect tweets based on it
kw = input('Enter keyword: ')

#Enter the number of the tweets you want to fetch
num = int(input('Number of tweet (enter -1 if you want max number) : '))

# Open/Create a file to append data
csvFile = open(kw+'.csv', 'a')

#Use csv Writer
csvWriter = csv.writer(csvFile)

#Columns that you want to print in CSV file
csvWriter.writerow(['Tweet_Date', 'user_id','username','Followers','Verified', 'Tweet_text'])

apicalls = 0
count =0

for tweet in tweepy.Cursor(api.search,q=kw,count=100).items():
    
    apicalls = apicalls+1
    if (apicalls == 150*100):
        print("sleep")
        apicalls = 0
        time.sleep(15*60)
    
    
    csvWriter.writerow([tweet.created_at, tweet.user.screen_name, tweet.user.followers_count, tweet.text.encode('utf-8')])
    counter=counter+1
    
    if num==-1:
        pass
    elif counter==num:
        break
        

print("Fetch Finished")
