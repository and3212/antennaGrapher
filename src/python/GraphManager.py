import matplotlib.pyplot as plt

# Author: Liam Lawrence
# Date: July 20, 2017
# Graphs the data in polar that we pass to it

def graph(theta, r, angle, offset, type):
    ax = plt.subplot(111, polar=True)
    ax.plot(theta, r, color='r', linewidth=3, label='Radiation Path')
    ax.grid(True)
    ax.set_title(type + " Scan at " + str(angle) + "°", va='bottom')

    # if offset != 0:
        # ax.text(200, 55, r"R has an offset of " + str(offset), fontsize=12, fontweight='bold')
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.show()
