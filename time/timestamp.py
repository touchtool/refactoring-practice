#  package time
"""
This code creates a datetime.time object from a string.

- Is it easy to verify that it works correctly?
- Do you see any obvious errors?
- How would you modify it to be easier to read?
"""

import datetime


def create_time_from_timestamp(timestamp: str) -> datetime.time:
    """Create a datetime.time object from a string in the form 'hh:mm:ss'.

    Args:
    timestamp - string containing a timestamp in the format 'hh:mm:ss'

    Returns:
    a datetime.time object with value equal to the timestamp

    Raises:
    ValueError if timestamp is not a string in form "hh:mm:ss"

    Example:
    >>> t = create_time_from_timestamp("9:23:15")
    >>> type(t)
    <class 'datetime.time'>
    >>> print(t)
    09:23:15
    """
    hours_min_second = timestamp.split(":")
    if len(hours_min_second) != 3:
        raise ValueError('Timestamp must be "hh:mm:ss"')
    else:
        # if the timestamp is not valid, this may raise TypeError or ValueError
        if 0 <= int(hours_min_second[0]) <= 23 and 0 <= int(hours_min_second[1]) < 60 and 0 <= int(hours_min_second[2]) < 60:
            return datetime.time(int(hours_min_second[0]), int(hours_min_second[1]), int(hours_min_second[2]))
