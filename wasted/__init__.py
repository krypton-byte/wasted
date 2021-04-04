from PIL import Image, ImageDraw, ImageFont
import os
path=os.path.dirname(os.path.abspath(__file__))
if not "pricedown bl.ttf" in os.listdir(path):
    print("downloading font pricedown bl.ttf")
    import requests
    open(f"{path}/pricedown bl.ttf", "wb").write(requests.get("https://github.com/krypton-byte/wasted/raw/master/wasted/pricedown%20bl.ttf").content)
def resizeTo(x, y, width_=1000):
    if x == y:
        width, height = width_, width_
    elif x > y:
        width=width_
        height = y/(x/width_)
    elif x < y:
        height = width_
        width = x/(y/width_)
    return (int(width), int(height))

def wasted(im):
    if max(im.size) < 1000:
        im=im.resize(resizeTo(*im.size))
    im=im.convert("L").convert("RGB")
    font=ImageFont.truetype(f"{path}/pricedown bl.ttf", int(im.height/7))
    new=Image.new("RGBA", (im.width, int((im.height/8)*1.5)), color=(0,0,0,100))
    ImageDraw.Draw(new).text((int(im.width/2-font.getsize("wasted")[0]/2),0), "wasted", font=font, fill=(255, 0, 68), stroke_width=int(font.size/10), stroke_fill=(0,0,0))
    im.paste(new, (0, int(im.height/2-new.height/2)), new.convert("RGBA"))
    return im