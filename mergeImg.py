import PIL.Image as Image
import os, sys

img_lis = os.listdir('imgs')

img_ex = Image.open(os.getcwd()+'\\imgs\\'+img_lis[0])
img_ex_width = img_ex.width
img_ex_height = img_ex.height


wrap_width = img_ex_width * 5
wrap_height = img_ex_height * 4


toImage = Image.new('RGBA', (wrap_width, wrap_height))
for x in range(5):
	for y in range(4):
		item = img_lis.pop(0)
		fromImage = Image.open(os.getcwd()+'\\imgs\\'+item)
		toImage.paste(fromImage, (x*img_ex_width, y*img_ex_height))

toImage.show()
toImage.save('code.font.exp1.tiff')
toImage.save('code.font.exp1.png')