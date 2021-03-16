import quipclient
import quip
import sys
from bs4 import BeautifulSoup
ACCESS_TOKEN = "SWRVQU1BcGlrTWQ=|1646283665|Lp3fCBq19jTs8xML5n7hsC0pe7PfM3vQNno1wAaulHQ=" # your access token
client = quipclient.QuipClient(access_token=ACCESS_TOKEN)
user = client.get_authenticated_user()
#print(user)
jso = client.get_thread(id="hYN3AMYjVq4Y")
print(len(jso))
#print(jso['html'])

soup = BeautifulSoup(jso['html'], "lxml")
print(soup.prettify())
#print(soup.title)
# def remove_html_tags(text):
#     """Remove html tags from a string"""
#     import re
#     clean = re.compile('<.*?>')
#     return re.sub(clean, '', text)
# print(remove_html_tags(jso['html']))


#gdp_table=soup.find("class", attrs={"id":"OAAACAFcIok"})
gdp_table = soup.find("table", attrs={"id":"OAAACA3MBfG"})
gdp_table_data = gdp_table.tbody.find_all("tr")
# print(gdp_table_data[0])
headings = []
for td in gdp_table_data[0].find_all("td"):
    # remove any newlines and extra spaces from left and right
    headings.append(td.text.replace('\n', ''))

print(headings)
print("here")
data = {}
for table in gdp_table_data[1].find_all("table"):
    for tr in table.tbody.find_all("tr"):
        trow = {}
        for td in tr.findAll("td"):
            print(td.text.replace('\n', '').strip())



