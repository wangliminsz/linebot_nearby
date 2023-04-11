import requests
import random

from arapp.models import mbkkaround

# results["name"]
# results["geometry"]["location"]["lat"]
# results["geometry"]["location"]["lng"]

# results["photos"]["height"]
# results["photos"]["width"]
# results["photos"]["photo_reference"]

# results["vicinity"]
# results["rating"]

# locName = results["name"]
# locLat = results["geometry"]["location"]["lat"]
# locLng = results["geometry"]["location"]["lng"]
# locRating = results["rating"]
# locAddress = results["vicinity"]
# locPhoto_reference = results["photos"]["photo_reference"]
# locPhoto_width = results["photos"]["width"]
# locPhotoUrl = "https://maps.googleapis.com/maps/api/place/photo?key={}&photoreference={}&maxwidth={}".format(GOOGLE_API_KEY,locPhoto_reference,locPhoto_width)

# thumbnail_image_url="https://maps.googleapis.com/maps/api/place/photo?key={}&photoreference={}&maxwidth={}".format(GOOGLE_API_KEY,photo_reference,photo_width)
# map_url="https://www.google.com/maps/search/?api=1&query={lat}, {long}&query_place_id={place_id}".format(lat=location["geometry"]["location"]["lat"], long=location["geometry"]["location"]["lng"],place_id=location["place_id"])

# Elements Srinakarin
# 13.69642131796132,
# 100.64538084064222

# the Privacy Rama9
# 13.74455317945146,
# 100.60296055413663


# ?key={}&location={},{}&...&...&...".format(GOOGLE_API_KEY,lat,lng)
# &keyword=chinese
# &rankby=distance
# &location=13.69642131796132%2C100.64538084064222
# &type=restaurant
# &key=
# &language=zh-TW
# &radius=6000

# # ------------------------------------------------------


def locationData(locUser, latP, lngP):

    userInfo = mbkkaround.objects.filter(mbuserid=locUser).last()
    lat = latP
    lng = lngP


#     2022-02-20 ---------------------
#     kWordList = ["airport" , "aquarium" , "bowling_alley" , "casino" , "cemetery" , "courthouse" , "funeral_home" , "light_rail_station" , "painter" , "synagogue" , "taxi_stand" , "zoo"]
#     2022-02-20 ---------------------

    GOOGLE_API_KEY = "AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg"
    finalRadius = userInfo.mbradius


    resultList = []

    if userInfo.mbradius == 0:

        if userInfo.mbmethod == 1:
                # kWord = userInfo.mbkword
                gmap_Example = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=" + userInfo.mbkword + "&rankby=distance&key={}&location={},{}".format(GOOGLE_API_KEY,lat,lng)
                # print('url keyword-----------------')
                # print(gmap_Example)

        if userInfo.mbmethod == 2:
                # kWord = userInfo.mbkword
                gmap_Example = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=" + userInfo.mbkword + "&type=" + userInfo.mbtype + "&rankby=distance&key={}&location={},{}".format(GOOGLE_API_KEY,lat,lng)
                print('url keyword type-----------------')
                print(gmap_Example)


        if userInfo.mbmethod == 3:
                gmap_Example = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?type=" + userInfo.mbtype + "&rankby=distance&key={}&location={},{}".format(GOOGLE_API_KEY,lat,lng)

    else:

        if userInfo.mbmethod == 1:
                # kWord = userInfo.mbkword
                gmap_Example = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=" + userInfo.mbkword + "&radius={}&key={}&location={},{}".format(finalRadius, GOOGLE_API_KEY,lat,lng)
                print('radius keyword-----------------')
                print(gmap_Example)

        if userInfo.mbmethod == 2:
                # kWord = userInfo.mbkword
                gmap_Example = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=" + userInfo.mbkword + "&type=" + userInfo.mbtype + "&radius={}&key={}&location={},{}".format(finalRadius, GOOGLE_API_KEY,lat,lng)
                print('url keyword type-----------------')
                print(gmap_Example)


        if userInfo.mbmethod == 3:
                gmap_Example = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?type=" + userInfo.mbtype + "&radius={}&key={}&location={},{}".format(finalRadius, GOOGLE_API_KEY,lat,lng)
                print('radius keyword-----------------')
                print(gmap_Example)

    # resultDict = {"locId": 0, "locName": "", "locLat": 0, "locLng": 0, "locRating": None, "locAddress": "",  "locPhotoUrl": ""}

#     2022-02-20 ---------------------

#     if userInfo.mbtype in kWordList:

#         gmap_Example = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=" + userInfo.mbtype + "&rankby=distance&key={}&location={},{}".format(GOOGLE_API_KEY,lat,lng)

#     else:
#         gmap_Example = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?type=" + userInfo.mbtype + "&rankby=distance&key={}&location={},{}".format(GOOGLE_API_KEY,lat,lng)
#         print(gmap_Example)

