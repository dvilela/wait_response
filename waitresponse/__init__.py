import argparse

from .waitresponse import waitresponse, ATTEMPTS, SLEEP_SECS, STATUS_UP

def main():
    parser = argparse.ArgumentParser()

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
    args, unknown_args  = parser.parse_known_args()

    exit(waitresponse(args.url, args.max_attempts, args.sleep, args.status))

if __name__ == "__main__":
    main()
