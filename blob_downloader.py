import requests
import subprocess
import os

urlsource = 'https://cp3.hboav.com/check/hbo7/hls/files/mp4/M/L/U/MLUl8.mp4/'
folderName = 'football'
folderPathName = os.getcwd() + \
    "\\{}\\".format(folderName)


try:
    os.makedirs(folderPathName)
except:
    pass

url_list = ["{}seg-{}-v1-a1.ts".format(urlsource, i) for i in range(1, 100)]
for u in url_list:
    fileName = u.split('/')[-1]
    filePathName = folderPathName+fileName
    with open(filePathName, "wb") as f:
        r = requests.get(u, stream=True)
        for chunk in r.iter_content():
            f.write(chunk)
        print("{} done".format(fileName))

print("完成")
