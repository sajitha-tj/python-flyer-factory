import os
from PIL import Image, ImageFilter, ImageFont, ImageDraw

UniDictionary = {"SJP": "University of Sri Jayewardenepura - SJP",
                 "USJ": "University of Sri Jayewardenepura - SJP",
                 "COL": "University of Colombo - COL",
                 "UOC": "University of Colombo - COL",
                 "PER": "University of Peradeniya - PER",
                 "UOP": "University of Peradeniya - PER",
                 "KEL": "University of Kelaniya - KEL",
                 "UOK": "University of Kelaniya - KEL",
                 "JAF": "University of Jaffna - JAF",
                 "UOJ": "University of Jaffna - JAF",
                 "MOR": "University of Moratuwa - MOR",
                 "UOM": "University of Moratuwa - MOR",
                 "RUH": "University of Ruhuna - RUH",
                 "UOR": "University of Ruhuna - RUH",
                 "VAU": "University of Vavuniya - VAU",
                 "VAV": "University of Vavuniya - VAU",
                 "SAB": "Sabaragamuwa University of Sri Lanka - SAB",
                 "WAY": "Wayamba University of Sri Lanka - WAY",
                 "WYB": "Wayamba University of Sri Lanka - WAY",
                 "RAJ": "Rajarata University of Sri Lanka - RAJ",
                 "RJT": "Rajarata University of Sri Lanka - RAJ",
                 "UVA": "Uva Wellassa University - UVA",
                 "UVU": "Uva Wellassa University - UVA",
                 "EST": "Eastern University of Sri Lanka - EST",
                 "EU": "Eastern University of Sri Lanka - EST",
                 "SEU": "South Eastern University of Sri Lanka - SEU",
                 "SEA": "South Eastern University of Sri Lanka - SEU",
                 "VPA": "University of Visual & Performing Arts - VPA",
                 "GWU": "Gampaha Wickramarachchi University - GWU",
                 "GWA": "Gampaha Wickramarachchi University - GWU"
                 }


def getUniName(uniNameShort):
    if UniDictionary.get(uniNameShort) == None:
        print(f'Error in excel file. Please check the name of {uniNameShort}')
        exit()
    else:
        uniName = UniDictionary.get(uniNameShort)
        return uniName.split(' - ')[0].upper()


# name = input('Enter the name: ')
name = "Sithum nimesh".upper()
uni = "Sabaragamuwa University of Sri Lanka".upper()
number = "DYN001".upper()

errorFileList = []

dir_path = os.path.dirname(os.path.realpath(__file__))


#  fonts
nameFont = ImageFont.truetype(f'{dir_path}/fonts/Montserrat-Bold.ttf', 44)
uniFont = ImageFont.truetype(f'{dir_path}/fonts/Montserrat-Regular.ttf', 24)
numberFont = ImageFont.truetype(f'{dir_path}/fonts/Evil Empire.otf', 92)

numberOfPhotos = 0

for image in os.listdir(f'{dir_path}/photos'):
    splitedName = image.split('.jpg')[0].split('_')

    number = splitedName[0].upper()
    name = splitedName[1].upper()
    uni = splitedName[2].upper()

    numberOfPhotos += 1

    try:
        # open the image
        img = Image.open(f'{dir_path}/photos/{image}')

        # if landscape
        # if img.size[0] > img.size[1]:
        photoframe = Image.open(f'{dir_path}/imgs/pFrame.png')
        iw, ih = img.size
        fw, fh = photoframe.size

        photoframe = photoframe.resize((iw, ih))

        # if img is bigger than photoFrame, crop it into the center
        # if iw > fw:
        #     left = (iw - fw)/2
        #     top = (ih - fh)/2
        #     right = (iw + fw)/2
        #     bottom = (ih + fh)/2
        #     img = img.crop((left, top, right, bottom))

        # resize the image
        # img = img.resize((fw, fh))

        # paste the frame on photo
        img.paste(photoframe, (0, 0), photoframe)

        # resize the image into the fw width with the same aspect ratio of img
        if (iw > ih):
            img = img.resize((fw, int((fw/iw)*ih)))
        else:
            img = img.resize((int((fh/ih)*iw), fh))

        inw, inh = img.size

        # open the BG
        templateBG = Image.open(f'{dir_path}/imgs/frameBG.png')
        tw, th = templateBG.size

        # paste the image on the center of template
        templateBG.paste(img, (int((tw - inw)/2), 213))

        # paste texts on the template
        draw = ImageDraw.Draw(templateBG)
        draw.text((int((tw - fw)/2), 805), name,
                  (255, 255, 255), font=nameFont)
        uni = getUniName(uni)
        draw.text((int((tw - fw)/2), 857), uni, (255, 255, 255), font=uniFont)

        numberWidth = draw.textlength(number, font=numberFont)
        draw.text(((int((tw - fw)/2)+fw)-numberWidth, 805),
                  number, (248, 237, 1), font=numberFont)

        # save the image
        templateBG.save(f'{dir_path}/output/image-{number}.png')

        print(f'image{numberOfPhotos} done!')

    except:
        print(f'Error in photo number {number} by {name}')
        errorFileList.append(f'{number}_{name}_{uni}.jpg')
        continue

print(f'\n\n{numberOfPhotos} photos created!')

if len(errorFileList) > 0:
    print(f'\n\n{len(errorFileList)} photos are not created due to errors!')
    print('Error files are: ')
    for file in errorFileList:
        print(file)
