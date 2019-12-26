from selenium import webdriver
import get_statistics
import get_links
import add_istatistik
import time
import csv

links = []
links = get_links.get_links("https://www.mackolik.com/puan-durumu/t%C3%BCrkiye-s%C3%BCper-lig/fikstur/482ofyysbdbeoxauk19yg7tdt","/html/body/div[6]/div[2]/main/div/div[4]/div[1]/div/div/ul/li[7]")
links = add_istatistik.add_istatistik(links)
file_rows = []

for idx, item in enumerate(links):
    match_details = get_statistics.get_stat(item)
    print("{0}/{1} => {2}".format(idx+1,len(links),match_details))
    file_rows.append(match_details)

with open('2016-2017_tsl.csv', 'w', newline='') as f:
    for i in file_rows:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL)
        wr.writerow(i)