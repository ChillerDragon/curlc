#!/usr/bin/env python3

from pycookiecheat import chrome_cookies
import subprocess
import sys

def main():
    if len(sys.argv) < 2:
        print("usage: curlc [url] <curl args...>")
        sys.exit(1)

    curlargs = sys.argv[1:]
    for arg in curlargs:
        if arg[0] != '-':
            url = arg
            break

    chrome = chrome_cookies(url)

    cargs = []
    carg = "cookie: "
    for k, v in chrome.items():
        cargs.append(k + "=" + v)
    carg += "; ".join(cargs)

    args = ["curl", "-H", carg]
    args.extend(curlargs)
    subprocess.run(args)


if __name__ == '__main__':
    main()
