from matplotlib import pyplot as plt

x_days = [1,2,3,4,5,6,7,8,9,10]
y_views = [1211, 1201, 1213, 1238, 1272,
           1196, 1256, 1023, 1053, 1443]
plt.plot(x_days, y_views, color='r', linestyle='--', marker='.')

y_best = [366,378,352,327,237,
          276,343,382,315,227]
plt.plot(x_days, y_best, color='g', linestyle='-.', marker='v')
plt.title('Channel Views')
plt.xlabel('September 2022')
plt.ylabel('Views')

plt.grid(True)
plt.xticks(x_days)
plt.ylim(0, 1500)

print(plt.style.available)
plt.show()
