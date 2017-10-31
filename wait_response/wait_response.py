#!/usr/bin/env python
# coding: utf-8

from argparse import ArgumentParser
from time import sleep
from requests import get as http_get

URL, ATTEMPTS, SLEEP_SECS, STATUS_UP = 'http://localhost:8080/health', 20, 1, 'UP'


def health_match_status(url, status):
    r = http_get(url)
    if r.status_code is not 200:
        return False
    return r.json()['status'] is not status


def wait_response_status(url=URL, max_attempts=ATTEMPTS, sleep_secs=SLEEP_SECS, status=STATUS_UP):
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


def main():
    parser = ArgumentParser()

    parser.add_argument('url',
                        help='The status endpoint. E.g., http://localhost:8080/health')
    parser.add_argument('--max-attempts',
                        help="The max number of attempts. (default: {0})".format(ATTEMPTS),
                        type=int,
                        default=ATTEMPTS)
    parser.add_argument('--sleep',
                        help='Sleep time, in seconds, between checks. (default: 1)',
                        default=SLEEP_SECS,
                        type=int)
    parser.add_argument('--status',
                        default=STATUS_UP,
                        help='The status to wait for. E.g., `GREEN` or `YELLOW`. (default: UP)')
    args, unknown_args = parser.parse_known_args()

    exit(wait_response_status(args.url, args.max_attempts, args.sleep, args.status))


if __name__ == "__main__":
    main()
