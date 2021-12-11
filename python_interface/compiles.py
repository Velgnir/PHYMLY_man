import os
from PIL import Image
import glob
import os

def compiles():
	os.system("bin/thermal_conductivity")
	# Create the frames
	onlyfiles = next(os.walk("images"))[2] #dir is your directory path as string
	len_of = len(onlyfiles)
	frames = []
	for i in range(len_of):
		path ="images/im"+str(i)+".png"
		frames.append(Image.open(path))

	# Save into a GIF file that loops forever
	frames[0].save('result.gif', format='GIF',
		append_images=frames[1:],
		save_all=True,
		duration=30, loop=0)