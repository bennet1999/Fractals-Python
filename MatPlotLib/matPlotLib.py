import matplotlib as mpl
from matplotlib import pyplot as plt
mpl.rcParams['toolbar'] = 'None'


ages_x = [5, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(ages_x, dev_y, 'b:', label='All Devs')

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(ages_x, py_dev_y, 'r:', label='Python')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD )')
plt.title('Median Salary')
plt.legend()
# plt.axis('off')
plt.tight_layout()
plt.grid(True)

plt.show()