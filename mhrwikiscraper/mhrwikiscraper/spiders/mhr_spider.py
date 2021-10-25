import scrapy
import json

def linkGenerator(self):
        # Credit for this information and links go to Fextralife's and his community's very detailed information about all the monsters
        baseUrl = 'https://monsterhunterrise.wiki.fextralife.com/'
        monsters = ['Bishaten', 'Great+Wroggi','Magnamalo','Royal+Ludroth',
                   'Somnacanth','Goss+Harag','Lagombi','Khezu',
                   'Great+Baggi','Barioth','Mizutsune','Rathalos',
                   'Tigrex','Great+Izuchi','Arzuros','Tetranodon',
                   'Aknosom','Rathian','Rakna-Kadaki','Basarios',
                   'Volvidon','Almudron','Diablos','Rajang',
                   'Apex+Arzuros','Kulu-Ya-Ku','Barroth','Pukei-Pukei',
                   'Jyuratodus','Tobi-Kadachi','Anjanath','Nargacuga',
                   'Zinogre','Wind+Serpent+Ibushi','Apex+Rathian','Thunder+Serpent+Narwa',
                   'Chameleos','Apex+Rathalos','Apex+Mizutsune','Teostra',
                   'Kushala+Daora','Apex+Diablos','Bazelgeuse','Narwa+the+Allmother',
                   'Apex+Zinogre','Crimson+Glow+Valstrax']
        monsterUrls = []
        for monster in monsters:
            newUrl = baseUrl+monster
            monsterUrls.append(newUrl)
        return monsterUrls

class mhrSpider(scrapy.Spider):
    name = 'monsters'
    
    def start_requests(self):
        start_urls = linkGenerator(self)
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):
        #Multiple tables with class wiki table, I only want to use the information from the first one for now.
        #TODO: Not all the table data is arranged the same way unfortunately. Need to tinker some more 
        #with the function to categorize the information correctly and clean the data after scraping the html.
        table = response.xpath('//*[@class="wiki_table"]//tbody')[0]
        
        yield {
            'monster_name' : table.xpath('tr[1]/th/h2//text()').get(),
            'monster_type' : table.xpath('tr[4]/td[2]//text()').get(),
            'threat_level' : table.xpath('tr[5]/td[2]//text()').get(),
            'elements' : table.xpath('tr[6]/td[2]//text()').getall(),
            'ailments' : table.xpath('tr[7]/td[2]//text()').getall(),
            'weaknesses' : table.xpath('tr[8]/td[2]//text()').getall(),
            'resistances' : table.xpath('tr[9]/td[2]//text()').getall(),
            'habitats' : table.xpath('tr[10]/td[2]//text()').getall()
        }