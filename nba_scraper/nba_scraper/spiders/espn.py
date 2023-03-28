import scrapy
import csv

fields = ["First Name", "Last Name", "Team City", "Team Name", "Number", "Height (feet)", "Height (inches)", "Weight", "Position", "Age", "College", "Salary"]
rows = []

def get_team_links():
    with open("links.csv") as file:
        links = csv.reader(file)
        list = []
        correct_list = []
        for row in links:
            for int in range(30):
                list.append(row[int])
    for link in list:
        correct_link = "https://www.espn.com" + link
        correct_list.append(correct_link)
    return correct_list

class EspnSpider(scrapy.Spider):
    name = "espn"
    allowed_domains = ["espn.com"]
    start_urls = get_team_links()

    def parse(self, response):
        team_city = response.xpath('//span[@class="db pr3 nowrap"]/text()').get()
        team_name = response.xpath('//span[@class="db fw-bold"]/text()').get()
        cur_index = 0

        while True:
            full_name = response.xpath(f'//tr[(@class="Table__TR Table__TR--lg Table__even") and (@data-idx="{cur_index}")]/td/div/a/text()').get()
            if full_name == None:
                break
            more_info = response.xpath(f'//tr[(@class="Table__TR Table__TR--lg Table__even") and (@data-idx="{cur_index}")]/td/div/text()').getall()

            split_name = full_name.split()
            first_name = split_name[0]
            del split_name[0]
            last_name = " ".join(split_name)

            number = response.xpath(f'//tr[(@class="Table__TR Table__TR--lg Table__even") and (@data-idx="{cur_index}")]/td/div/span/text()').get()

            height = more_info[2]
            height_feet = height[height.index("\'") - 1]
            quote_index = height.index("\"")
            height_inches = height[quote_index - 2:quote_index].strip()

            weight = more_info[3]
            position = more_info[0]
            age = more_info[1]
            college = more_info[4]
            salary = more_info[5]

            rows.append([first_name, last_name, team_city, team_name, number, height_feet, height_inches, weight, position, age, college, salary])

            cur_index += 1

        filename = "player_list.csv"
        with open(filename, 'w') as csvfile: 
            csvwriter = csv.writer(csvfile)  
            csvwriter.writerow(fields) 
            csvwriter.writerows(rows)
