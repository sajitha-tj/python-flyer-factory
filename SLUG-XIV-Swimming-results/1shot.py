import os
# import pandas as pd
from PIL import Image, ImageFont, ImageDraw


UniDictionary = {"SJP" : "University of Sri Jayewardenepura - SJP",
                 "USJ" : "University of Sri Jayewardenepura - SJP",
                 "COL" : "University of Colombo - COL",
                 "UOC" : "University of Colombo - COL",
                 "PER":"University of Peradeniya - PER",
                 "UOP":"University of Peradeniya - PER",
                 "KEL":"University of Kelaniya - KEL",
                 "UOK":"University of Kelaniya - KEL",
                 "JAF":"University of Jaffna - JAF",
                 "UOJ":"University of Jaffna - JAF",
                 "MOR":"University of Moratuwa - MOR",
                 "UOM":"University of Moratuwa - MOR",
                 "RUH":"University of Ruhuna - RUH",
                 "UOR":"University of Ruhuna - RUH",
                 "VAU":"University of Vavuniya - VAU",
                 "VAV":"University of Vavuniya - VAU",
                 "SAB":"Sabaragamuwa University of Sri Lanka - SAB",
                 "WAY":"Wayamba University of Sri Lanka - WAY",
                 "WYB":"Wayamba University of Sri Lanka - WAY",
                 "RAJ":"Rajarata University of Sri Lanka - RAJ",
                 "RJT":"Rajarata University of Sri Lanka - RAJ",
                 "UVA":"Uva Wellassa University - UVA",
                 "UVU":"Uva Wellassa University - UVA",
                 "EST":"Eastern University of Sri Lanka - EST",
                 "EU":"Eastern University of Sri Lanka - EST",
                 "SEU":"South Eastern University of Sri Lanka - SEU",
                 "SEA":"South Eastern University of Sri Lanka - SEU",
                 "VPA":"University of Visual & Performing Arts - VPA",
                 "GWU":"Gampaha Wickramarachchi University - GWU",
                 "GWA":"Gampaha Wickramarachchi University - GWU"
                }

dir_path = os.path.dirname(os.path.realpath(__file__))

def getUniLogo(uniNameShort):
    if UniDictionary.get(uniNameShort) == None:
        print(f'Error in excel file. Please check the name of {uniNameShort}')
        exit()
    else:
        uniName = UniDictionary.get(uniNameShort)
    
    if len(uniName.split(" - ")) > 1:
        uniTag = uniName.split(" - ")[1]
    else:
        uniTag = uniName.split(" - ")[1]

    uniLogo = Image.open(f'{dir_path}/uni_logos/{uniTag}.png').convert("RGBA")

    uniLogo = uniLogo.resize((140,140))

    if len(uniName.split(" - ")) > 1:
        uniName = uniName.split(" - ")[0]
    else:
        uniName = uniName.split(" - ")[0]

    return (uniTag, uniLogo)

def seperateInput(inputString):
    # inputString = "M. M. Kottearachchi UOC 00.37.61"

    playerName = inputString.split(" - ")[0:-1]
    playerName = " ".join(playerName)
    uniName = inputString.split(" - ")[-1]
    # time = inputString.split(" ")[-1]
    # time = time.split(".")
    # ss = time[-1]
    # mm = time[-2]
    # hh = time[-3]
    # time = f"{hh}:{mm}.{ss}"
    print(playerName, uniName)
    return (playerName, uniName)

# sportName = input("Enter the sport name: ")
sportName = "tk"

if(sportName == "km"):
    sportName = "karatem"

elif(sportName == "kw"):
    sportName = "karatew"

elif(sportName == "w"):
    sportName = "wrestling"

elif(sportName == "tk"):
    sportName = "tk"


category = input("Enter the category: ")
categoryS = category
# category = "200M Individual Medley Women Final"

numOfPlayers = int(input("Enter the number of players: "))
# numOfPlayers = 3
if not (numOfPlayers == 3 or numOfPlayers == 5 or numOfPlayers == 4):
    print("Error! invalid number player")
    exit()


placeFont = ImageFont.truetype(f'{dir_path}/fonts/RadwaveFont-Demo.otf',90)
uniNameFont = ImageFont.truetype(f'{dir_path}/fonts/Montserrat-Medium.ttf',45)
playerFont = ImageFont.truetype(f'{dir_path}/fonts/Montserrat-ExtraBold.ttf',65)
timeFont = ImageFont.truetype(f'{dir_path}/fonts/Montserrat-Bold.ttf',70)
categoryFont = ImageFont.truetype(f'{dir_path}/fonts/Montserrat-Bold.ttf',40)

#category
templateCategory = Image.open(f'{dir_path}/imgs/categoryBG.png').convert("RGBA")
tcw,tch = templateCategory.size

