import scrapy
import sys
from scrapy.crawler import CrawlerProcess
from scrapy.dupefilters import RFPDupeFilter
import os
sys.path.append("..")
from items import MirPhase3Item
import re

cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')


def cleanhtml(raw_html):
    global cleanr
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def find_authors(s):
    sprim = s[s.find("author"):]
    return list(map(str.strip, sprim[sprim.find("{") + 1: sprim.find(",") - 1].split(" and ")))


class myspider(scrapy.Spider):
    # custom_settings = {
    #
    # }

    def add_home_url(self, s):
        return "https://www.semanticscholar.org" + s

    items = MirPhase3Item()
    name = "my_cute_spider"

    def parse(self, response):
        references = response.css('#references .citation__title a::attr(href)')[:min(20,
                                                                                     len(response.css(
                                                                                         '#references .citation__title span::text'))):1].extract()
        references = list(map(self.add_home_url, references))
        for next_page in references:
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse, dont_filter=False)

        references = list(map(lambda s: s[s.rindex("/") + 1:], references))

        abstract = response.xpath("//meta[@name='description']/@content").extract()

        id = response.request.url
        id = id[id.rindex("/") + 1:]
        title = response.css('h1::text').extract()

        authors = find_authors(response.css('pre.bibtex-citation::text').extract()[0])
        date = response.css('.bibtex-citation::text').extract()[0]
        date = date[date.find('year=') + 6: date.find('year=') + 10]
        try:
            date = int(date)
        except ValueError:
            date = 1940
        abstract = cleanhtml(abstract[0]) + " " + cleanhtml(abstract[1]) if len(abstract) > 1 else \
            cleanhtml(abstract[0]) if len(abstract) > 0 else ""
        title = cleanhtml(title[0]) if len(title) > 0 else ""

        self.items['id'] = id
        self.items['title'] = title
        self.items['authors'] = authors
        self.items['date'] = date
        self.items['abstract'] = abstract
        self.items['references'] = references

        yield self.items


if os.path.exists("result.json"):
    os.remove("result.json")

# start_url = [
#         "https://www.semanticscholar.org/paper/The-Lottery-Ticket-Hypothesis%3A-Training-Pruned-Frankle-Carbin/f90720ed12e045ac84beb94c27271d6fb8ad48cf",
#         "https://www.semanticscholar.org/paper/Attention-is-All-you-Need-Vaswani-Shazeer/204e3073870fae3d05bcbc2f6a8e263d9b72e776",
#         "https://www.semanticscholar.org/paper/BERT%3A-Pre-training-of-Deep-Bidirectional-for-Devlin-Chang/df2b0e26d0599ce3e70df8a9da02e51594e0e992"]

item_limit = int(input("Enter page limit\n"))
start_urls = []
n = int(input("How many start urls?\n"))
print("Enter", n, "urls, one in each line")
for i in range(n):
    url = input().strip("\n")
    start_urls.append(url)

process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'result.json',
        # 'DEPTH_LIMIT': 5,
        'CLOSESPIDER_PAGECOUNT': item_limit,
        'DUPEFILTER_CLASS': 'scrapy.dupefilters.RFPDupeFilter',
        'CONCURRENT_REQUESTS': 32,
})
process.crawl(myspider, start_urls=start_urls)
process.start()
