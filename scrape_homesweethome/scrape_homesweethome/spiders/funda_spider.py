import scrapy
import time
from scrape_homesweethome.items import HomeItem, ScreenshotItem, DistanceItem

# Conversion function 
def convert_currency_text_to_number(currency_text):
    currency_number = float(currency_text.replace('€','').replace(',',''))
    return currency_number

def convert_area_text_to_number(area_text):
    length_of_number = area_text.find(' ')
    area_number = float(area_text[:length_of_number].replace(',',''))
    return area_number

def convert_inclusive_signs_into_booleans(inclusive_sign):
    if inclusive_sign == '(ex.)':
        is_inclusive = True
    
    else:
        is_inclusive = False

    return is_inclusive




# Main parsing class
class FundaSpider(scrapy.Spider):
    name = "funda"

    start_urls = [
        'https://www.funda.nl/huur/amsterdam/',
    ]


    def parse(self, response):
        # #Follow links to each specific house
        for href in response.xpath("//div[contains(@class, 'search-result__header-title')]/div/a[@class='fd-flex']/@href"):
            time.sleep(3)
            print('traversing to house {}'.format(href))
            yield response.follow(href, self.parse_property)

        # Follow links to next page (maximum 5 pages)
        # for href in response.xpath("//li[@class='next']/a/@href"):
        #     page_number = href.get().split('-')[-1]
        #     if page_number == '6': # maximum page number
        #         break
        #     else:
        #         time.sleep(3)
        #         print('traversing to next page {}'.format(href))
        #         yield response.follow(href, self.parse)


    def parse_property(self,response):
        print("parse_property function triggered")


        # url_elements = response.url.split('/')
        # xpath_details_definition = "//*[@id='details']/dl/dd"
        

        # p = HomeItem()
        # p['id_from_website']            = url_elements[-2]
        # p['property_name']              = url_elements[-1]
        # p['street']                     = response.xpath(xpath_details_definition+'[3]/text()').get() 
        # p['region']                     = response.xpath(xpath_details_definition+'[1]/text()').get() 
        # p['postcode']                   = response.xpath(xpath_details_definition+'[2]/text()').get() 
        # p['price']                      = convert_currency_text_to_number(response.xpath(xpath_details_definition+'[5]/text()').get())
        # p['including_utilies']          = convert_inclusive_signs_into_booleans(response.xpath("//p[@class='price']/span[@class='inclusive']/text()").extract_first())  
        # p['area']                       = convert_area_text_to_number(response.xpath(xpath_details_definition+'[4]/text()').get())
        # p['number_of_bedrooms']         = response.xpath(xpath_details_definition+'[7]/text()').get() 
        # p['state_of_furnishing']        = response.xpath("//ul[@class='property-features']/li[@class='furniture']/text()").extract_first()
        # p['available_from']             = response.xpath(xpath_details_definition+'[6]/text()').get() 
        # p['offered_since']              = response.xpath(xpath_details_definition+'[8]/text()').get() 
        # p['energy_label']               = response.xpath("//a[contains(@class, 'energy-label')]/text()").extract_first()
        # p['description_from_tenant']    = response.xpath("//p[@class='text']/text()").extract_first()
        # p['tenant_contact_information'] = str(response.xpath("//a[contains(@class, 'telephone')]/@data-telephone").get())
        # p['property_website_source']    = 'Pararius'
        # p['property_source_url']        = response.url
        # homerecord = p.save()

        # # Save screenshot links
        # # first screenshot
        # link_to_active_screenshot = response.xpath('//ul[@id="photos"]/li/img/@src').get()
        # s = ScreenshotItem(link=link_to_active_screenshot, 
        #                     home = homerecord
        #                     )
        # s.save()
                                
        
        # # The rest of the screenshot
        # list_of_inactive_screenshot = response.xpath('//ul[@id="photos"]/li/img/@data-src').getall()
        # for link in list_of_inactive_screenshot:
        #     s = ScreenshotItem(link=link, 
        #             home = homerecord
        #             )
        #     s.save()


    


