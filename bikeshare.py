import time
import pandas as pd
import numpy as np
import statistics as st

###loading data
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
###choose the right data function
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
   #LIST FOR ALL I NEED
   # for easy check
    city_list =  ["chicago","new york city","washington"]
    month_list = ["all","january", "february", "march", "april", "may", "june"]
    day_list = ["all","sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

  # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs 
    while 1:
        city = input("choose a city Chicago, New York city, or Washington?\n ")
        if city.lower() in city_list:
            break
            
# TO DO: get user input for month (all, january, february, ... , june)
    while 1:
        month = input("choose a month  January, February, March, April, May, June or all ? \n")
        if month.lower() in month_list:
            break
            
# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while 1:
        day = input("choose a  day monday, tuesday, wednesday, thursday, friday, saturday , sunday or all ? \n")
        if day.lower() in day_list:
            break
            
    print('-'*40)
    
    #return then in lower case , just in case.
    city = city.lower()
    month = month.lower()
    day = day.lower()
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
   # name_data = city+".csv" #creat string and add ".hsv" to the city selected to read it 
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        #used to find index of month.
        month = months.index(month) + 1       

        df = df[df['Start Time'].dt.month == month]
        
    #filter data by day.
    if day != 'all': 
        df = df[df['Start Time'].dt.weekday_name == day.title()]

    return df

### git the time from the table 
def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
     # display the most common month
    if(month == 'all'):
        most_common_month = df['Start Time'].dt.month.value_counts().idxmax()
        print('Most common month is ' + str(most_common_month))

    # display the most common day of week
    if(day == 'all'):
        most_common_day = df['Start Time'].dt.weekday_name.value_counts().idxmax()
        print('Most common day is ' + str(most_common_day))

    # display the most common start hour
    most_common_hour = df['Start Time'].dt.hour.value_counts().idxmax()
    print('Most popular hour is ' + str(most_common_hour))
    
    ########################################
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(" most commonly start station {} \n".format(st.mode(df['Start Station'])))
    # TO DO: display most commonly used end station
    print(" most commonly end station {} \n".format(st.mode(df['End Station'])))


    # TO DO: display most frequent combination of start station and end station trip
    combination = df['Start Station'].astype(str) + " to " + df['End Station'].astype(str)
    both = combination.value_counts().idxmax()
    
    print(" most frequent combination {} \n".format(both) ) # df['both'].mode())
        
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

### get the trip duration
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Duration'] = df['Trip Duration']

    total_travelTime = df['Duration'].sum()
    print('total_travelTime= ',total_travelTime/ (26*3600) ,"day and ",total_travelTime/3600 ,"hour and ",total_travelTime/60 ,"min")

    # TO DO: display mean travel time
    mean_time =df['Duration'].mean() 
    print("mean travel time= ",mean_time/ (24*3600) ,"day and ",mean_time/3600 ,"hour and ",mean_time/60 ,"min") 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    if 'User Type' in df:
    # TO DO: Display counts of user types
        no_of_subscribers = df['User Type'].str.count('Subscriber').sum()
        no_of_customers = df['User Type'].str.count('Customer').sum()
        no_of_Dependent =df['User Type'].str.count('Dependent').sum()
        print('\nNumber of subscribers are {}\n'.format(int(no_of_subscribers)))
        print('\nNumber of customers are {}\n'.format(int(no_of_customers)))    
        print('\nNumber of Dependent are {}\n'.format(int(no_of_Dependent)))    
    
   
    # TO DO: Display counts of gender
    if 'Gender' in df:
        male_count = df['Gender'].str.count('Male').sum()
        female_count = df['Gender'].str.count('Female').sum()
        print('Number of male users are {} \n'.format(int(male_count)))
        print('Number of female users are {} \n'.format(int(female_count)))

    else :
       print("unkown")
       print('dataframe of the city you select did not have gender data')
    # TO DO: Display earliest, most recent, and most common year of birth
    print("\n")
    if 'Birth Year' in df:
        earliest_birth = int (df['Birth Year'].min() )
        print("earliest_birth= ", earliest_birth)
        recet_birth = int (df['Birth Year'].max() )
        print("recet_birth= ",recet_birth)
        mostCommon_birth =int (df['Birth Year'].mode())
        print("mostCommon_birth= ",mostCommon_birth )
    else :
       print("unkown")
       print('dataframe of the city you select did not have Birth Year data')
    print("\n")    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def see_data(df):
    n=0
    while 1: 
        x = input("do you want to see five row of data u selected yes or no > ")
        if x.lower() == "yes" or x.lower() == "y":
            print(df.iloc[n:n+5,:])
            n+=5
            print("\n")
        else :
            break
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        see_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
