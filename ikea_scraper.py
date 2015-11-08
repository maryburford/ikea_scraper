import csv
import urllib2

with open('ikea.psv', 'wb') as csvfile:
    writer = csv.writer(csvfile,delimiter='|')
    url = 'http://www.ikea.com/us/en/catalog/productsaz/0/'
    data = urllib2.urlopen(url)  
    for line in data:
    	if '<span class="productsAzLink">' in line:
    		f,u = line.split('<a href="',2)
    		url,c = u.split('">')
    		name = c.replace('</a></span>','').strip()
    		print name
    		writer.writerow([name])