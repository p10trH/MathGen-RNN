# MathGen-RNN
This is a quick and dirty prototype to answer some of the curiosities we had when experimenting with word-rnn. 

We tried to "teach" a RNN basic addition, mostly to observe interesting patterns when sampling.

Mostly reused code from https://github.com/hunkim/word-rnn-tensorflow by Sung Kim

...which is mostly reused code from https://github.com/sherjilozair/char-rnn-tensorflow which was inspired from Andrej Karpathy's char-rnn.

# Requirements
- [Tensorflow](http://www.tensorflow.org)

# Basic Usage
To start the GUI and sample from a trained model.
```bash
python3 ui_genMath.py
```
The idea is to input a number (in this case up to 998), and a solution will be generated for that number. See the "Demo" section for a video showing the GUI.

# Demo
https://youtu.be/23N4JtNT64k

# Results
Most numbers generate incorrect solutions. This is mostly due to our quick training of the data and not validating solutions during the training step. This was a quick experiment, so we will have to work on it more to achieve better results.

However, it is still interesting to observe the output and discover any patterns that might exist. For starters, the RNN was able to learn the structure of an addition problem and knew where to include "+" and "=" symbols along with the numbers. This was consistent, but sometimes the structure was completely wrong. An example of this is shown at the end of the demo video.

More specifically, the number "500" is very interesting. When you input this number, all generated solutions are correct, as seen in the image below!
