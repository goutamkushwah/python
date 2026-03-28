def login_required(func):
    def wrapper(user_logged_in):
        if user_logged_in:
            func(user_logged_in)
        else:
            print("Access Denied")
    return wrapper


@login_required
def view_dashboard(user_logged_in):
    print("Welcome to Dashboard")


view_dashboard(True)
view_dashboard(False)