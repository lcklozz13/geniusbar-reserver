from utils import debug
from utils.webpage import WebPage


class StorePage(WebPage):
    storeNumber = None
    headers = {}
    postData = {}
    appleId = ''
    accountPassword = ''
    governmentId = ''

    def __init__(self, url, data=None,
                 headers={},
                 charset='utf-8',
                 timeout=100):
        super(StorePage, self).__init__(url, data, headers, charset, timeout)
        
    def get_tag_value(self, tagLabel, attrs):
        soup = self.get_soup()
        try:
            tag = soup.find(tagLabel, attrs=attrs)
            return tag.get('value').encode('utf-8')
        except AttributeError as e:
            debug.info('%s %s' % (tagLabel, str(attrs)))
            return ''

    @classmethod
    def set_user_data(self, appleId, passwd, governmentId):
        StorePage.accountPassword = passwd
        StorePage.appleId = appleId
        StorePage.governmentId = governmentId

    @classmethod
    def _init_headers(self):
        StorePage.headers['Accept-Language'] = 'zh-cn,zh;q=0.8,en-us;q=0.5,\
en;q=0.3'

        StorePage.headers['User-Agent'] = "Mozilla/5.0 (Windows \
NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0"

        StorePage.headers['Accept'] = 'text/html,application/xhtml+xml,\
application/xml;q=0.9,*/*;q=0.8'
        StorePage.headers["Connection"] = 'keep-alive'

class GeniusbarPage(StorePage):
    geniusbarBaseUril = "http://concierge.apple.com/geniusbar/"
    def __init__(self, url, data=None,
                 headers={},
                 charset='utf-8',
                 timeout=100):
        super(GeniusbarPage, self).__init__(url, data, headers,
                                            charset,
                                            timeout)


    def get_formtoken_value(self):
        attrs = {'name': '_formToken'}
        return self.get_tag_value('input', attrs=attrs)

    def get_store_list(self):
            attrs = {"id": "cnstores", "class": "listing"}
            soup = self.get_soup()
            tag = soup.find('div', attrs=attrs)
            hrefs = tag.findAll('a')
            suburl = None
            storeName = None
            data = {}
            index = 1
            for href in hrefs:
                suburl = href.get('href').encode('utf-8')
                storeName = href.text.encode('gbk', 'ignore')
                data[index] = (storeName, suburl)
                index += 1
            return data

    @classmethod
    def get_geniusbar_url(self):
        return GeniusbarPage.geniusbarBaseUril + GeniusbarPage.storeNumber

    def build_auth_post_data(self):
        tag_names = ['Env', 'appIdKey', 'captchaType', 'captchaToken',
                     'grpCode', 'language', 'iForgotNewWindowVar',
                     'paramcode', 'path', 'path2', 'segment']
        postData = {}
        for tag in tag_names:
            postData[tag] = self.get_tag_value("input", {'id': tag})
        return postData

    def build_governmentid_post_data(self):
        postData = {}
        postItems = ['clientTimezone', 'FirstName', 'LastName']
        for item in postItems:
            postData[item] = self.get_tag_value('input', {'id': item})
        return postData

    def build_smschallenge_post_data(self, serviceType):
        postData = {}
        postItems=['clientTimezone']
        for item in postItems:
            postData['clientTimezone'] = self.get_tag_value('input', {'id': item})

        # find service spantag
        spantag = self.get_soup().find('a', attrs={'id': serviceType})
        attrs = {'class': 'NSCSSStateHidden value', "name": "id"}
        idtag = spantag.find('span', attrs=attrs)
        postData['id'] = idtag.text
        postData['_formToken'] = self.get_formtoken_value()
        return postData
