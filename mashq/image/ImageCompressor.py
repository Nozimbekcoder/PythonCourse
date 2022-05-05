import PIL
from PIL import Image
from tkinter.filedialog import askopenfilename

file_path = askopenfilename()
img =PIL.Image.open(file_path)
myHeight,myWidth = img.size


img= img.resize((myHeight,myWidth),PIL.Image.ANTIALIAS)
save_path = askopenfilename()
img.save(save_path+"comperssed.jpg")