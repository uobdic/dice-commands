import classad
from time import strftime, localtime


startd_history_file = "/mnt/p/DICE/incidents/2023.07.05/hd75/startd_history.other"

with open(startd_history_file) as f:
    lines = f.readlines()

ads = []

stop_at = "*** Offset"

current_ad = []
for line in lines:
    if line.startswith(stop_at):
        ads.append("\n".join(current_ad))
        current_ad = []
        continue
    current_ad.append(line)

cads = [classad.parseOne(ad) for ad in ads]
cms_ads = [cad for cad in cads if cad["Owner"].startswith("cms")]
cms_pilot_ads = [cad for cad in cms_ads if "pil" in cad["Owner"]]

ten_minutes_in_epoch = 600
event_time = 1688526720

rows = []
for ad in cms_pilot_ads:
    start_date = ad["JobStartDate"]
    end_date = ad["CompletionDate"]
    clusterid = ad["ClusterId"]
    JobCurrentStartDate = strftime('%Y-%m-%d %H:%M:%S', localtime(ad["JobCurrentStartDate"]))
    # if start_date < event_time or start_date < event_time + ten_minutes_in_epoch:
    # print(JobCurrentStartDate)
    rows.append([strftime('%Y-%m-%d %H:%M:%S', localtime(start_date)), strftime('%Y-%m-%d %H:%M:%S', localtime(end_date)),clusterid])
    # print(strftime('%Y-%m-%d %H:%M:%S', localtime(start_date)), strftime('%Y-%m-%d %H:%M:%S', localtime(end_date)),clusterid)

import tabulate
print(tabulate.tabulate(rows, headers=["Start", "End", "ClusterId"], tablefmt="psql"))
    
    
    # if end_date > 1688526720 and start_date < 1688526720 + ten_minutes_in_epoch:
    #     print(ad["CompletionDate"],clusterid)

# ad = classad.parseAds(content)

# for a in ad:
#     print(a["Owner"])

# while True:
#     print(ad["Owner"])
#     ad = classad.parseNext(content)
# print(len(ads[0]))

# for ad in ads:
#     print(ad["Owner"])

# print(ads)



