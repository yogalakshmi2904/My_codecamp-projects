import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = df[df["sex"]=="Male"]["age"].mean().round(2)

    # What is the percentage of people who have a Bachelor's degree?
    Num_bachelors=len(df[df["education"]=="Bachelors"])
    total_num=len(df)
    Num_bachelors=len(df[df["education"]=="Bachelors"])
    percentage_bachelors = round(Num_bachelors/total_num * 100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    df_higher=df[df["education"].isin(["Bachelors", "Masters","Doctorate"])]
    num_higher_edu=len(df_higher["education"])
    num_higher_edu
    more_than_50= df_higher[df_higher["salary"]==">50K"]
    num_morethan50=len(more_than_50)
    round(num_morethan50/num_higher_edu * 100,1)
    # What percentage of people without advanced education make more than 50K?
    lower_edu = df[~df["education"].isin(["Bachelors", "Masters","Doctorate"])]
    total_lower_edu=len(lower_edu["education"])
    lower_morethan50=len(lower_edu[lower_edu["salary"]==">50K"])
    round(lower_morethan50/total_lower_edu * 100,1)

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df["education"].isin(["Bachelors", "Masters","Doctorate"])]
    lower_education = df[~df["education"].isin(["Bachelors", "Masters","Doctorate"])]

    # percentage with salary >50K
    higher_education_rich = round(num_morethan50/num_higher_edu * 100,1)
    lower_education_rich = round(lower_morethan50/total_lower_edu * 100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers=df[df["hours-per-week"]==1]
    num_min_workers =len(min_workers["hours-per-week"])
    rich_min=len(min_workers[min_workers["salary"]==">50K"])
    rich_percentage = round(rich_min/num_min_workers*100,1)

    # What country has the highest percentage of people that earn >50K?
    country_based=more_than_50["native-country"].value_counts()
    country_count=df["native-country"].value_counts()
    highest_earning_country = round(country_based/country_count*100,1).idxmax()
    highest_earning_country_percentage = round(country_based/country_count*100,1).max()

    # Identify the most popular occupation for those who earn >50K in India.
    peopleInIndia=df[df["native-country"]=="India" ]
    numberofIndian=peopleInIndia["native-country"].value_counts()
    top_IN_occupation = (peopleInIndia["native-country"]==">50K").value_counts()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
