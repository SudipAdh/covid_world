# -*- coding: utf-8 -*-
import scrapy
from covid_nepal.items import CovidNepalItem

class CovidSipdeySpider(scrapy.Spider):
    name = 'covid_spidey'
    def start_requests(self):
        start_urls = ['https://earthquakealertnepal.com/api/covid-world']

        for url in start_urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        items = CovidNepalItem()
        whole = response.xpath("//body//text()").get()
        whole = whole.split("[")
        whole = whole[1].split("]")
        print(len(whole))
        splited = whole[0].split("},")
        print(len(splited))
        for each in splited:
            new = each.replace("{","").replace("}","")
            spliter =  new.split(",")
            for each_spliter in spliter:
                main_split = each_spliter.split(":")
                key = main_split[0].replace('"',"")
                value = main_split[1].replace('"',"")
                
                
                if key == "confirmed_total":
                    items["confirmed"] = value
                elif key == "deaths_total":
                    items["deaths"] = value
                elif key == "recovered_total":
                    items["recovered"] = value
                elif key == "active_total":
                    items["active"] = value
                elif key == "Country_Region":
                    items["country"] = value
            yield items

                

       
       
       
       
        # print(response.url)
        # items = CovidNepalItem()
        # div_data = response.xpath("//tbody//tr")
        # for each_div in div_data:
        #     items["country"] = each_div.xpath("/td[1]/text()").get()
        #     items["confirmed"] = each_div.xpath("/td[2]/text()").get()
        #     items["deaths"] = each_div.xpath("/td[3]/text()").get()
        #     items["recovered"] = each_div.xpath("/td[4]/text()").get()
        #     items["active"] =  each_div.xpath("/td[5]/text()").get()
        #     yield items
    
   
        
        