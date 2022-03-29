names = 'CDU/SDU', 'SPD', 'Greens', 'FDP', 'AfD', 'Left Party', '...'
sizes = [3134070, 2228857, 1672438, 1113851, 424269, 169578, 697219]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=names, autopct='%1.2f%%')
plt.legend(title = "LEGENDA:")

plt.show()
