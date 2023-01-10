
# API Automation Framework

API automation framework using **Requests** library. The requests module allows you to send HTTP requests using Python.
requests module also provides the ability to validate the HTTP Responses received from the server. For e.g. we can verify the Status code, Status message and even the Body of the response. 
This makes requests a very flexible library that can be used for testing.


## Installation

•	**requests** : The requests module allows you to send HTTP requests using Python.

•	**pytest** : Python UnitTest framework

•	**pytest-html** : PyTest HTML Reports

## API Documentation

https://restful-booker.herokuapp.com/apidoc/index.html


## Running Tests


**CreateToken**
```bash
  pytest -m auth  OR  pytest RestfulBooker/tests/test_create_auth_token.py
```

**GetBookingIds** : Returns the ids of all the bookings that exist within the API.
```bash
  pytest -m getallbooking  OR  pytest RestfulBooker/tests/test_get_booking.py::TestGetBooking::test_get_all_booking_ids
```

**Filter by name**
```bash
  pytest -m getbookingbyfilter  OR  pytest RestfulBooker/tests/test_get_booking_by_filter.py
```

**GetBooking**  : Returns a specific booking based upon the booking id provided
```bash
  pytest -m getspecificbooking  
  OR pytest RestfulBooker/tests/test_get_booking.py::TestGetBooking::test_get_specific_booking
```

**CreateBooking**  : Creates a new booking in the API
```bash
  pytest -m createbooking  OR  pytest RestfulBooker/tests/test_create_booking.py
```

**UpdateBooking**  : Updates a current booking
```bash
  pytest -m updatebooking  OR  pytest RestfulBooker/tests/test_update_booking.py
```

**PartialUpdateBooking**  : Updates a current booking with a partial payload
```bash
  pytest -m partialupdatebooking  OR  pytest RestfulBooker/tests/test_partial_update_booking.py
```

**DeleteBooking**  : Updates a current booking with a partial payload
```bash
  pytest -m deletebooking  OR  pytest RestfulBooker/tests/test_delete_booking.py
```
