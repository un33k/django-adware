from bs4 import BeautifulSoup


def get_adsense_attribute(html):
    ad_client = ''
    ad_slot = ''
    if html:
        soup = BeautifulSoup(html)
        tag = soup.find('ins')
        ad_client = tag.get('data-ad-client', '')
        ad_slot = tag.get('data-ad-slot', '')
    return ad_client, ad_slot
