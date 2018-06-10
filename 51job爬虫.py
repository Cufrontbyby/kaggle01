
# coding: utf-8

# 爬虫练习

import time
import requests 
from lxml import etree

import pandas as pd
from pandas import DataFrame
from pandas import Series


def Crawler_51job(df_origin,n):
    head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    s= requests.Session()
    for i in range(1,n+1):
          url='https://search.51job.com/list/000000,000000,0000,00,9,99,%25E9%2587%2591%25E8%259E%258D%25E6%259C%258D%25E5%258A%25A1,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
          res=s.get(url,headers=head)
          res.encoding='gbk'
          root=etree.HTML(res.text)
          postion = root.xpath('//div[@class="el"]/p/span/a/@title')
          company =root.xpath('//div[@class="el"]/span[@class="t2"]/a/@title')
          place = root.xpath('//div[@class="el"]/span[@class="t3"]/text()')
          salary =root.xpath('//div[@class="el"]/span[@class="t4"]/text()')
          date =root.xpath('//div[@class="el"]/span[@class="t5"]/text()')
          df=DataFrame([postion,company,place,salary,date]).T
          df.columns=['postion','company','place','salary','date']
          df['page']=i
          time.sleep(2)
          df_origin=pd.concat([df_origin,df])
    return(df_origin)
          

job= Crawler_51job(job,100)
job=job.drop_duplicates()
job.to_csv('51job.csv',index=0)





