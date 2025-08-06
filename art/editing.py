from PIL import Image, ImageOps

 
# Opens a image in RGB mode
im = Image.open(r"art/minion_animations\david_minion\david_crawl\david_krype1.png")
 
# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size
 
# Setting the points for cropped image
left = 0
top = 0
right = width - 0
bottom = height - 0
 
# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))

img_with_border = ImageOps.expand(im1,border=1,fill=(255, 0, 0))
 
# Save image
img_with_border.show()
#im1.save("art\player_animations\Hans\hans_run\Hans_springe.png")

