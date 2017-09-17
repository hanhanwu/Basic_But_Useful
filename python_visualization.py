
# Bar Chart
import numpy as np
import matplotlib.pyplot as plt

x_values = ['A', 'B', 'C', 'D']
x_pos = np.arange(len(x_values))
y_values = [10, 20, 30, 40]
plt.bar(x_pos, y_values, align='center', alpha=0.5)
plt.xticks(x_pos, x_values)
plt.ylabel('Y')
plt.title('Edit Your Title')
plt.show()


# Change fiture size
import matplotlib.pyplot as plt
plt.figure(figsize=(3,4))
