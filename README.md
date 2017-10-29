Wait for some HTTP response
===========================

Written in order to make functional tests less complicated.

Retries a HTTP request until it responds as expected or reaches
the max attempt number.

------------------------------------------------------------------

Lets say we have an endpoint `http://localhost:8080/health` that give
us a json, e.g., `{ "status": "UP" }`. This script keep checking that endpoint
until it receives the `UP` status or it reaches the max number of attempts.

# Module

You can use a function from the module to wait for status responses.

```python
import waitresponse
from waitresponse import waitresponse

# Make 2 attempts to get status=UP, trying every 1 seconds. 
respCode = waitresponse('http://localhost:8080/health', 2, 1, 'UP')
print(respCode) # 0 if sucess or else, 1

```

# Script

`python waitresponse.py url [OPTIONS]`

`url` is the required endpoint, e.g., `http://localhost:8080/health`.

## Options

* `--max-attempts default=20` The max number of attempts.
* `--sleep defaul=1` Sleep time, in seconds, between checks.
* `--status default=UP` The status to wait for. E.g., `GREEN` or `YELLOW`.
