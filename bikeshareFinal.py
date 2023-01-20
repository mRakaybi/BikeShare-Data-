import time
import pandas as pd 
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=str(input("Please enter the city to analyze (chicago, new york city, washington): ")).lower()
    while city not in ["chicago", "new york city", "washington"]:
        city=input("Please enter a valid city: ")

    # get user input for month (all, january, february, ... , june)
    month=str(input("Please enter the month to analyze (all, january, february, ... , june): ")).lower()
    while month.lower() not in ["all", "january", "february","march","april","may","june"]:
        month=input("Please enter a valid month or all: ")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=str(input("Please enter the day to analyze (all, monday, tuesday, ... sunday): ")).lower()
    while day not in ["all", "monday", "tuesday","wednesday","thursday","friday","saturday","sunday"]:
        day=input("Please enter a valid day or all: ")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
       # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city]) 
        
    # convert the Start Time column to datetime
    df['Start Time'] =pd.to_datetime(df["Start Time"])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df["Start Time"].dt.month
    df['day_of_week'] = df["Start Time"].dt.dayofweek


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df.loc[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = [ 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday','sunday']
        day=days.index(day)
        df = df.loc[df['day_of_week']==day]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['month'] =df["Start Time"].dt.month
    popular_month = df["month"].mode()[0]
    print('Most common month:', popular_month)

    # display the most common day of week
    df['day'] =df["Start Time"].dt.dayofweek
    popular_day = df["day"].mode()[0]
    print('Most common day of week:', popular_day)

    # display the most common start hour
    df['hour'] =df["Start Time"].dt.hour
    popular_hour = df["hour"].mode()[0]
    print('Most common start hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most commonly used start station:', df["Start Station"].mode()[0])

    # display most commonly used end station
    print('Most commonly used end station:', df["End Station"].mode()[0])

    # display most frequent combination of start station and end station trip
    print('Most frequent combination of start station and end station trip:', df.groupby(['Start Station','End Station']).size().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    hours=df["Trip Duration"].sum()//3600
    minutes=(df["Trip Duration"].sum()%3600)//60
    seconds=(df["Trip Duration"].sum()%3600)%60
    print("The Total Travel time is: {} hours, {} minutes, {} seconds.".format(hours,minutes,seconds))

    # display mean travel time
    hours=df["Trip Duration"].mean()//3600
    minutes=(df["Trip Duration"].mean()%3600)//60
    seconds=(df["Trip Duration"].mean()%3600)%60
    print("The Mean Travel time is: {} hours, {} minutes, {} seconds.".format(hours,minutes,seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("The counts of user types is: \n", df["User Type"].value_counts())
    #Handle the washington city lack of data
    if city=="washington":
        print("The Gender and Birth_Year Data are not avilable in this city!!")
    else:
        # Display counts of gender
        print("The counts of gender: \n", df["Gender"].value_counts())

        # Display earliest, most recent, and most common year of birth
        print("The earliest year of birth for users is: ", df["Birth Year"].min())
        print("The most recent year of birth for users is: ", df["Birth Year"].max())
        print("The most common year of birth for users is: ", df["Birth Year"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #Display the raw data five by five rows
        showData=str(input("\nWould you like to display top 5 Rows of Data?(yes/no)\n")).lower()
        i=0
        while showData=="yes":
            print(df.iloc[i:i+5])
            i+=5
            showData=str(input("\nWould you like to display next 5 Rows of Data?(yes/no)\n")).lower()
        #Analyze data and display stats
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
