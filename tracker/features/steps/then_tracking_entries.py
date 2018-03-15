from behave import then


@then('there is {number_of_entries} tracking entry started at {time} with {minutes} minutes length')
def step(context, number_of_entries, time, minutes):
    pass