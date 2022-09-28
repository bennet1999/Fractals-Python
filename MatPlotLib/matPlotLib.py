import matplotlib as mpl
from matplotlib import pyplot as plt
import matplotlib.lines as lines
import matplotlib.animation as animation

mpl.rcParams['toolbar'] = 'None'

# plt.xkcd()

# ages_x = [5, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# dev_y = [38496, 42000, 46752, 49320, 53200,
#          56000, 62316, 64928, 67317, 68748, 73752]

# plt.plot(ages_x, dev_y, 'b:', label='All Devs')

# py_dev_y = [45372, 48876, 53850, 57287, 63016,
#             65998, 70003, 70000, 71496, 75370, 83640]

# plt.plot(ages_x, py_dev_y, 'r:', label='Python')

# plt.xlabel('Ages')
# plt.ylabel('Median Salary (USD )')
# plt.title('Median Salary')
# plt.legend()


fig = plt.figure()
x_plot = [0, 1]
y_plot = [0, 0]

for i in range(50):
    fig.add_artist(lines.Line2D(x_plot, y_plot, color='#be2525'))
    y_plot[0] = i+2
    # x_plot[1] = i+1
x_plot = [0, 1]
y_plot = [0, 0]
for i in range(50):
    fig.add_artist(lines.Line2D(x_plot, y_plot, color='#040fe7'))
    y_plot[1] = i+2


# fig.add_artist(lines.Line2D([0, 1, 0.5], [1, 0, 0.2]))


# plt.title('matplotlib.pyplot.figure() Example\n',
#           fontsize=14, fontweight='bold')

plt.axis('off')
plt.tight_layout()
plt.grid(False)

plt.show()
