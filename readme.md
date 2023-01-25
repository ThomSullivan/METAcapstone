Homepage found at /restaurant

API ENDPOINTS
/auth/users/
    GET with token retrieves user information
    POST with {username} and {password} registers user

/auth/token/login
    POST with {username} and {password} of a registered user returns user token

/restaurant/menu/
    GET lists paginated menu items. Throttled to 5 requests per minute for anon users
    POST from superuser creates menu item given {title}, {price}, and {inventory}

/restaurant/booking/tables/
    GET lists all bookings to authenticated users
    POST adds a table booking given {name} and {bookingDate | (YYYY-MM-DDT00:00)} 

SUPERUSER LOGIN : thom
SUPERUSER PASSWORD : password
SUPERUSER TOKEN : f598e314fd4fe3c411a83c3c8299f45abe9ca44e

USER LOGIN : Bowser
USER PASSWORD : lemon@bow!
USER TOKEN : 94fe78b9ffa8454631eacb5ddeb1b517483c7c89