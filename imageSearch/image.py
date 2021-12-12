import OlivOS
import imageSearch
import requests
from lxml import etree

def searchImagebyUrl(img_url):
    url = "https://saucenao.com/search.php"
    #files = {'name': (<filename>, <file object>,<content type>, <per-part headers>)}
    files={'file':('',None,'application/octet-stream'),
           'url':(None,img_url),
           'frame':(None,1),
           'hide':(None,0),
           'database':(None,999)
    }
    try:
        response=requests.post(url,files=files)
    except Exception as e:
        return e
    else:
        html = etree.HTML(response.text)
        result = html.xpath("/html/body/div[2]/div[3]/*")
        if result[2].xpath("@class")[0] != 'result hidden':
            result_list = html.xpath('/html/body/div[2]/div[3]/*[@class="result"]')


            result_num = len(result_list)
            for i in range(0, result_num):
                if html.xpath('/html/body/div[2]/div[3]/div['+ str(i + 2) +']/@id') and html.xpath('/html/body/div[2]/div[3]/div['+ str(i + 2) +']/@id')[0] == 'result-hidden-notification':
                    result_num = result_num - 1



            output = "find" + str(result_num)
            if result_num > 3:
                result_num = 3
            output += ",show" + str(result_num) + "\n"


            for i in range(0, result_num):
                creator_xpath = '/html/body/div[2]/div[3]/div['+ str(i + 2) +']/table/tr/td[2]/div[2]/div[1]'
                source_xpath = '/html/body/div[2]/div[3]/div['+ str(i + 2) +']/table/tr/td[2]/div[2]/div[2]'
                similarity_xpath = '/html/body/div[2]/div[3]/div['+ str(i + 2) +']/table/tr/td[2]/div[1]/div[1]'
                image_url_xpath = '/html/body/div[2]/div[3]/div['+ str(i + 2) +']/table/tr/td[1]/div/a/img'

                creator = "[" + html.xpath(similarity_xpath + '/text()')[0] + "]" 
                if html.xpath(creator_xpath + '/strong/text()')[0]:
                    creator += html.xpath(creator_xpath + '/strong/text()')[0]
                if html.xpath(creator_xpath + '/text()'):
                    creator += html.xpath(creator_xpath + '/text()')[0]
                output += creator + "\n"
                if html.xpath(image_url_xpath + '/@src')[0]:
                    image_code = "[CQ:image,file=" + html.xpath(image_url_xpath + '/@src')[0] + "]" + "\n"
                output += image_code
                source = html.xpath(source_xpath + '/strong[1]/text()')[0] + html.xpath(source_xpath + '/a/text()')[0] + "\n"
                source += html.xpath(source_xpath + '/strong[2]/text()')[0]
                if html.xpath(source_xpath + '/text()'):
                    source += html.xpath(source_xpath + '/text()')[0]
                else:
                    source += html.xpath(source_xpath + '/a[2]/text()')[0]
                source += "\n" + html.xpath(source_xpath + '/a/@href')[0] + "\n"
                output += source
            return output
        else:
            output = "未检索到符合的图片"
            return output
