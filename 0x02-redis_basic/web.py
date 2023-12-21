#!/usr/bin/env python3
"""
implement a get_page function (prototype: def get_page(url: str) -> str:).
The core of the function is very simple.
It uses the requests module to obtain the HTML content of a
particular URL and returns it.

Inside get_page track how many times a particular URL was
accessed in the key "count:{url}"
and cache the result with an expiration time of 10 seconds.

Tip: Use http://slowwly.robertomurray.co.uk to simulate
a slow response and test your caching.

Bonus: implement this use case with decorators.
"""

import requests
import time
import functools

"""
Dictionary to store cached results and access counts
"""

cache = {}


def get_page(url: str) -> str:
    """
    test
    """
    cache_key = f"count:{url}"
    """
    Check if the result is in the cache and not expired
    """

    if cache_key in cache and time.time() - cache[cache_key]["timestamp"] < 10:
        cache[cache_key]["count"] += 1
        print(f"Cache hit for {url}. Access count:
              {cache[cache_key]['count']}")
        return cache[url]["content"]

    """
    Fetch the page using requests
    """
    response = requests.get(url)
    content = response.text

    """
    Update the cache with the new result
    """
    cache[cache_key] = {"content": content,
                        "timestamp": time.time(), "count": 1}

    return content


def cache_decorator(func):
    """
    test
    """
    @functools.wraps(func)
    def wrapper(url):
        """
        test
        """
        cache_key = f"count:{url}"

        """
        Check if the result is in the cache and not expired
        """
        if cache_key in cache and time.time() - cache[
                                                cache_key]["timestamp"] < 10:

            cache[cache_key]["count"] += 1
            print(f"Cache hit for {url}. Access count:
                  {cache[cache_key]['count']}")
            return cache[url]["content"]

        """
        If not in the cache, call the original function
        """
        result = func(url)

        """
        Update the cache with the new result
        """
        cache[cache_key] = {"content": result,
                            "timestamp": time.time(), "count": 1}

        return result

    return wrapper


@cache_decorator
def get_page_with_decorator(url: str) -> str:
    """
    Fetch the page using requests
    """
    response = requests.get(url)
    content = response.text
    return content
