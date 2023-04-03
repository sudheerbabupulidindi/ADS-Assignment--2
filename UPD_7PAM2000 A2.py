#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt  # Import the 'matplotlib' library for creating visualizations


def file_function(filename):
    """
    This function reads data from a CSV file, creates a copy of the data, drops unnecessary columns and sets 
    the index to "Country Name" and transposes the dataframe.

    Parameters:
        filename (str): Name of the file to read

    Returns:
        data (DataFrame): Original data read from the file
        data_f1 (DataFrame): Transposed data with unnecessary columns dropped
    """
    # Read data from CSV file, skipping first three rows
    data = pd.read_csv(filename, skiprows=3)

    # Create a copy of the data and drop unnecessary columns
    data_f = data
    data_f1 = data_f.drop(columns=["Country Code", "Indicator Name", "Indicator Code"], axis=1)

    # Set the index to "Country Name" and transpose the dataframe
    data_f1 = data_f1.set_index('Country Name')
    data_f1 = data_f1.transpose()

    return data, data_f1


# function with the filename "API_19_DS2_en_csv_v2_4902199.csv".
filename = "API_19_DS2_en_csv_v2_4902199.csv"

# stores the resulting dataframes in df_years and df_countries
df_years, df_countries = file_function(filename)

# prints the first few rows of the df_years dataframe.
df_years.head()

# In[2]:

# prints the first few rows of the df_countries dataframe.
df_countries.head()

# In[3]:

# prints the information of the df_years dataframe.
df_years.info()

# In[4]:

# grouping the null values in the data set
df_years.isnull().sum()

# In[ ]:


# In[5]:

# fill up the null values with zero and print data.
data = df_years.fillna(0)
data

# In[6]:


# Assign the same DataFrame to a new variable
data1 = data

# Remove the "Country Code" and "Indicator Code" columns from the DataFrame
data1 = data.drop(["Country Code", "Indicator Code"], axis=1)

# Set the "Indicator Name" column as the index of the DataFrame
data1.set_index("Indicator Name", inplace=True)

# Select rows where the "Indicator Name" is "Population growth (annual %)"
data1 = data1.loc["Population growth (annual %)"]

# Reset the index of the DataFrame, moving the "Indicator Name" column back to a regular column
data1 = data1.reset_index(level="Indicator Name")

# Group the data by "Country Name" and calculate the mean for each group
data1.groupby(["Country Name"]).mean()

# Print the resulting DataFrame
data1


# In[7]:

data1 = data1.head(10)  # Filter the 'data1' DataFrame to include only the first 10 rows

# Create a line plot using the 'plot()' function of the 'data1' DataFrame object.
# The 'x' parameter specifies the column name for the x-axis data, and the 'y' parameter
# specifies a list of column names for the y-axis data. The 'figsize' parameter specifies
# the size of the figure in inches.
data1.plot(x="Country Name", y=['1965', '1970', '1975', '1980', '1985', '1990', '1995', '2000', '2005', ],
           figsize=(15, 5))

plt.title("Population growth (annual %)")  # Add a title to the plot using the 'title()' function of the 'plt' object
plt.show()  # Display the plot using the 'show()' function of the 'plt' object



# In[8]:

# Assign the 'data' DataFrame to a new variable 'data2'
data2 = data

# Remove the "Country Code" and "Indicator Code" columns from 'data2'
data2 = data.drop(["Country Code", "Indicator Code"], axis=1)

# Set the "Indicator Name" column as the index for 'data2'
data2.set_index("Indicator Name", inplace=True)

# Filter 'data2' to include only rows with "Agricultural land (% of land area)" in the index
data2 = data2.loc["Agricultural land (% of land area)"]

# Reset the index to include "Indicator Name" as a regular column
data2 = data2.reset_index(level="Indicator Name")

# Group 'data2' by "Country Name" and compute the sum of each group
data2.groupby(["Country Name"]).sum()

# Print the resulting DataFrame
data2



# In[9]:

# Filter the 'data2' DataFrame to include only the first 15 rows
data2 = data2.head(15)

# Create a kernel density estimate plot using the 'plot.kde()' function of the 'data2' DataFrame object.
# The 'y' parameter specifies a list of column names for the data to plot along the y-axis.
# The 'figsize' parameter specifies the size of the figure in inches.
data2.plot.kde(y=['1965', '1970', '1975', '1980', '1985', '1990', '1995', '2000', '2005'], figsize=(15, 5))