#     2022-02-20 ---------------------

    destSearch = gmap_Example

    destReq = requests.get(destSearch)
    nearby_Facility_dict = destReq.json()
    nearby_Facility_20 = nearby_Facility_dict ["results"]
    result_Num = len(nearby_Facility_20)

    # print(nearby_Facility_20)
    # print('20-------------------------------------------')
    # print(result_Num)
    # print('20-------------------------------------------')


    for i in range(result_Num):

        # resultDict = {"locId": 0, "locName": "", "locLat": 0, "locLng": 0, "locRating": None, "locAddress": None,  "locPhotoUrl": None}
        resultDict = {}


        if nearby_Facility_20[i]:

            resultDict["locId"] = i
            resultDict["locName"] = nearby_Facility_20[i]["name"]
            resultDict["locLat"] = nearby_Facility_20[i]["geometry"]["location"]["lat"]
            resultDict["locLng"] = nearby_Facility_20[i]["geometry"]["location"]["lng"]
    #             # resultDict["locRating"] = nearby_Facility_20[i]["rating"]
    #             # resultDict["locAddress"] = nearby_Facility_20[i]["vicinity"]

    # Cal Distance -------------------------------------------------------------------------

            latL = nearby_Facility_20[i]["geometry"]["location"]["lat"]
            lngL = nearby_Facility_20[i]["geometry"]["location"]["lng"]

            latDiff = abs(latL - lat)
            lngDiff = abs(lngL - lng)
            totalDiff = pow(latDiff, 2) + pow(lngDiff, 2)

            myDistance = pow(totalDiff, 0.5)
            resultDict["locDistance"] = myDistance

            myDistanceStr = str(round(139.276 * myDistance, 2)) + " km"
            resultDict["locDistanceStr"] = myDistanceStr

    # Cal Distance -------------------------------------------------------------------------

            resultDict["locRating"] = 0 if nearby_Facility_20[i].get("rating") is None else nearby_Facility_20[i]["rating"]
    #             resultDict["locAddress"] = None if nearby_Facility_20[i].get("vicinity") is None else nearby_Facility_20[i]["vicinity"]

            if nearby_Facility_20[i].get("photos") is None:
                    resultDict["locPhotoUrl"] = None
            else:
                resultDict["locPhoto_reference"] = nearby_Facility_20[i]["photos"][0]["photo_reference"]
                resultDict["locPhoto_width"] = nearby_Facility_20[i]["photos"][0]["width"]
                resultDict["locPhotoUrl"] = "https://maps.googleapis.com/maps/api/place/photo?key={}&photoreference={}&maxwidth={}".format(GOOGLE_API_KEY,resultDict["locPhoto_reference"], resultDict["locPhoto_width"])

    #             ###

            resultList.append(resultDict)
            # print(resultList)
            # print("resultList -------------------------------------------")

    if userInfo.mbmethod == 1:
        resultRateList = resultList

    if userInfo.mbmethod == 2:
        resultRateList = resultList

    if userInfo.mbmethod == 3:
        resultRateList = sorted(resultList, key=lambda x: x['locRating'], reverse=True)
        # print(resultRateList)
        # print('sorted ---------------------------------------------')

    return (resultRateList, result_Num)

    # ---------------------------------------------------------------


#     top20_locations = nearby_locations_dict["results"]
#     res_num = (len(top20_locations))

#     #取得評分高於3.9的店家位置

#     bravo=[]

#     for i in range(res_num):

#         try:
#             if top20_locations[i]['rating'] > 3.9:

#                 bravo.append(i)

#         except:

#             KeyError

#     if len(bravo) < 0:

#         content="Not found"

# # ------------------------------------------------------

#     # location = random．choice(top20＿locations)沒有的話隨便選一間 #從高於3.9的店家隨機選一間
#     # location = top20_locations[random.choice(bravo)]

#     #檢查餐廳有沒有照片，有的話會顯示
#     # if location.get("photos") is None:
#     #     thumbnail_image_url =None

#     # else:
#     # # 根據文件，最多只會有一張照片
#     #     photo_reference = location["photos"][0]["photo_reference"]
#     #     photo_width = location["photos"][0]["width"]
#     #     thumbnail_image_url="https://maps.googleapis.com/maps/api/place/photo?key={}&photoreference={}&maxwidth={}".format(GOOGLE_API_KEY,photo_reference,photo_width)

#     # rating = "No rating" if location.get("rating") is None else location["rating"]

#     # address ="No Address" if location.get("vicinity") is None else location["vicinity"]

#     # details = "Google Map rating:{}\nAddress:{}".format(rating, address)

#     # #取得餐廳的 Google map 網址

#     # map_url="https://www.google.com/maps/search/?api=1&query={lat}, {long}&query_place_id={place_id}".format(lat=location["geometry"]["location"]["lat"], long=location["geometry"]["location"]["lng"],place_id=location["place_id"])