import matplotlib.pyplot as plt

# Author: Liam Lawrence
# Date: July 20, 2017
# Graphs the data in polar that we pass to it

def compare(theta1, theta2, r1, r2, angle, offset, type, name1, name2):
    ax = plt.subplot(111, polar=True)
    ax.plot(theta1, r1, color='r', linewidth=3, label=name1)
    ax.plot(theta2, r2, color='b', linewidth=3, label=name2)
    ax.grid(True)
    ax.set_title(type + " Scan at " + str(angle) + "°", va='bottom')

    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.show()

def graph(theta, r, angle, offset, type, name):
    ax = plt.subplot(111, polar=True)
    ax.plot(theta, r, color='r', linewidth=3, label=name)
    ax.grid(True)
    ax.set_title(type + " Scan at " + str(angle) + "°", va='bottom')

    # if offset != 0:
        # ax.text(200, 55, r"R has an offset of " + str(offset), fontsize=12, fontweight='bold')
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.show()
