#!/usr/bin/env python
# coding: utf-8

# ### Group Project Presentation
# 

# ### Active Group Members
# 1. Fauzeeyah Adams
# 2. Ayomide Bello
# 3. Achi Fidelia Oreoluwa
# 4. Adetola Ibrahim
# 5. Chukwuebuka Nnakwe
# 6. Joshua Ayere
# 7. Olamide Omotosho

# ### Choose any python package, import it, demonstrate how it works, and how it can solve a problem. Show the package like you built it and you want to advertise it

# ### We are choosing Matplotlib
# In this section, we will look at Matplotlib, which is a popular python library commonly used for data visualization, we will define what a Matplotlib is, show how to create Figures and some other components, how to access it, demonstrate how a Matplolib works and how it can solve a problem.
# 
# ### What is a Matplotlib?
# Matplotlib is a popular python library! it's a powerful tools that allows you to create all sorts of visualizations and plots using Python programming language. it's like a magic wand that helps you turn data into beautiful charts and graphs
# 
# Basically, Matplotlib is a popular package built on NumPy arrays. It consists of several components that work together to create visualizations. some of the key components include: Figures, Axes, Artists, Legend, e.t.c. One of the greatest benefits of visualization is that it allows us visual access to huge amounts of data in easily digestible visuals. With Matplotlib, you can bring your data to life and communicate insights effectively
# 
# ### Creating a Matplotlib
# If we want to work with any Matplotlib functions we first need to import the Matplotlib library

# In[4]:


import matplotlib.pyplot as plt


# ### This code imports the Matplotlib library and assigns it to the "plt". By using the alias, you can refer to Matplotlib functions and methods more conveniently

# In[7]:


# Importing Matplotlib module from Matplotlib, import pyplot as plt
# Temperature data
# x-axis values
time =[2,4,6,8,10,12]
# y-axis values
temperature = [25, 27, 29, 30, 32, 31]
# Create a line plot
# Function to plot
plt.plot(time, temperature)
# Title of the plot
plt.title('Temperature Changes')
# Adding the label
plt.ylabel("temperature")
plt.xlabel("time")
# Function to show the plot
plt.show()


# ### In the above example, the elements of time and temperature provides the coordinates for the x-axis and y-axis and a line is plotted against those cordinates.

# ### Matplotlib is primarily focused on visualization, so it doesn't directly handle data loading,slicing, or other manipulation operations. However, it works seamlessly with other python libraries like NumPy and Pandas
# 

# In[26]:


### Using Pandas, we need to analyze and visualize the data sets
revenue = {'months':['jan', 'feb', 'mar', 'apr', 'may',
                     'jun', 'jul','aug', 'sept', 'oct','nov', 'dec'],
          'monthly_sales': [120, 135, 150, 145, 155, 160, 
                            170, 180, 190, 200, 210, 220]}


# In[10]:


import pandas as pd
df = pd.DataFrame(revenue)


# In[12]:


df


# In[23]:


import pandas as pd
revenue = pd.DataFrame(revenue)
import matplotlib.pyplot as plt


# In[24]:


# Function to plot
revenue.plot(x ="months", y = "monthly_sales", kind = "line")
# Title of the plot
plt.title("Total_yearly_revenue")
# Adding the labels
plt.ylabel =("months")
plt.xlabel =("monthly_sales")
# Function to show the plot
plt.show()


# In[27]:


### Using Numpy, we need to visualize the given data
import numpy as np
import matplotlib.pyplot as plt


# In[56]:


# Create a NumPy array with the relevant data
data = np.array([1,2,3,4,5])

# Create a simple line plot
# Function to plot
plt.plot(data)
# Adding the title
plt.title("Line PLot of NumPy Data")
# Adding the labels
plt.ylabel = ("Y-axis")
plt.xlabel = ("X-axis")
# Function to show the plot
plt.show()


# ###  Some Components of Matplotlib
# 
# Matplotlib consists of several components that work together to create visualiations. Some of the key components include:
# 
# 1. Figures: Figures are the top-level container for all the plot elements. They can contain one or more subplots and other visual elements.
# 
# 2. Axes: These are the individual plots within the figures. They are the area where data is plotted and can have their own labels, titles, and other customizations
# 
# 3. Artists: These are the objects that represent the visual elements in a plot, such as lines, markers, text and shapes. These obects can be customized to create the desired visual representation.
# 
# 4. Legends: These are used to provide additional information about the elements in a plot. They help in identifying different data series or categories in a plot.
# 

# In[35]:


### An example of some components
### Figures and Axes
import matplotlib.pyplot as plt
### Creating a Figure and Axes
fig, ax = plt.subplots()

