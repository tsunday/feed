from behave import when


@when('user {user} starts event today at {time}')
def step(context, user, time):
    pass


@when('user {user} stops event today at {time}')
def step(context, user, time):
    pass


@when('user {user} registers {minutes} minutes length event at {time}')
def step(context, user, minutes, time):
    pass