editable_templateCategory = ImageDraw.Draw(templateCategory)
category = category.upper()

textWidth = editable_templateCategory.textlength(category,font=categoryFont)
templateCategory = templateCategory.resize((int(textWidth+100),tch))
tcw,tch = templateCategory.size
editable_templateCategory = ImageDraw.Draw(templateCategory)
editable_templateCategory.text((50,8),category,(0,0,0),categoryFont)

templateCategory.save(f'{dir_path}/results/category.png')


# creating each score card
for i in range(numOfPlayers):
    templateScore = Image.open(f'{dir_path}/imgs/scoreCardBG.png').convert("RGBA")

    if sportName == "karatem" or sportName == "karatew":
        templateScore = Image.open(f'{dir_path}/imgs/scoreCardBGK.png').convert("RGBA")    

    tw,th = templateScore.size

    editable_templateScore = ImageDraw.Draw(templateScore)

    inputString = input(f"Enter the details of player {i+1}: ").upper()

    playerName, uniName = seperateInput(inputString)

    # playerName = input(f"Enter the names of player {i+1}: ").upper()
    # # playerName = "Sajitha Jayawickrama"
    # uniName = input(f"Enter the university of player {i+1}: ").upper()
    # # uniName = "SJP"
    # time = input(f"Enter the time of player {i+1}: ").upper()
    # # time = "45:03.20"

    if i==0:
        place = "1ST"
    elif i==1:
        place = "2ND"
    elif i==2:
        place = "3RD"
    # elif i==3 and (sportName == "karatem" or sportName == "karatew"):
    #     place = "3RD"
    # elif i==3 and (sportName != "karatem" or sportName != "karatew"):
    #     place = "4TH"
    elif i==3 :
        place = "3RD"
    else:
        place = "5TH"

    un, uniLogo = getUniLogo(uniName)
    un = un.upper()

    templateScore.paste(uniLogo,(105,88),uniLogo)

    editable_templateScore.text((300,105),playerName,(255,255,255),playerFont)

    editable_templateScore.text((300,170),un,(255,255,255),uniNameFont)

    editable_templateScore.text((1340,120),place,(255,255,255),placeFont)

    # textWidth = editable_templateScore.textlength(time,font=timeFont)
    # editable_templateScore.text(((tw-textWidth-155),197),time,(143,196,251),timeFont)

    templateScore.save(f'{dir_path}/results/match{i}.png')

    print(f'{i+1} of {numOfPlayers} result created!')

# creating the final image
background = Image.open(f'{dir_path}/imgs/{sportName}BG.jpg').convert("RGBA")
W,H = background.size

category = Image.open(f'{dir_path}/results/category.png').convert("RGBA")
cw,ch = category.size
background.paste(category,(int((W-cw)/2),390),category)

conut = 1

if numOfPlayers == 3:
    # match = Image.open(f'{dir_path}/results/match0.png')
    # w,h = match.size
    # match = match.resize((int(w*1.2),int(h*1.2)))
    # w,h = match.size
    # background.paste(match,(int((W-w)/2),520),match)

    for i in range(numOfPlayers):
        match = Image.open(f'{dir_path}/results/match{i}.png').convert("RGBA")
        w,h = match.size
        background.paste(match,(int((W-w)/2),int(((H-((h+70)*numOfPlayers))*(conut+1)/2)-160)),match)
        conut+=1
        print(f'{conut} of {numOfPlayers} result pasted!')

elif numOfPlayers == 4:

    for i in range(numOfPlayers):
        match = Image.open(f'{dir_path}/results/match{i}.png').convert("RGBA")
        w,h = match.size
        background.paste(match,(int((W-w)/2),int(((H-((h-15)*numOfPlayers))*(conut+1)/2)-130)),match)
        conut+=1
        print(f'{conut} of {numOfPlayers} result pasted!')

elif numOfPlayers == 5:
    match = Image.open(f'{dir_path}/results/match0.png')
    w,h = match.size
    match = match.resize((int(w*1.2),int(h*1.2)))
    w,h = match.size
    background.paste(match,(int((W-w)/2),340),match)

    for i in range(numOfPlayers-1):
        match = Image.open(f'{dir_path}/results/match{i+1}.png').convert("RGBA")
        w,h = match.size
        background.paste(match,(int((W-w)/2),int(((H-((h-80)*numOfPlayers))*(conut+1)/2)+120)),match)
        conut+=1
        print(f'{conut} of {numOfPlayers} result pasted!')

background.save(f'{dir_path}/{sportName}-{categoryS}.png')

# editable_templateScore.text((365,145),f"After completion of {numOfGames} games".upper(),(0,0,0),boldFont)







print("Exit..")
exit()