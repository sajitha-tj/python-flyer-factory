import os
# import pandas as pd
from PIL import Image, ImageFont, ImageDraw


UniDictionary = {"SJP" : "University of Sri Jayewardenepura - SJP",
"COL" : "University of Colombo - COL",
"PER":"University of Peradeniya - PER",
"KEL":"University of Kelaniya - KEL",
"JAF":"University of Jaffna - JAF",
"MOR":"University of Moratuwa - MOR",
"RUH":"University of Ruhuna - RUH",
"VAU":"University of Vavuniya - VAU",
"VAV":"University of Vavuniya - VAU",
"SAB":"Sabaragamuwa University of Sri Lanka - SAB",
"WAY":"Wayamba University of Sri Lanka - WAY",
"RAJ":"Rajarata University of Sri Lanka - RAJ",
"UVA":"Uva Wellassa University - UVA",
"UVU":"Uva Wellassa University - UVA",
"EST":"Eastern University of Sri Lanka - EST",
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

    uniLogo = uniLogo.resize((175,175))
    return (uniTag, uniLogo)


sportName = input("Enter the sport name: ").lower()

numOfGames = int(input("Enter the number of games: "))
# numOfGames = 1
if numOfGames > 4:
    print("Error! Maximum number of games is 4")
    exit()


scoresFont = ImageFont.truetype(f'{dir_path}/fonts/RadwaveFont-Demo.otf',112)
uniNameFont = ImageFont.truetype(f'{dir_path}/fonts/Montserrat-Bold.ttf',80)
winningFont = ImageFont.truetype(f'{dir_path}/fonts/Montserrat-ExtraBold.ttf',75)

# creating each score card
for i in range(numOfGames):
    templateScore = Image.open(f'{dir_path}/imgs/scoresBG.png').convert("RGBA")

    editable_templateScore = ImageDraw.Draw(templateScore) 
    
    uniNames = input(f"Enter the names of the universities(ex: SJP EST): ")
    # uniNames = "sjp est"
    un1,un2 = uniNames.split(" ")
    un1 = un1.upper()
    un2 = un2.upper()
    scores = input(f"Enter the scores of {un1} and {un2}(ex: 1 2): ")
    # scores ="1 3"
    s1,s2 = scores.split(" ")

    if s1 > s2:
        winningTeam = un1
    else:
        winningTeam = un2

    # isWinningTeam = input(f"is {winningTeam} the winning team? (y/n): ")
    isWinningTeam = "y"
    if isWinningTeam == "y":
        winningTeam = winningTeam.upper()
    else:
        print("Some inputs may be wrong!!")
        exit()

    winningTeam += " WON"

    uni1, uniLogo1 = getUniLogo(un1)
    uni2, uniLogo2 = getUniLogo(un2)

    templateScore.paste(uniLogo1,(107,93),uniLogo1)
    templateScore.paste(uniLogo2,(1400,93),uniLogo2)

    editable_templateScore.text((360,130),uni1,(255,255,255),uniNameFont)
    editable_templateScore.text((1140,130),uni2,(255,255,255),uniNameFont)

    editable_templateScore.text((700,130),s1,(255,255,255),scoresFont)
    editable_templateScore.text((900,130),s2,(255,255,255),scoresFont)

    editable_templateScore.text((660,277),winningTeam,(143,196,251),winningFont)
    
    templateScore.save(f'{dir_path}/results/match{i}.png')

    print(f'{i+1} of {numOfGames} result created!')

background = Image.open(f'{dir_path}/imgs/{sportName}BG.jpg').convert("RGBA")
W,H = background.size

conut = 1
if numOfGames == 1:
    for i in range(numOfGames):
        match = Image.open(f'{dir_path}/results/match{i}.png').convert("RGBA")
        w,h = match.size
        background.paste(match,(int((W-w)/2), 1450),match)
        conut+=1
        print(f'{conut} of {numOfGames} result pasted!')

elif numOfGames == 2:
    for i in range(numOfGames):
        match = Image.open(f'{dir_path}/results/match{i}.png').convert("RGBA")
        w,h = match.size
        background.paste(match,(int((W-w)/2),int((H-((h-100)*(numOfGames)))*conut/2)-50),match)
        conut+=1
        print(f'{conut} of {numOfGames} result pasted!')

elif numOfGames == 3:
    for i in range(numOfGames):
        match = Image.open(f'{dir_path}/results/match{i}.png').convert("RGBA")
        w,h = match.size
        background.paste(match,(int((W-w)/2),int((H-((h-100)*(numOfGames)))*conut/2)),match)
        conut+=1
        print(f'{conut} of {numOfGames} result pasted!')

elif numOfGames == 4:
    for i in range(numOfGames):
        match = Image.open(f'{dir_path}/results/match{i}.png').convert("RGBA")
        w,h = match.size
        background.paste(match,(int((W-w)/2),int(((H-((h-135)*(numOfGames)))*conut/2)-10)),match)
        conut+=1
        print(f'{conut} of {numOfGames} result pasted!')

background.save(f'{dir_path}/final.png')

# editable_templateScore.text((365,145),f"After completion of {numOfGames} games".upper(),(0,0,0),boldFont)







print("Exit..")
exit()