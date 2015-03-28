import numpy as np
from matplotlib import pyplot as plt


class TreSlice:
    def __init__(self, X, Y, Z, C):
        self.data = C
        self.axes = np.array([X, Y, Z])
        self.labels = np.array(['X', 'Y', 'Z'])
        self.views = np.array([[0, 1, 2], [1, 0, 2], [2, 0, 1]])
        self.curAxis = 2
        self.curSlice = 0
        self.fig = plt.figure()
        self.dataMin = np.amin(self.data)
        self.dataMax = np.amax(self.data)

    def keypress(self, event):
        if event.key == ' ':
            self.curAxis += 1
            self.curSlice = 0
            if self.curAxis > 2:
                self.curAxis = 0
            self.refresh()
        elif event.key == 'up':
            self.move(1)
        elif event.key == 'down':
            self.move(-1)
        elif event.key == 'right':
            self.move(5)
        elif event.key == 'left':
            self.move(-5)

    def move(self, i):
        self.curSlice = max(min(self.curSlice + i,
                                len(self.axes[self.curAxis]) - 2), 0)
        self.refresh()

    def show(self):
        self.fig.canvas.mpl_connect('key_press_event', self.keypress)
        self.makePlot()
        plt.show()

    def refresh(self):
        self.fig.clear()
        self.makePlot()
        self.fig.canvas.draw()

    def makePlot(self):
        ax = self.fig.gca()
        axes = np.take(self.axes, self.views[self.curAxis], axis=0)
        labels = np.take(self.labels, self.views[self.curAxis])
        heatmap = ax.pcolormesh(
            axes[1], axes[2],
            np.rollaxis(self.data, self.curAxis)[self.curSlice, :, :].T,
            vmin=self.dataMin, vmax=self.dataMax)
        ax.set_aspect('equal')
        ax.set_xlabel(labels[1])
        ax.set_ylabel(labels[2])
        ax.set_title('{0} = {1}'.format(labels[0], axes[0][self.curSlice]))
        self.fig.colorbar(heatmap)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: python treslice.py filename')
        sys.exit(0)
    data = np.load(sys.argv[1])
    plot = TreSlice(data['X'], data['Y'], data['Z'], data['C'])
    plot.show()
