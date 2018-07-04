import matplotlib.pyplot as plt


class Graph:

    def add_info(self, data, colour='blue'):
        colour_dic = {'blue': 'b',
                      'green': 'g',
                      'red': 'r',
                      'cyan': 'c',
                      'magenta': 'm',
                      'yellow': 'y',
                      'black': 'k',
                      'white': 'w'}
        plt.plot(data, colour, linestyle='-', marker='*')

    def show_graph(self):
        plt.show()
