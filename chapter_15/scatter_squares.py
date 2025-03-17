import matplotlib.pyplot as plt
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
ax.tick_params(labelsize=14)
# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')
plt.savefig('squares_plot.png', bbox_inches='tight')


import matplotlib.pyplot as plt

# Generate data for the first five cubic numbers
x_values_first_five = range(1, 6)
y_values_first_five = [x**3 for x in x_values_first_five]

# Generate data for the first 5000 cubic numbers
x_values_first_five_thousand = range(1, 5001)
y_values_first_five_thousand = [x**3 for x in x_values_first_five_thousand]

# Plotting the first five cubic numbers
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.scatter(x_values_first_five, y_values_first_five, c=y_values_first_five, cmap='viridis', s=100)
ax.set_title("First Five Cubic Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cubic Value", fontsize=14)
ax.tick_params(labelsize=14)
ax.axis([0, 6, 0, 150])  # Adjust axis range to fit the data
plt.savefig('first_five.png', bbox_inches='tight')

# Plotting the first 5000 cubic numbers
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.scatter(x_values_first_five_thousand, y_values_first_five_thousand, c=y_values_first_five_thousand, cmap='viridis', s=1)
ax.set_title("First Cubic Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cubic Value", fontsize=14)
ax.tick_params(labelsize=14)
ax.axis([0, 5100, 0, 130_000_000_000])  # Adjust axis range to fit the data
plt.savefig('first_five_thousand', bbox_inches='tight')


