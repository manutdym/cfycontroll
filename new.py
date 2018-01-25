#!/usr/bin/python
#-*-coding:utf-8
import requests
import urllib2
import  json
r=urllib2.urlopen('http://10.10.1.6/backend/grafana/series?dashboardId=nodecellar&q=select++mean(value)+from+%2Fnodecellar%5C..*%3F%5C.cpu_total_system%2F+where++time+%3E+now()+-+15m+++++group+by+time(10)++order+asc&time_precision=s')
hjson=json.loads(r.read())
print hjson[0]['points']
# for (d,x) in hjson.items:
#     print d,x

# s=r.text
# js=s.decode('utf8').encode('gb2312')
# jso=json.dumps(js)
# print type(jso)