# Plotting data on the Axes
# Adding the labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
# Adding the title
ax.set_title("Figure with Axes")
# Displaying the Figure
plt.show()


# In[44]:


### Artists
import matplotlib.pyplot as plt

# Creating a Figure and Axes
fig, ax = plt.subplots()

# Creating and customizing different artists
line_artist, = ax.plot([1, 2, 3, 4, 5], [2, 4, 6, 8, 10],
                       color="blue", linewidth=2)
scatter_artist = ax.scatter([1, 2, 3, 4, 5], [2, 4, 6, 8, 10], 
                            color="red", marker="o")
text_artist = ax.text(3, 8, "Hello, Learning Circle 119!",
                      fontsize=12, color= "green")
 
# Adding the labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
# Modifying artist properties
line_artist.set_linestyle("--")
scatter_artist.set_edgecolors("black")
text_artist.set_fontweight("bold")

# Adding the title
ax.set_title("Artist")
# Displaying the Figure
plt.show()


# In[48]:


### Legends
import matplotlib.pyplot as plt
# Data to display on plots
x = [3,1,3]
y = [3,2,1]
# Function to plots
plt.plot(x, y)
plt.plot(y, x)

# Adding the legends
plt.legend(["blue", "ornge"])
# Displaying the plot
plt.show()


# ### Creating Different Types of Plots
# 
# ### Scatter Plot
# These are graphs used that present the relationship between two variables in a data set. The scatter() method in the Matplotlib library is used to draw a scatter plot.
# 

# In[55]:


import matplotlib.pyplot as plt
# Sample data
x = [1,2,3,4,5]
y = [2,4,6,8,10]

# Create a scatter plot
plt.scatter(x, y)

# Adding the labels
plt.xlabel = ("X-axis")
plt.ylabel = ("Y-axis")

# Adding the title
plt.title("Scatter Plot")

# Display the plot
plt.show()


# ### Line chart/ line graph
# This is used to represent a relationship between two data X and Y connected by straight lines. It's commonly used to show the trend or relationship between two variables over a continuous interval
# 
# 

# In[60]:


import matplotlib.pyplot as plt
# Sample data
x = [1,2,3,4,5]
y = [2,4,6,8,10]

# Create the function to plot
plt.plot(x, y)

# Adding the labels
plt.xlabel = ("X-axis")
plt.ylabel = ("Y-axis")

# Adding the title
plt.title("Line Graph")

# Adding the legends
plt.legend(["Line"])

# Display the plot
plt.show()


# ### Bar Chart
# A bar chart or bar graph is a graph that represents the category of data with rectangular bars to represent data. Each bar represents a category or group, and the length or height of the bar corresponds to the value or quantity of the data. Bar charts are commonly used to compare different categories or show the distribution of data across different groups.

# In[62]:


import matplotlib.pyplot as plt

# Sample data
x = ["A", "B", "C", "D", "E"]
y = [10,15, 9,12,8]

# Create the function to plot
plt.bar(x, y)

# Adding the labels
plt.xlabel = ("Categories")
plt.ylabel = ("Values")

# Adding the title
plt.title("Bar Chart")

# Adding the legends
plt.legend(["Bar"])

# Display the plot
plt.show()


# ### Histogram
# A histogram is a type of bar chart that represents the distribution of a dataset. It displays the frequencies of data within specific intervals, called bins. The x-axis represents the range of values or intervals, while the y-axis represents the frequency or count of data falling within each bin. Histograms are useful for visualizing the shape, center, and spread of a dataset, as well as identifying any outliers.

# In[70]:


import matplotlib.pyplot as plt
# data to display on plots
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# This will plot a simple histogram
plt.hist(x, bins = [1, 2, 3, 4, 5, 6, 7, 8, 9])

# Adding the labels
plt.xlabel = ("Values")
plt.ylabel = ("Frequency")

# Adding title to the plot
plt.title("Histogram")

# Adding the legends
plt.legend(["Bar"])

# Displaying the plot
plt.show()


# ### Pie Chart
# A pie chart is a circular chart that is divided into slices to represent different categories or proportions of a whole. Each slice of the pie chart represents a specific category, and the size of each slice corresponds to the proportion or percentage it represents. The total of all the slices ia always 100% or the whole. Pie charts are commonly used to visualize data that can be divided into discrete categories and to show the relative sizes or percentages of each category 

# In[74]:


import matplotlib.pyplot as plt
### Sample Data
categories = ["Category A", "Category B", 
              "Category C", "Category D", "Category E"]
values = [30, 15, 20, 21, 14]

# Explode the second slice(Category B)
explode = [0, 0.1, 0, 0, 0] 

