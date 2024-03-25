from PIL import Image, ImageDraw


BLUE = (0, 101, 189)
WHITE = (255, 255, 255)

def Scotland(fname, width=300, height=200):
    flag = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(flag)
    draw.rectangle([(0,0),flag.size], fill =BLUE )
    draw.line((0, 0) + flag.size, fill= WHITE, width= 35)
    draw.line((0, flag.size[1], flag.size[0], 0), fill=WHITE, width = 35)
    flag.save(fname)
Scotland("Scotland.png")
