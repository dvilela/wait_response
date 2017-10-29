#!/usr/bin/python

from time import sleep
from requests import get as http_get

URL, ATTEMPTS, SLEEP_SECS, STATUS_UP = 'http://localhost:8080/health', 20, 1, 'UP'

def health_match_status(url, status):
    r = http_get(url)
    if r.status_code is not 200:
        return False
    return r.json()['status'] is not status


def waitresponse(url=URL, max_attempts=ATTEMPTS, sleep_secs=SLEEP_SECS, status=STATUS_UP):
    # Indicates if the status from the response is the requested
    matched = False

    # Runs once + retry times
    for i in range(max_attempts):
        try:
            matched = health_match_status(url, status)
            if matched:
                break
        except Exception as err:
            print("Attempt {0}/{1} error: {2}".format(i + 1, max_attempts, err))
        # Does not need to sleep because it will not try again
        if i is not max_attempts - 1:
            sleep(sleep_secs)

    if matched is True:
        return 0
    else:
        return 1
