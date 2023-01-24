from PIL import Image, ImageDraw, ImageOps

sqSize = 20
ratio = 0.5
numSqX = 20
numSqY = 20
baseColor = "#0d1117"

margin = sqSize * ratio
width = int(sqSize * numSqX + margin * (numSqX+1))
height = int(sqSize * numSqY + margin * (numSqY+1))
size = (width,height)

print(size,margin)

def fillGrid(color,size, margin):
  count = 0
  x1 = margin
  x2 = margin + size
  for x in range(numSqX):
    y1 = margin
    y2 = margin + size
    for y in range(numSqY):
      draw.rectangle((x1, y1, x2, y2), fill=(color),)
      y1+= margin + size
      y2+= margin + size
    x1+= margin + size
    x2+= margin + size


im = Image.new('RGB', (width, height), baseColor)
draw = ImageDraw.Draw(im)

fillGrid("#9be9a8",sqSize,margin)


# cool greens"#9be9a8"
# cool greens"#40c463"
# cool greens"#30a14e"
# cool greens"#216e39"



# colors = ["#9be9a8", "#40c463", "#30a14e","#216e39"]

aux = ImageOps.mirror(im)
new_image = Image.new('RGB',(2*width, height), (250,250,250))
new_image.paste(im, (0, 0) )
new_image.paste(aux, (width, 0) )

new_image.save('result.png', quality=95)
new_image.show()