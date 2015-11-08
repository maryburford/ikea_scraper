import csv
import urllib2
import time

with open('ikea.psv', 'ab') as csvfile:
	writer = csv.writer(csvfile,delimiter='|')
	for i in range(1,26):
		    number = str(i)
		    url = 'http://www.ikea.com/us/en/catalog/productsaz/'+number+'/'
		    data = urllib2.urlopen(url)  
		    for line in data:
		    	if '<span class="productsAzLink">' in line:
		    		f,u = line.split('<a href="',2)
		    		url,c = u.split('">')
		    		print url
		    		name = c.replace('</a></span>','').strip()
		    		item_url = 'http://www.ikea.com'+url
		    		try:
			    		item_data = urllib2.urlopen(item_url)
			    		for line in item_data:
			    			if '<img id="productImg"' in line:
			    				f,u = line.split("src='")
			    				item_image_url = u.replace("'",'').strip()
			    		writer.writerow([name,'http://www.ikea.com'+item_image_url])
			    		print name
			    		item_image_url = ''
			    	except Exception as e:
			    		print str(e)
			    		writer.writerow(['error',url,str(e)])