# Add a title to the plot using the 'title()' function of the 'plt' object
plt.title("Agricultural land (% of land area)")

# Display the plot using the 'show()' function of the 'plt' object
plt.show()


# In[10]:

# Assign the 'data' DataFrame to a new variable 'data3'
data3 = data

# Remove the "Country Code" and "Indicator Code" columns from 'data3'
data3 = data.drop(["Country Code", "Indicator Code"], axis=1)

# Set the "Indicator Name" column as the index for 'data3'
data3.set_index("Indicator Name", inplace=True)

# Filter 'data3' to include only rows with "Urban population growth (annual %)" in the index
data3 = data3.loc["Urban population growth (annual %)"]

# Reset the index to include "Indicator Name" as a regular column
data3 = data3.reset_index(level="Indicator Name")

# Group 'data3' by "Country Name" and compute the sum of each group
data3.groupby(["Country Name"]).sum()

# Print the resulting DataFrame
data3


# In[11]:


data3 = data3.head(15)  # Filter the 'data3' DataFrame to include only the first 15 rows

# Create a box plot using the 'plot.box()' function of the 'data3' DataFrame object.
# The 'y' parameter specifies a list of column names for the data to plot along the y-axis.
# The 'figsize' parameter specifies the size of the figure in inches.
data3.plot.box(y=['1965', '1970', '1975', '1980', '1985', '1990', '1995', '2000', '2005'], figsize=(15, 5))

plt.title("Urban population growth (annual %)")  # Add a title to the plot using the 'title()' function of the 'plt' object
plt.show()  # Display the plot using the 'show()' function of the 'plt' object



# In[12]:


def pieGraph():
    '''
    Create a pie chart using the 'plot()' function of the 'data2' DataFrame object.
    The 'x' parameter specifies the column to use for the labels, while the
    'y' parameter specifies the column to use for the values.
    The 'kind' parameter specifies the type of chart to create (in this case, a pie chart).
    The 'figsize' parameter specifies the size of the figure in inches.
    '''
    data2.plot(x="Country Name", y="2020", kind='pie', figsize=(15, 5))

    # Add a super title to the plot using the 'suptitle()' function of the 'plt' object.
    plt.suptitle("Primary completion rate, female (% of relevant age group)")

    # Add a label to the x-axis using the 'xlabel()' function of the 'plt' object.
    plt.xlabel("Country")

    # Add a label to the y-axis using the 'ylabel()' function of the 'plt' object.
    plt.ylabel("Year")

    # Rotate the x-axis labels using the 'xticks()' function of the 'plt' object.
    plt.xticks(rotation=90)

    # Rotate the y-axis labels using the 'yticks()' function of the 'plt' object.
    plt.yticks(rotation=90)

    # Add a legend to the plot using the 'legend()' function of the 'plt' object.
    # The legend label is specified as a list containing the string "1960", and the 'loc' parameter specifies the position of the legend.
    plt.legend(["1960"], loc=1)

    # Display the plot using the 'show()' function of the 'plt' object.
    plt.show()



# In[13]:

# print the pie-Graph
pieGraph()

# In[14]:

# drop the unwanted data
data_1 = data.drop(
    columns=["1960", "1961", "1962", "1963", "1964", "1966", "1967", "1968", '1969', '1971', "1972", "1973", "1974",
             "1976", "1977", "1978", "1979", "1981", "1982", "1983", "1984", "1986", "1987", "1988", "1989", "1991",
             "1992", "1993", '1994', "1996", "1997", "1998", "1999", "2001", "2002", "2003", "2004", "2007", "2008",
             "2009", "2011", "2012", "2013", "2014", "2016", "2017", "2018", "2019", 'Unnamed: 66'])
data_1

# In[15]:

# defines a new variable df1 which is a copy of the data_1 dataframe
df1 = data_1

# columns "Country Code" and "Indicator Code" dropped.
df1 = df1.drop(["Country Code", "Indicator Code"], axis=1)

# The index of the new dataframe is then set to the column "Indicator Name"
df1.set_index("Indicator Name", inplace=True)

