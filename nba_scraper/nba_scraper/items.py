# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ESPNPlayer(scrapy.Item):
    first_name = scrapy.Field()
    last_name = scrapy.Field()
    team_city = scrapy.Field()
    team_name = scrapy.Field()
    number = scrapy.Field()
    height_feet = scrapy.Field()
    height_inches = scrapy.Field()
    weight = scrapy.Field()
    position = scrapy.Field()
    age = scrapy.Field()
    college = scrapy.Field()
    salary = scrapy.Field()

