from PIL import Image, ImageDraw

w, h = 540, 960
image = Image.new('RGBA', (w, h), "#95c8d8")
draw = ImageDraw.Draw(image)

with open("DS9.txt", 'r') as f:
    for line in f:
        x = line.split(' ')
        draw.point((int(x[0]), int(x[1])), fill = "#828282")

image.save('result.png')
image.show()