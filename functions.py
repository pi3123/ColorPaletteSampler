# import modules
import random
from colorthief import ColorThief
from utils import conversions


def getRandomPalette():
    palette = []
    highlightColor = (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255))
    for i in range(5):
        rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        palette.append({'HEX': conversions.rgb_to_hex(rgb[0], rgb[1], rgb[2]),
                        'CMYK': conversions.rgb_to_cmyk(rgb[0], rgb[1], rgb[2]),
                        'HSV': conversions.rgb_to_hsv(rgb[0], rgb[1], rgb[2]),
                        'RGB': rgb})
    return palette, highlightColor


def getColorAttributes(path, noOfColors):
    color_thief = ColorThief(path)
    colors = color_thief.get_palette(color_count=noOfColors)

    palette = []
    for i in colors:
        palette.append({'HEX': conversions.rgb_to_hex(i[0], i[1], i[2]),
                        'CMYK': conversions.rgb_to_cmyk(i[0], i[1], i[2]),
                        'HSV': conversions.rgb_to_hsv(i[0], i[1], i[2]),
                        'RGB': i})

    return palette


def getComplementaryPalette(palette):
    compPalette = []
    for i in palette:
        rgb = (255 - i['RGB'][0], 255 - i['RGB'][1], 255 - i['RGB'][2])

        compPalette.append({'HEX': conversions.rgb_to_hex(rgb[0], rgb[1], rgb[2]),
                            'CMYK': conversions.rgb_to_cmyk(rgb[0], rgb[1], rgb[2]),
                            'HSV': conversions.rgb_to_hsv(rgb[0], rgb[1], rgb[2]),
                            'RGB': rgb})

    return compPalette


def getHighlightColors(palette, highlightColor):
    highlightPalette = []
    for i in palette:
        rgb = [int(i['RGB'][0] + highlightColor[0]), int(i['RGB'][1] + highlightColor[1]),
               int(i['RGB'][2] + highlightColor[2])]

        # rgb = [int((i['RGB'][0] + highlightColor[0]) / 2), int((i['RGB'][1] + highlightColor[1]) / 2), int((i['RGB'][1] + highlightColor[1]) / 2)]

        for j in range(3):
            if rgb[j] > 255:
                rgb[j] = 255

        highlightPalette.append({'HEX': conversions.rgb_to_hex(rgb[0], rgb[1], rgb[2]),
                                 'CMYK': conversions.rgb_to_cmyk(rgb[0], rgb[1], rgb[2]),
                                 'HSV': conversions.rgb_to_hsv(rgb[0], rgb[1], rgb[2]),
                                 'RGB': rgb})

    return highlightPalette


def paletteGen(canvas, palette, point1, point2, text):
    box_x = point1[0]
    box_x1 = point2[0]

    text_x = point1[0] + 83
    text_y = point1[1] + 50

    canvas.create_text(text[0], text[1], fill="White", font=("ambit", 20), text=text[2], anchor="c")

    for i in range(0, 5):

        # checking if the color's brightness is more than 50% of 255 = 128
        #   if yes, use black font
        #   if no, use white font

        luminance = int((palette[i]['RGB'][0] * 0.3) +
                        (palette[i]['RGB'][1] * 0.59) +
                        (palette[i]['RGB'][2] * 0.11))

        fontColor = "white"
        if luminance > 128:
            # print(f"{luminance} : {str(palette[i]['RGB'])} )")
            fontColor = "black"

        canvas.create_rectangle(box_x, point1[1], box_x1, point2[1], fill=palette[i]['HEX'])

        canvas.create_text(text_x, text_y, fill=fontColor, font=("ambit", 10), text=f"RGB : {palette[i]['RGB']} \n"
                                                                                    f"CMYK : {palette[i]['CMYK']} \n"
                                                                                    f"HEX : {palette[i]['HEX']} \n"
                                                                                    f"HSV : {palette[i]['HSV']}")

        box_x += 180
        box_x1 += 180
        text_x = box_x + 83
