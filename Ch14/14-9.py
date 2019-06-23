title_list = re.findall(("link_txt">)(.+)(</a>)", html_contents)
for title in title_list:
    print (title)
