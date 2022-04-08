logged_in = True
standard_user = True

if logged_in and not standard_user:
    print('you can access the admin dashboard')
else:
    print('you can only access the standard dashboard')