# only the rows with the indicator name "Forest area (% of land area)" are selected.
df1 = df1.loc["Forest area (% of land area)"]

# The index is then reset to make "Country Name" a regular column
df1 = df1.reset_index(level="Indicator Name")

# Finally, only the first 15 rows of the resulting dataframe
df1 = df1.head(15)

# printed.
df1

# In[16]:

# The index of the new dataframe is then set to the column "Country Name"
df1.set_index("Country Name", inplace=True)

# columns "2021" dropped.
df1 = df1.drop("2021", axis=1)

#print "df1"
df1

# In[17]:

# a new variable df2 as a copy of df1 with the first column dropped
df2 = df1.drop(df1.columns[0], axis=1)

# the title of the plot to "Forest area (% of land area)"
plt.title("Forest area (% of land area)")

# adjusts the figure size
sns.set(rc={'figure.figsize': (12, 10)})

# it creates a heatmap plot using bye.heatmap()
p1 = sns.heatmap(df2, annot=True, fmt=".1f", linewidth=1)

# In[38]:

import numpy as nmp

# Define a function to transpose a dataframe
def dataframe_Transpose(x):
    """
    Transposes a dataframe and drops unnecessary columns and rows

    Parameters
    ----------
    x : dataframe
        Dataframe to be transposed

    Returns
    ----------
    z : dataframe
        Transposed dataframe
    """
    # Set the index to "Indicator Name"
    x.set_index("Indicator Name", inplace=True)
    # Select only the data for "Arable land (% of land area)"
    x = x.loc["Arable land (% of land area)"]
    # Drop unnecessary columns
    x = x.drop(["Country Code", "Indicator Code"], axis=1)
    # Select the first 15 rows
    x = x.head(15)
    # Reset the index
    x = x.reset_index(drop=True)
    # Transpose the dataframe
    y = nmp.transpose(x)
    # Set the column names to the values in the first row
    y.columns = y.iloc[0]
    # Drop the first row
    y = y.drop(y.index[0])
    # Drop the row with the 2010 data (since it is incomplete)
    z = y.drop(y.index[5])
    # Return the transposed dataframe
    return z

# Call the function to get the transposed dataframe
df2 = dataframe_Transpose(data_1)

# In[47]:


# In[48]:


# Plot the transposed dataframe
df2.plot(figsize=(9, 9))
# Place the legend outside the plot
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
# Add a title to the plot
plt.title("Arable land (% of land area)")

# In[50]:

# defines a new variable df3 which is a copy of the data_1 dataframe
df3 = data_1.copy()
# using loc fucntion to select the data in the indexing
df3 = df3.loc["Marine protected areas (% of territorial waters)"]
# drop some column with were not required in ploting the dataset
df3 = df3.drop(["Country Code", "Indicator Code"], axis=1)
# select the dataframe to plot the selected data
df3 = df3.head(15)
df3 = df3.reset_index(drop=True)
# transpose the dataframe
y = nmp.transpose(df3)
# set the first row as the column names
y.columns = y.iloc[0]
# drop the first row since it's now the column names
y = y.drop(y.index[0])
# drop the row corresponding to the year 2005 since it has many missing values
df3 = y.drop(y.index[5])
df3


# In[56]:

# Plot the transposed dataframe
df3.plot(figsize=(5, 5))
# Place the legend outside the plot
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
# Add a title to the plot
plt.title("Marine protected areas (% of territorial waters)")

# In[58]:

# defines a new variable df4 which is a copy of the data_1 dataframe
df4 = data_1.copy()
# drop some column with were not required in ploting the dataset
df4 = df4.drop(["Country Code", "Indicator Code"], axis=1)
# using loc fucntion to select the data in the indexing
df4 = df4.loc["Renewable energy consumption (% of total final energy consumption)"]
# reset the index
df4 = df4.reset_index(level="Indicator Name")
df4.groupby(["Country Name"]).sum()
# drop some column with were not required in ploting the dataset
df4 = df4.drop("2020", axis=1)
df4 = df4.drop("2021", axis=1)
# Select the first 15 rows
df4 = df4.head(15)
# drop some column with were not required in ploting the dataset
df4 = df4.drop("Indicator Name", axis=1)
# set the index to "Country Name"
df4 = df4.set_index("Country Name")
df4

# In[45]:


# In[ ]:
