# Defining a function to create Linear Regression plots
def plot_linear_regression(x_values, y_values, x_label, y_label, title, output_file):
    
    # Perform linear regression
    (slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
    
    # Calculate regression line values
    regress_values = x_values * slope + intercept
    
    # Create scatter plot
    plt.scatter(x_values, y_values, edgecolor="black", linewidths=1, marker="o", alpha=0.8)
    
    # Plot regression line
    plt.plot(x_values, regress_values, "r-", label=f"y={slope:.2f}x + {intercept:.2f}")
    
    # Add labels and title
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    
    # Displaying the r-squared value
    plt.text(0.5, 0.05, f"y = {slope:.2f}x + {intercept:.2f}", transform=plt.gca().transAxes, color= "red", fontsize=16, fontweight='bold')
    
    
    # Save the plot
    plt.savefig(output_file)
    
    # Show the plot
    #print(f"y= {slope:.2f}x + {intercept:.2f}")
    print(f"The r^2-value is: {rvalue**2:.6f}")
    plt.show()