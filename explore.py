import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

import os
import random

nb_samples = 4
data_dir = "data"

fig = plt.figure()

ACTIONS = ["left", "right", "none"]
# initialize the toolbox containing :
# - a subplot to generate the images 
# - a place to store the images
tool = {}
for i ,action in enumerate(ACTIONS):
    tool[action] = {}
    ax = fig.add_subplot(3, 1, i+1)
    ax.set_title(action)
    ax.set_xlabel("frequency")
    ax.set_ylabel("channel")
    tool[action]["axis"] = ax
    tool[action]["im"] = []

ims = []
for action in ACTIONS:
    # pick nb_samples random files to display for each action
    action_dir = os.path.join(data_dir,action)
    items = random.choices(os.listdir(action_dir), k=nb_samples)
    print(action)
    print(items)
    datas = []
    for item in items:
        data  = np.load(os.path.join(action_dir, item))

        for frame in data:
            im = tool[action]["axis"].imshow(frame, animated = True)
            tool[action]["im"].append(im)

# create a list of list of images with this patern:
#  [[im1_action1,im1_action2 im1_action3 ], [im2_action1,im2_action2 im2_action3 ]...]
image_list = list(zip(*[tool[k]["im"] for k in ACTIONS] ))

ani = animation.ArtistAnimation(fig,image_list , interval=50, blit=True,repeat_delay=1000)

plt.show()