# Plotting the pie chart
plt.pie(values, labels = categories,
       explode = explode, autopct="%1.1f%%" )

# Adding a title
plt.title("Pie Chart")

# Displaying the pie chart
plt.show()


# ###  Box plot
# This is a graphical representation of the distribution of a dataset. The plot displays the minimum, first quartile, median, third quartile, and maximum values of the dataset in a box-like shape. This plot provides a vital summary of the dataset's distribution , including information about outliers and the spread of the data

# In[75]:


import matplotlib.pyplot as plt
# Sample data
data = [60, 65, 70, 75, 80, 85, 90, 95, 100]

# Creating the box plot
plt.boxplot(data)

# Adding the labels
plt.xlabel = ("Dataset")
plt.ylabel = ("Values")

# Adding the title
plt.title("Box plot")

# Displaying the plot
plt.show()


# In[77]:


### Using numpy array on a box plot  displays the minimum,
first quartile, median,third quartile, and maximum values of the dataset
import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = [60, 65, 70, 75, 80, 85, 90, 95, 100]

# Calculating the statistics
minimum = np.min(data)
first_quartile = np.percentile(data, 25)
median = np.median(data)
third_quartile = np.percentile(data, 75)
maximum = np.max(data)

# Creating the box plot
plt.boxplot(data)

# Adding labels
plt.xlabel = ("Dataset")
plt.ylabel = ("Values")
# Adding the title
plt.title("Box Plot")

# Adding statistics to the plot
plt.text(1.1, minimum, f"Min: {minimum}")
plt.text(1.1, first_quartile, f"Q1: {first_quartile}")
plt.text(1.1, median, f"Median: {median}")
plt.text(1.1, third_quartile, f"Q3: {third_quartile}")
plt.text(1.1, maximum, f"Max: {maximum}")

# Displaying the plot
plt.show()



# ### Area Plot
# An area plot, also known as a stacked area plot, is a type of data visualization that displays the cummulative contribution of different categories over time or any other continuous variable. It is similar to a line plot, but the area between the line and the x-axis is filled with color to represent the contribution of each category.
# Area plots are useful for visualizing the changing proportions or contributions of different categories over time or any other continuous variable. They can help identify trends, patterns, and relative magnitudes of different categories.
# 

# In[78]:


import matplotlib.pyplot as plt

# Example data
years = [2015, 2016, 2017, 2018, 2019, 2020]
category1 = [20, 30, 40, 50, 60, 70]
category2 = [10, 25, 35, 45, 55, 65]
category3 = [5, 15, 25, 35, 45, 55]

# Creating the area plot
plt.stackplot(years, category1, category2, 
              category3, labels=['Category 1', 'Category 2', 'Category 3'])

# Adding labels and title
plt.xlabel = ('Year')
plt.ylabel = ('Value')
plt.title('Area Plot')

# Adding legend
plt.legend(loc='upper left')

# Displaying the plot
plt.show()




# ### Creatingthe imshow() function
# The imshow() function in Matplotlib is used to display an image or a matrix as a 2D plot. It stands for "image show." You can use this function to visualize images, heatmaps, or any other 2D data.
# 
# 

# In[81]:


### Using the numpy array
import matplotlib.pyplot as plt
import numpy as np

# Create a random 2D array
data = np.random.rand(10, 10)

# Display the data using imshow()
plt.imshow(data)
plt.colorbar()  # Add a colorbar for reference
plt.show()


# ### When to use a Matplotlib
# You can use Matplotlib whenever you want to create visualizations or plots in Python. It's a great tool for displaying data in a visual and intuitive way. Here are some common scenarios where Matplotlib can be useful:
# 
# 1. Data exploration: When you have a dataset and want to gain insights or understand the patterns and relationships within the data, Matplotlib can help you create various types of plots like line plots, scatter plots, histograms, etc.
# 
# 2. Data presentation: If you need to present your data to others, Matplotlib can help you create visually appealing and informative plots that make it easier for your audience to understand the data.
# 
# 3. Report generation: When generating reports or documenting your analysis, including visualizations created with Matplotlib can enhance the readability and impact of your work.
# 
# 4. Comparing data: If you have multiple datasets and want to compare them visually, Matplotlib can help you create side-by-side plots or overlay plots to easily identify similarities or differences.
# 
# 5. Trend analysis: If you want to analyze trends or patterns over time or across different variables, Matplotlib can help you create line plots or other types of time-series visualizations.
# 
# 6. Model evaluation: If you're working with machine learning models and need to evaluate their performance, Matplotlib can help you create plots like ROC curves, confusion matrices, or precision-recall curves.
