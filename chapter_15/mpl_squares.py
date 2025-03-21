import matplotlib.pyplot as plt
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.style.use('seaborn-v0_8')
print(plt.style.available)
fig, ax = plt.subplots()   #This function can generate one or more plots in the same figure. 
ax.plot(input_values, squares, linewidth=3)   #method, which tries to plot the data it’s given in a meaningful way.
# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
ax.tick_params(labelsize=14)          
plt.show()               #The function plt.show() opens Matplotlib’s viewer and displays the plot