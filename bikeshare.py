import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters(city, month, day):
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nSelect city: Chicago, New York City or Washington!\n").lower()
        if city not in CITY_DATA:
            print("\nInvalid answer\n")
            continue   
        else:
            break

    while True:
        time = input("\nWould you like to filter by month, day, all or none?\n").lower()               
        if time == 'month':
            month = input("\nWhich month? January, Feburary, March, April, May or June?\n").lower()
            day = 'all'
            break
                    
        elif time == 'day':
            month = 'all'
            day = input("\nWhich day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday\n").lower()
            break
                    
        elif time == 'all':
            month = input("\nWhich month? January, Feburary, March, April, May or June?\n").lower()           
            day = input("\nWhich day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday\n").lower()
            break       
        elif time == 'none':
            month = 'all'
            day = 'all'
            break       
        else:
            input("\nWrong Entry! Kindly Retype. month, day, all or none?\n")
            break

    print(city)
    print(month)
    print(day)
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
       
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
      

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month of travels is: ' +
          str(common_month).title() + '.')


    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('Most common day of travels is: ' +
          str(common_day_of_week).title() + '.')


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common hour of travels is: ' +
          str(common_hour).title() + '.')

    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('The most commonly used start station is: ' + common_start.title() + '.')

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('The most commonly used start station is: ' + common_end.title() + '.')

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['combination'].mode()[0]
    print('The most frequent combination of start and end station trip is: ' +
          common_combination.title() + '.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print('The total travel time is: ' + str(total_travel).title() + '.')

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('The mean travel time is: ' + str(mean_travel).title() + '.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nThe count of user types is: \n')
    print(str(user_types).title() + '.')

    # Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('\nThe count of gender is: \n')
        print(str(gender).title() + '.')
    else:
        print("\nThere is no gender information in this city.\n")


    # Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest = df['Birth_Year'].min()
        print('The earliest year of birth is: ' + str(earliest).title() + '.')
        recent = df['Birth_Year'].max()
        print(recent)
        common_birth = df['Birth Year'].mode()[0]
        print(common_birth)
    else:
        print("\nNo information found for birth year, for this city.\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

"""Asking 5 lines of the raw data and more, if they want"""
def data(df):
    raw_data = 0
    while True:
        answer = input("Do you want to see the raw data? Yes or No").lower()
        if answer not in ['yes', 'no']:
            answer = input("Wrong entry! Kindly type Yes or No.").lower()
        elif answer == 'yes':
            raw_data += 5
            print(df.iloc[raw_data : raw_data + 5])
            again = input("See more? Yes or No").lower()
            if again == 'no':
                break
        elif answer == 'no':
            return


def main():
    city = ""
    month = ""
    day = ""
    while True:
        city, month, day = get_filters(city, month, day)
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()