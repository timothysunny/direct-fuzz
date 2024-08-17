# Direct FUZZ
![Direct FUZZ ASCII ART ](https://github.com/timothysunny/direct-fuzz/blob/main/default/dfuzz.png?raw=true)
**Version 0.01**

Direct FUZZ is a simple yet powerful directory Fuzzer written in Python. 


- [Installation](https://github.com/timothysunny/direct-fuzz#installation)
- [Usage](https://github.com/timothysunny/direct-fuzz#usage)
- [Features](https://github.com/timothysunny/direct-fuzz#Features)
- [Todo](https://github.com/timothysunny/direct-fuzz#Todo)


## Installation

1.Clone the repository:
  ```sh
   git clone https://github.com/timothysunny/direct-fuzz.git
 ```

2.Install dependencies:
  ```sh
  cd direct_fuzz
  ```
  ```sh
  pip install -r requirements.txt
  ```

 ## Usage
Using with default wordlist
```bash
python dfuzz.py -u <URL>
```
Using with wordlist path
```bash
python dfuzz.py -u <URL> -w <wordlist>
```


## Features

- ✔️ Basic directory brute-forcing functionality
- ✔️ HTTP status code color coding for easy identification
- ✔️ User-agent customization
- ✔️ Ability to save output

## Todo

- `[ ]` Implement multi-threading for faster directory brute-forcing
- `[ ]` Add support for custom HTTP headers
- `[ ]` Implement timeout handling for requests
- `[ ]` Improve error handling and user messages
- `[ ]` Add more customization options

## License

DirectFuzz is released under MIT license. See [LICENSE](https://github.com/timothysunny/direct-fuzz/blob/main/LICENSE).



