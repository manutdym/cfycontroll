import requests
r=requests.get('http://10.10.1.6/backend/grafana/series?dashboardId=nodecellar&q=select++mean(value)+from+%2Fnodecellar%5C..*%3F%5C.cpu_total_system%2F+where++time+%3E+now()+-+15m+++++group+by+time(10)++order+asc&time_precision=s')
print r.text