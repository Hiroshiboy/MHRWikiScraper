# MHRWikiScraper
I was just building this as a support for one of my other projects and didn't know how to scrape a webpage before. 
It's a fun little script using Python3 and Scrapy to pull basic information about a monster in Monster Hunter Rise (Name, Species, Threat Level, etc.).
It still needs some work in my opinion as I am still manually cleaning the data currently.

# Why is the script not running?
This project as mentioned earlier uses python and scrapy so, I am assuming you know how to install, 
create a virtual environment and recreate the environment with the requirements.txt file within the git.
If not click [here](https://docs.scrapy.org/en/latest/intro/install.html).
That link contains both a guide for installing scrapy and a link to another article of how to setup a Python3 virtual environment.

The website the script pulls the information from is https://monsterhunterrise.wiki.fextralife.com/Monsters run by Fextralife and his community. 
They cover much more content and guides for other games as well than just Monster Hunter.

To run the script use this command ```scrapy crawl monsters -o monsters.json``` with your virtual environment enabled 
You should then receive an uncleaned (currently) json file that contains data from the wiki about the monster.

# TODO: Clean the data after retrieval
* Some of the data is not in the same place as other monsters so the data ends up scrambled and miss-categorized



