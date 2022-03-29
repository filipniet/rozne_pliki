import matplotlib.pyplot as plt
import numpy as np
names = 'Niemcy', 'Francja', 'Włochy', 'hiszpania', 'Polska', 'Rumunia', 'Holandia', 'Belgia', 'Grecja', 'Czechy', 'Portugalia', 'Szwecja', 'Węgry','Austria','bułgaria','Dania','Finlandia','Słowacja','Irlandia','Chorwacja','Litwa','Słowenia','Łotwa','Estonia','Cypr','Luksemburg','Malta'
values = [3134, 2228, 1672, 1113, 424, 169, 697, 421, 175, 174, 184,462,112,349,47,276,214,80,265,45,38,39,25,20,17,54,9]

plt.figure(figsize =(25, 20))
plt.title('Gospodarka państw Unii Europejskiej(w mld euro)', fontsize=20)
plt.bar(names, values)
