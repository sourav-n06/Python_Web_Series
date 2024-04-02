"""
           2. Write a discount coupon code using dictionary in Python with different rate coupons for
            each day of the week.
""" 

# Dictionary representing discount coupon codes for each day of the week
discount_coupons = {
    'Monday': 'MONDAY20',    # 20% off coupon for Monday
    'Tuesday': 'TUESDAY15',  # 15% off coupon for Tuesday
    'Wednesday': 'WEDNESDAY25',  # 25% off coupon for Wednesday
    'Thursday': 'THURSDAY10',  # 10% off coupon for Thursday
    'Friday': 'FRIDAY30',  # 30% off coupon for Friday
    'Saturday': 'SATURDAY40',  # 40% off coupon for Saturday
    'Sunday': 'SUNDAY50'   # 50% off coupon for Sunday
}

# Take user input for the day of the week
day_of_week = input("Enter the day of the week: ").capitalize()

# Check if the entered day exists in the dictionary
if day_of_week in discount_coupons:
    coupon_code = discount_coupons[day_of_week]
    print(f"Today is {day_of_week}, use coupon code '{coupon_code}' for your discount.")
else:
    print("Sorry, no discount coupon available for the entered day.")
