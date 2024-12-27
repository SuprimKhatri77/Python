age = 30
day = "wednesday"

if age < 18 and day == 'wednesday':
    print("you can get a discount")
elif age < 18 and day != 'wednesday':
    print("you cannot get a discount")
elif age > 18 and day == 'wednesday':
    print("you can get a discount and tkt price is: $10")
# elif age > 18 and day != 'wednesday':
else :
    print("you cannot get a discount and tkt price is $12")