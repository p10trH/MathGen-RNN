from __future__ import print_function
import numpy as np
import tensorflow as tf

import argparse
import time
import os
from six.moves import cPickle

from utils import TextLoader
from model import Model

from tkinter import *

# directory where to load trained models from
# save_Math_Final  save_Math
save_dir_arg = "save_Math_Final"

# load saved arguments, word/vocab lists, and model to use
with open(os.path.join(save_dir_arg, 'config.pkl'), 'rb') as f:
	saved_args = cPickle.load(f)
with open(os.path.join(save_dir_arg, 'words_vocab.pkl'), 'rb') as f:
	words, vocab = cPickle.load(f)
model = Model(saved_args, True)

# generate "solutions" to given number
def sample2():
	# default parameters
	#save_dir_arg = "save_WP2"  # default: "save"
	n_arg = 3  # default: 200
	prime_arg = " "  # default: " "
	pick_arg = 1  # default: 1
	sample_arg = 1  # default: 1

	# retrieve user input, number to generate solution for
	content = entry_1.get() + " ="

	# was going to use this to break down solutions, 
	# but generated solutions are wrong most of the time
	#sliderVal = slider_1.get()

	# print to terminal for debugging
	print("["+content+"]")

	# start session
	with tf.Session() as sess:
		# initialize variables
		tf.global_variables_initializer().run()
		# create a saver
		saver = tf.train.Saver(tf.global_variables())
		# get checkpoint
		ckpt = tf.train.get_checkpoint_state(save_dir_arg)
		if ckpt and ckpt.model_checkpoint_path:
			# restore checkpoint
			saver.restore(sess, ckpt.model_checkpoint_path)

			# sample number, receive generated "solution"
			generatedSolution = model.sample(sess, words, vocab, n_arg, content, sample_arg, pick_arg)

			# print to terminal for debugging
			print(generatedSolution)

			# append problem to the text module in GUI
			text_1.insert(END, generatedSolution+"\n")

# set root for GUI using TKinter
root = Tk()

# name of GUI
root.title("Math Generator")

# size of GUI
root.geometry("360x650")

# entry module to type number that you want to generate a solution for
entry_1 = Entry(root)
entry_1.place(x = 20, y = 40)

# button to "solve" addition problem based on user input
button_1 = Button(root, text = "Solve", command = sample2, width = 10)
button_1.place(x = 215, y = 40)

# text field module to display generated solutions
text_1 = Text(root, width = 44, height = 35, wrap=WORD, bg="gray")
text_1.place(x = 20, y = 80)

# slider
#slider_1 = Scale(root, from_=1, to=32, orient=HORIZONTAL, length=123)
#slider_1.place(x = 600, y = 40)

# start main loop for GUI
root.mainloop()