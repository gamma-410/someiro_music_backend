import requests
import math


def Note(username):
    url = "https://note.com/api/v2/creators/" + username + "/contents?kind=note&page=1"
    r = requests.get(url)
    jsonData = r.json()
    totalCount = jsonData["data"]["totalCount"]

    a = 0
    b = 1

    if totalCount >= 6:
        a = math.ceil(totalCount / 6)
    else:
        a = totalCount

    title = []
    key = []
    eyecatch = []
    audio = []
    audioDownload = []
    previewUrl = []

    while b <= a:
        url = "https://note.com/api/v2/creators/" + username + "/contents?kind=note&page=" + str(b)
        r = requests.get(url)
        jsonData = r.json()
        try:
            title.append(jsonData["data"]["contents"][0]["name"])
            key.append(jsonData["data"]["contents"][0]["key"])
            eyecatch.append(jsonData["data"]["contents"][0]["eyecatch"])
            audio.append(jsonData["data"]["contents"][0]["audio"]["url"])
            audioDownload.append(jsonData["data"]["contents"][0]["audio"]["urlForDownload"])
            previewUrl.append(jsonData["data"]["contents"][0]["audio"]["previewUrl"])
        except:
            pass
        try:
            title.append(jsonData["data"]["contents"][1]["name"])
            key.append(jsonData["data"]["contents"][1]["key"])
            eyecatch.append(jsonData["data"]["contents"][1]["eyecatch"])
            audio.append(jsonData["data"]["contents"][1]["audio"]["url"])
            audioDownload.append(jsonData["data"]["contents"][1]["audio"]["urlForDownload"])
            previewUrl.append(jsonData["data"]["contents"][1]["audio"]["previewUrl"])
        except:
            pass
        try:
            title.append(jsonData["data"]["contents"][2]["name"])
            key.append(jsonData["data"]["contents"][2]["key"])
            eyecatch.append(jsonData["data"]["contents"][2]["eyecatch"])
            audio.append(jsonData["data"]["contents"][2]["audio"]["url"])
            audioDownload.append(jsonData["data"]["contents"][2]["audio"]["urlForDownload"])
            previewUrl.append(jsonData["data"]["contents"][2]["audio"]["previewUrl"])
        except:
            pass
        try:
            title.append(jsonData["data"]["contents"][3]["name"])
            key.append(jsonData["data"]["contents"][3]["key"])
            eyecatch.append(jsonData["data"]["contents"][3]["eyecatch"])
            audio.append(jsonData["data"]["contents"][3]["audio"]["url"])
            audioDownload.append(jsonData["data"]["contents"][3]["audio"]["urlForDownload"])
            previewUrl.append(jsonData["data"]["contents"][3]["audio"]["previewUrl"])
        except:
            pass
        try:
            title.append(jsonData["data"]["contents"][4]["name"])
            key.append(jsonData["data"]["contents"][4]["key"])
            eyecatch.append(jsonData["data"]["contents"][4]["eyecatch"])
            audio.append(jsonData["data"]["contents"][4]["audio"]["url"])
            audioDownload.append(jsonData["data"]["contents"][4]["audio"]["urlForDownload"])
            previewUrl.append(jsonData["data"]["contents"][4]["audio"]["previewUrl"])
        except:
            pass
        try:
            title.append(jsonData["data"]["contents"][5]["name"])
            key.append(jsonData["data"]["contents"][5]["key"])
            eyecatch.append(jsonData["data"]["contents"][5]["eyecatch"])
            audio.append(jsonData["data"]["contents"][5]["audio"]["url"])
            audioDownload.append(jsonData["data"]["contents"][5]["audio"]["urlForDownload"])
            previewUrl.append(jsonData["data"]["contents"][5]["audio"]["previewUrl"])
        except:
            pass

        b += 1

    returnListData = []
    returnCount = 0

    while returnCount != len(title):
        returnJsonData = {
            'title': title[returnCount],
            'key': key[returnCount],
            'eyecatch': eyecatch[returnCount],
            # 'audio': audio[returnCount],
            # 'audioDownload': audioDownload[returnCount],
            # 'previewUrl': previewUrl[returnCount],
            # 'totalCount': len(title)
        }
        returnListData.append(returnJsonData)

        returnCount +=1

    return returnListData

def NoteDetail(id):
    url = "https://note.com/api/v1/notes/" + id
    r = requests.get(url)
    jsonData = r.json()
    return jsonData