import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.PhantomJS()
driver.set_window_size(1400, 1000)
driver.get("http://www.ncix.com/openbox/")
#driver.get("http://www.ncix.com/promo/SuperSanta2016.htm")

time_now = datetime.now().strftime("%y%m%d%H%M")
file = open('ncix%s.txt' % time_now,'w')

def search(text):
	searchbox = driver.find_element_by_name("promokw")
	searchbox.clear()
	searchbox.send_keys(text)
	searchbox.send_keys(Keys.RETURN)
	time.sleep(4)
	if "No result." in driver.page_source:
		file.write ("-"*9+text+"-"*9)
		file.write ("\n\n")
	else:
		file.write ("-"*9+text+"-"*9)
		file.write ("\n\n")
		item = driver.find_element_by_xpath('''
			/html/body/table/tbody/tr/td/table[2]/tbody/tr/td[@class='normal']/table[2]/tbody/tr/td[@id='searchresultmiddle']/table[@class='normal']
			''')
		rows = item.find_elements_by_xpath('''.//tbody/tr''')
		for row in rows: 
			cols = row.find_elements_by_xpath('''.//td''')
			for col in cols:
				try:
					blocks = col.find_elements_by_xpath('''.//div/div''')
					for block in blocks:
						aa = block.find_elements_by_tag_name('a')
						for a in aa:
							if a.get_attribute("title")!="":
								file.write (a.get_attribute("innerHTML"))
								file.write ("\n")
								file.write (a.get_attribute( "href" ))
								file.write ("\n")
					bs = col.find_elements_by_xpath('''.//div/div[3]/b''')
					if len(bs) > 0:
						font = block.find_elements_by_tag_name('font')[0]
						file.write (font.get_attribute("innerHTML").replace('&nbsp;',''))
						file.write ("\n\n")

				except Exception as b:
					print(b)
					continue

search("gtx 1080")
search("gtx 1070")
search("gtx 1060")
search("6700k")
search("6600k")
