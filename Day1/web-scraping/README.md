Files: 
	*stack
(* = Directory)
````````
Web scraping is performed using the scrapy python module. 
there are two spiders, one each for the news.ycombinator.com and stackoverflow.com. 

the spider for news.ycombinator.com scrapes the home webpage of the site for the text and url of the headline and stores the data in a mongo database

the spider for stackoverflow.com scrapes the latest questions page of the website for latest questions' text and their url. 

I studies the spider for stackoverflow.com through a web tutorial, upon which I built the required spider. 
````````
