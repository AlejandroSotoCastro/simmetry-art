from PIL import Image, ImageDraw

im = Image.new('RGB', (100, 100), ("#0d1117"))
draw = ImageDraw.Draw(im)

initialX = 5 
initialY = 5
size = 10

# draw.rectangle((initialX, initialY, 15, 15), fill=("#9be9a8"),)
# draw.rectangle((15,20,25,30), fill=("#40c463"),)
# draw.rectangle((20,10,30,20), fill=("#30a14e"),)
# draw.rectangle((20,30,30,40), fill=("#216e39"),)



colors = ["#9be9a8", "#40c463", "#30a14e","#216e39"]
for x in colors:
  draw.rectangle((initialX, initialY, size, size), fill=(x),)
  initialX += 15 
  initialY += 15
  size += 15


im.save('result.png', quality=95)
im.show()