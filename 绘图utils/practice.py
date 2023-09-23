from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "last_expr"

import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010, 2020]      # 世界人口数据
pop = [2.519, 3.692, 5.263, 6.972, 7.729]
plt.plot(year, pop)                  # 折线图
plt.show()

