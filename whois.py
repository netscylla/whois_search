#!/opt/local/bin/python3.6

import csv
import requests
import re
import datetime
import time 
import sys

def get_days_past(number_days):
  return datetime.date.fromordinal(datetime.date.today().toordinal()-number_days).strftime('%Y-%m-%d')

def unique(list1):
  unique_list = []
  for x in list1:
    if x not in unique_list:
      unique_list.append(x)
  return unique_list


def whois_search(keyword,days):

  print("[+] DEBUG Searching for: "+keyword)

  headers={'Origin':'https://brand-alert-api.whoisxmlapi.com','Referer':'https://brand-alert-api.whoisxmlapi.com/'}
  data={'MIME Type': 'application/x-www-form-urlencoded; charset=UTF-8','fromSiteRequest': 'true','mode': 'purchase','sinceDate': get_days_past(days),'responseFormat': 'JSON','includeSearchTerms[]': ''+keyword+''}
  url='https://brand-alert-api.whoisxmlapi.com/api/v1whois'

  r=requests.post(url,params=data,headers=headers)

  if (r.status_code != 200 ):
    return("[-] DEBUG Something went wrong?, exiting...")
  if (r.status_code != 503 ):
    return("[-] DEBUG Resource exhausted, wait and try again later.")
    exit(0)

  return(r.text)

