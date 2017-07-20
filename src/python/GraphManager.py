import matplotlib.pyplot as plt

def graph(theta, r, angle, offset, type):
    ax = plt.subplot(111, polar=True)
    ax.plot(theta, r, color='r', linewidth=3, label='another line')
    ax.grid(True)

    ax.set_title(type + " Scan at " + str(angle) + "°", va='bottom')
    #ax.set_title("R has an offset of " + str(offset), va='top')
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.show()