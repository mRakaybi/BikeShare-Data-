# BikeShare-Data-
In this project, i will use data provided by Motivate, a bike share system provider for many major cities in the United States,
to uncover bike share usage patterns. I will compare the system usage between three large cities:
 Chicago, New York City, and Washington, DC.
The Datasets:
Randomly selected data for the first six months of 2017 are provided for all three cities. 
All three of the data files contain the same core six (6) columns:
Start Time (e.g., 2017-01-01 00:07:57)
End Time (e.g., 2017-01-01 00:20:53)
Trip Duration (in seconds - e.g., 776)
Start Station (e.g., Broadway & Barry Ave)
End Station (e.g., Sedgwick St & North Ave)
User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
Gender
Birth Year

Statistics Computed:
We will learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. 
In this project, i'll write code to provide the following information:

#1 Popular times of travel (i.e., occurs most often in the start time):
most common month
most common day of week
most common hour of day

#2 Popular stations and trip:
most common start station
most common end station
most common trip from start to end (i.e., most frequent combination of start station and end station)

#3 Trip duration:
total travel time
average travel time

#4 User info:
counts of each user type
counts of each gender (only available for NYC and Chicago)
earliest, most recent, most common year of birth (only available for NYC and Chicago)

You will find python file for the code and the three data files as CSV files for the three countries.
I used pandas for data read and analysis.
