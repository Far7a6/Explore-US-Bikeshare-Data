import time
import pandas as pd
import numpy as np
Cities = ['chicago' , 'new york city', 'washington']
Months = ['january' , 'february', 'march' , 'april' , 'may' , 'june' , "all" ]
Days = ['monday' , 'tuesday', 'wednesday' , 'thursday' , 'friday' , 'saturday' , 'sunday', "all"]

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
    print ("Here you will input city to explore date from the available cities ,from the following :-")
    for city in Cities :
        print ("-",city , end = " \n")
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        city = input ("please choose acity to view the  bikeshare data!").lower()
        if city not in  CITY_DATA :                                      
            print ("Please choose correct city from the avialable cities list")
        else :
            break
    print ("Here you will input a Month to explore date ")
    for month in Months :
        print ("-",month , end = " \n")          
    # TO DO: get user input for month (all, january, february, ... , june)
    while True :
        month = input ("please choose a month to view the  bikeshare data!").lower()
        if month != "all" and month not in  Months :                                      
            print ("Please choose correct month from the avialable months list")
        else :
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print ("Here you will input a day to explore date ")
    for day in Days :
        print ("-",day , end = " \n")         
    # TO DO: get user input for month (all, january, february, ... , june)
    while True :
        day = input ("please choose a day to view the  bikeshare data!").lower()
        if day != "all" and day not in  Days :                                      
            print ("Please choose correct day from the avialable days list")
        else :
            break

    print('='*50)
    return city,month,day


def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df= pd.read_csv(CITY_DATA[city])
    df["Start_Time"] = pd.to_datetime (df["Start Time"])  # new column to format the start time
    df["month"] = df["Start_Time"].dt.month  
    df["day_of_week"] = df["Start_Time"].dt.weekday_name
    if month != "all" :
        months_list = ['january' , 'february', 'march' , 'april' , 'may' , 'june']
        month = months_list.index(month)+1
        df = df [df["month"] == month]        #to get filter by the required month
    if day != "all" :
        df = df [df["day_of_week"] == day.title()]        #to get filter by the required month

    return df

''' ask user if he need to disply raw dat or no '''

def disply_data(df) :
    j = 0
    user_descion = input ("Dear sir , whould you like to see raw data or not , please answer yes or no:- ").lower()
    pd.set_option ("display.max_columns", None)   #Displays the default number of value. Interpreter reads this value and displays the rows with this value as upper limit to display.
    while True :
        if user_descion == "no" :
            break 
        print (df.iloc[j:(j+5)])
        user_descion = input("Dear sir , whould you like to see raw data or not , please answer yes or no:- ").lower()
        j = j+1


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df["month"].mode()[0]
    print(f" As per tha avialable data , the most common month is {common_month}")

    # TO DO: display the most common day of week
    common_day = df["day_of_week"].mode()[0]
    print(f" As per tha avialable data , the most common day is {common_day}")

    # TO DO: display the most common start hour
    common_start_hour = (df["Start_Time"].dt.hour).mode()[0]
    print(f" As per tha avialable data , the most common start hour is {common_start_hour}")           

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*50)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df["Start Station"].mode()[0]
    print(f" As per tha avialable data , the most common start station is {common_start_station}") 

    # TO DO: display most commonly used end station
    common_end_station = df["End Station"].mode()[0]
    print(f" As per tha avialable data , the most common end station is {common_end_station}") 

    # TO DO: display most frequent combination of start station and end station trip
    group_field_between_two_stations =df.groupby(['Start Station','End Station'])
    common_start_end_stations = group_field_between_two_stations.size().sort_values(ascending=False).head(1)    # rank will wii be the populay                         
    print(f" As per tha avialable data , the most common combination btween start and end station is {common_end_station}") 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*50)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print(f" As per tha avialable data , total travel time is {total_travel_time}") 

    # TO DO: display mean travel time
    average_travel_time = df["Trip Duration"].mean()
    print(f" As per tha avialable data , average travel time is {average_travel_time}") 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*50)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_user_type = df["User Type"].value_counts()

    # TO DO: Display counts of gender
    if "Gender" in df :
        print (f"As per tha avialable data ,count of gender {count_of_user_type}")
        

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df :
        earliest_year_of_birth = int(df["Birth Year"].min())
        print (f"As per tha avialable data ,the earliest year of birth {earliest_year_of_birth}")
        recent_year_of_birth = int(df["Birth Year"].max())
        print (f"As per tha avialable data ,the recent year of birth {recent_year_of_birth}")
        common_year_of_birth = int(df["Birth Year"].mode()[0])
        print (f"As per tha avialable data ,the common year of birth {common_year_of_birth}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*50)


def main():
    while True:
        city, month ,day = get_filters()
        df = load_data(city, month ,day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        disply_data(df)
                                   

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
