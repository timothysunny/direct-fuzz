# Direct FUZZ

**Version 1.0**

Direct FUZZ is a simple yet powerful directory brute-forcer written in Python. It helps in discovering hidden directories on a web server by making requests to the server and checking the response codes.

## Features

- ✔️ Basic directory brute-forcing functionality
- ✔️ HTTP status code color coding for easy identification
- ✔️ User-agent customization
- ✔️ Progress bar with tqdm

 ## Usage

```bash
python dfuzz.py -u <URL> -w <wordlist>
```

## Installation

1. Clone the repository:
  ```sh
   git clone https://github.com/timothysunny/Direct-fuzz.git
 ```

2. Install dependencies:
  ```sh
  cd direct_fuzz
  ```
  ```sh
  pip install -r requirement.txt
  ```
## Todo

- `[ ]` Implement multi-threading for faster directory brute-forcing
- `[ ]` Add support for custom HTTP headers
- `[ ]` Implement timeout handling for requests
- `[ ]` Improve error handling and user messages
- `[ ]` Add more customization options


