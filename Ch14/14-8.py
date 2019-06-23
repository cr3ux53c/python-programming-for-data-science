import urllib.request
import re

url = "http://www.google.com/googlebooks/uspto-patents-grants-text.html" #1
url 값 입력
html = urllib.request.urlopen(url)
html_contents = str(html.read().decode("utf8"))

url_list = re.findall(r"(http)(.+)(zip)", html_contents)
for url in url_list:
    full_url = "".join(url)
    print(full_url)
    fname, header = urllib.request.urlretrieve(full_url, file_name)
    print ("End Download")
