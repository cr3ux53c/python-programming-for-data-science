import datetime

visitor_info =["Thanos", "Groot", "Dr.strange", "Captain America", "Spider Man"]
with open("cs50_click_stream.log", "a", encoding = "utf8" ) as f:
    for i in visitor_info:
        visit_time = datetime.datetime.now()
        f.write("userName : %s \t"%i + " visitedTime : %s \n"%str(visit_time))
f.close()
