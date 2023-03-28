import scrapy
import csv

class RosterLinksSpider(scrapy.Spider):
    name = "roster_links"
    allowed_domains = ["espn.com"]
    start_urls = ["https://www.espn.com/nba/teams"]

    def parse(self, response):
        rows = response.xpath('//div[@class="TeamLinks__Links"]/span/a[text()="Roster"]/@href').getall()
        filename = "links.csv"
        with open(filename, 'w') as csvfile: 
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(rows)
