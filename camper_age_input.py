def convert_to_months(age_in_months):
    global age_in_years
    age_in_years = age_in_months / 12
    return age_in_years


if __name__ == '__main__':
    input = input("Enter number :")
    age_in_months = int(input)
    age_in_years = 0

    convert_to_months(age_in_months)
    print(age_in_months, " months",  " is " , int( age_in_years), " years!")

