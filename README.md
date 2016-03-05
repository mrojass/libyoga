libyoga
----
A Python library for calculating yoga pose accuracy.

### How It Works
Images are converted into greyscale and run with a Canny edge detection
algorithm. We tested with several values of sigma and found **4.5** to lend a highly noise-reduced edge without a great loss of information--i.e., few boundary edge gaps or "loss of pixels" on the outline of the yoga poses.
