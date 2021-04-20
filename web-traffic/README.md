**Configurations**

- `MAX_DEPTH = 10`, `MIN_DEPTH = 5` Starting from each root URL generator will click to a depth
  radomly selected between MIN_DEPTH and MAX_DEPTH.
- **The interval between every HTTP GET requests is chosen at random between the following two variables...***
- `MIN_WAIT = 5` Wait a minimum of `5` seconds between requests
- `MAX_WAIT = 10`
- `DEBUG = False`
- `ROOT_URLS = [url1,url2,url3]` The list of root URLs to start from when browsing. Randomly selected.
- `blacklist = [".gif", "intent/tweet", "badlink", etc...]` A blacklist of strings that we check every link against. If the link contains any of the strings in this list, it's discarded.
- `userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3)'`

## Dependencies

```bash
sudo pip install requests
```

## Usage

edit config file:

```bash
nano config.py
```

Run the generator:

```bash
python gen.py
```

## Troubleshooting and debugging

change `DEBUG` to True
