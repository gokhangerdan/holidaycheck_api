import requests
import json
import pandas as pd


def holidaycheck(link):
    headers = {
        'cookie': 'optimizelyEndUserId=oeu1532910299436r0.6055594838654821; bd4ti=LUr53NGdvlcB.1532910445553; cto_lwid=b207a902-c69b-408c-9272-6330910a98aa; _wyidfp=ee60fbdc-38ed-4a12-8ba0-a9009ff27ace; _wyidfp=ee60fbdc-38ed-4a12-8ba0-a9009ff27ace; _ga=GA1.2.38128138.1532910447; remaffili=fe7c9290-f692-3e62-8520-0d5094c683d6; mobile_detected=false; ak_bmsc=2A1651BBAE927779CDDBDE142F5C2801173ADF2C99310000FFB67E5B18218D3B~plc7HzWFZGgurBuehjfeHKw09Cn2YvlJODFY4B9IWHYDMO91GeJGQOmqMjZWrJKtZpjN/FqPnm5alkxwXmLX5+xfpnELSKQxnwVQtIGGmL7tqtbmMYARG9Yx0EsgpZO1zEs65DNw0z3ynZGurC4555AD/HUVGxEUO5GySx9UIBNQRuPk1I0eSmfe+hE6cpT+CwFrTCbvYChFJnLA2m8I+7mm7fz1kGheupe/B2234NAX2oiTRygwpiFcdAEwZO6bhp; POPUPCHECK=1535117471968; _wysi=WY.1.763076688.2124536668; _wysi=WY.1.763076688.2124536668; _wysis=WY.1.763076688.2124536668; _wysis=WY.1.763076688.2124536668; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.1936398834.1535031080; _wybrs=1535031080047; _wybrs=1535031080047; bm_sv=D3B6284E39C3A87CFE60EA3BB10BA732~m/nwp0mVlHRR4Ocb6uE4j+HTB/WYzcGmREFb/jhXAoE0IImcpXOt/htQneak2CsxmcpA0ArLgzxotBimZ9H1F9kS6vrqspFjE8nkNoBM0ISPSVVW/p20sbcJWjLL9mnOfWgh9Rda1Os2PyYJ7nYKPhYpF3xwXgmjbePn1FKxmFQ=',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'accept': '*/*',
        'referer': link,
        'authority': 'www.holidaycheck.de',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = (
        ('returnMeta', 'true'),
    )

    response = requests.get('https://www.holidaycheck.de/api/hotel-reviews;filter=hotel.id%3A4c1305dc-cbe5-3761-a448-4487612ccc34%2CavailableLocales%3Ade;limit=10000;locale=de;offset=0;select=id%2Cuser%2Ctitle%2Ctexts%2CtextAdvice%2Chotel%2CtravelDate%2Crecommendation%2Cratings%2CproofedReservation%2CownerComment%2Carchived%2Cadditional%2CentryDate%2CtraveledWith%2CtravelReason%2CtravelDuration%2Cchildren;sort=travelDate%3Adesc%2CentryDate%3Adesc%2Cid%3Adesc', headers=headers, params=params)

    s = response.text
    d = json.loads(s)

    id = []
    title = []
    traveledWith = []
    # user
    userid, userfirstName, userhasPicture, userageGroup, userdestinationId = [], [], [], [], []
    entryDate = []
    travelDate = []
    hotel = []
    originalLocale = []
    returnedLocale = []
    recommendation = []
    archived = []
    proofedReservation = []
    # texts
    textsLOCATION, textsROOM, textsFOOD, textsHOTEL, textsSERVICE, textsSPORT = [], [], [], [], [], []
    # ratings
    ratingsGENERAL, ratingsLOCATION, ratingsROOM, ratingsFOOD, ratingsHOTEL, ratingsSERVICE, ratingsSPORT = [], [], [], [], [], [], []
    travelDuration = []
    travelReason = []
    children = []
    # additional
    additionaltourOperator, additionaltourOperatorName, additionalcostPerformance, additionalcatalogCorrect, additionalstarsCorrect, additionalroomType, additionalroomView, additionalroomCategory = [], [], [], [], [], [], [], []
    c = len(d["data"]["items"])
    for n, i in enumerate(d["data"]["items"]):
        id.append(i["id"])
        title.append(i["title"])
        traveledWith.append(i["traveledWith"])
        userid.append(i["user"]["id"])
        userfirstName.append(i["user"]["firstName"])
        userhasPicture.append(i["user"]["hasPicture"])
        userageGroup.append(i["user"]["ageGroup"])
        userdestinationId.append(i["user"]["destinationId"])
        entryDate.append(i["entryDate"])
        travelDate.append(i["travelDate"])
        hotel.append(i["hotel"])
        originalLocale.append(i["originalLocale"])
        returnedLocale.append(i["returnedLocale"])
        recommendation.append(i["recommendation"])
        archived.append(i["archived"])
        proofedReservation.append(i["proofedReservation"])
        try:
            textsLOCATION.append(i["texts"]["LOCATION"])
        except Exception as e:
            textsLOCATION.append(None)
        try:
            textsROOM.append(i["texts"]["ROOM"])
        except Exception as e:
            textsROOM.append(None)
        try:
            textsFOOD.append(i["texts"]["FOOD"])
        except Exception as e:
            textsFOOD.append(None)
        try:
            textsHOTEL.append(i["texts"]["HOTEL"])
        except Exception as e:
            textsHOTEL.append(None)
        try:
            textsSERVICE.append(i["texts"]["SERVICE"])
        except Exception as e:
            textsSERVICE.append(None)
        try:
            textsSPORT.append(i["texts"]["SPORT"])
        except Exception as e:
            textsSPORT.append(None)
        try:
            ratingsGENERAL.append(i["ratings"]["GENERAL"])
        except Exception as e:
            ratingsGENERAL.append(None)
        try:
            ratingsLOCATION.append(i["ratings"]["LOCATION"])
        except Exception as e:
            ratingsLOCATION.append(None)
        try:
            ratingsROOM.append(i["ratings"]["ROOM"])
        except Exception as e:
            ratingsROOM.append(None)
        try:
            ratingsFOOD.append(i["ratings"]["FOOD"])
        except Exception as e:
            ratingsFOOD.append(None)
        try:
            ratingsHOTEL.append(i["ratings"]["HOTEL"])
        except Exception as e:
            ratingsHOTEL.append(None)
        try:
            ratingsSERVICE.append(i["ratings"]["SERVICE"])
        except Exception as e:
            ratingsSERVICE.append(None)
        try:
            ratingsSPORT.append(i["ratings"]["SPORT"])
        except Exception as e:
            ratingsSPORT.append(None)
        travelDuration.append(i["travelDuration"])
        travelReason.append(i["travelReason"])
        children.append(i["children"])
        additionaltourOperator.append(i["additional"]["tourOperator"])
        additionaltourOperatorName.append(i["additional"]["tourOperatorName"])
        additionalcostPerformance.append(i["additional"]["costPerformance"])
        additionalcatalogCorrect.append(i["additional"]["catalogCorrect"])
        additionalstarsCorrect.append(i["additional"]["starsCorrect"])
        additionalroomType.append(i["additional"]["roomType"])
        additionalroomView.append(i["additional"]["roomView"])
        additionalroomCategory.append(i["additional"]["roomCategory"])
        print(c-n)

    df = pd.DataFrame({"id": id,
                       "title": title,
                       "traveledWith": traveledWith,
                       "userid": userid,
                       "userfirstName": userfirstName,
                       "userhasPicture": userhasPicture,
                       "userageGroup": userageGroup,
                       "userdestinationId": userdestinationId,
                       "entryDate": entryDate,
                       "travelDate": travelDate,
                       "hotel": hotel,
                       "originalLocale": originalLocale,
                       "returnedLocale": returnedLocale,
                       "recommendation": recommendation,
                       "archived": archived,
                       "proofedReservation": proofedReservation,
                       "textsLOCATION": textsLOCATION,
                       "textsROOM": textsROOM,
                       "textsFOOD": textsFOOD,
                       "textsHOTEL": textsHOTEL,
                       "textsSERVICE": textsSERVICE,
                       "textsSPORT": textsSPORT,
                       "ratingsGENERAL": ratingsGENERAL,
                       "ratingsLOCATION": ratingsLOCATION,
                       "ratingsROOM": ratingsROOM,
                       "ratingsFOOD": ratingsFOOD,
                       "ratingsHOTEL": ratingsHOTEL,
                       "ratingsSERVICE": ratingsSERVICE,
                       "ratingsSPORT": ratingsSPORT,
                       "travelDuration": travelDuration,
                       "travelReason": travelReason,
                       "children": children,
                       "additionaltourOperator": additionaltourOperator,
                       "additionaltourOperatorName": additionaltourOperatorName,
                       "additionalcostPerformance": additionalcostPerformance,
                       "additionalcatalogCorrect": additionalcatalogCorrect,
                       "additionalstarsCorrect": additionalstarsCorrect,
                       "additionalroomType": additionalroomType,
                       "additionalroomView": additionalroomView,
                       "additionalroomCategory": additionalroomCategory})
    return df

holidaycheck('https://www.holidaycheck.de/hr/bewertungen-horus-paradise-luxury-resort-club/4c1305dc-cbe5-3761-a448-4487612ccc34').to_csv("out.csv")
