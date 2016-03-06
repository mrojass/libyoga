import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage as ndi
from skimage import feature
from skimage import io
import sys
import getopt

VALUE_SIGMA = 5

def main(argv):
    ifile = ''
    ofile = ''
    try:
        opts, args = getopt.getopt(argv, 'hi:o:', ['ifile=', 'ofile='])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            ifile = arg
        elif opt in ("-o", "--ofile"):
            ofile = arg

    edge(ifile, ofile)

def edge(ifile, ofile):
    img = io.imread(ifile, flatten=True)
    edges1 = feature.canny(img)
    edges2 = feature.canny(img, sigma=VALUE_SIGMA)
    out = np.uint8(edges2 * 255)

    io.imsave(ofile, out)

    # display results
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3), sharex=True, sharey=True)

    ax1.imshow(img, cmap=plt.cm.jet)
    ax1.axis('off')
    ax1.set_title('noisy image', fontsize=20)

    ax2.imshow(edges1, cmap=plt.cm.gray)
    ax2.axis('off')
    ax2.set_title('Canny filter, $\sigma=1$', fontsize=20)

    ax3.imshow(edges2, cmap=plt.cm.gray)
    ax3.axis('off')
    ax3.set_title('Canny filter, $\sigma=' + str(VALUE_SIGMA) + '$', fontsize=20)

    fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9,
                        bottom=0.02, left=0.02, right=0.98)

    plt.show()

if __name__ == "__main__":
    main(sys.argv[1:])
