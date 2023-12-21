#!/usr/bin/env python3
"""
Create a Cache class.
In the __init__ method, store an instance of the Redis client as
a private variable named _redis (using redis.Redis())
and flush the instance using flushdb.

Create a store method that takes a data argument and
returns a string. The method should generate a
random key (e.g. using uuid),
store the input data in Redis using the random key and
return the key.

Type-annotate store correctly.
Remember that data can be a str, bytes, int or float.
"""

import uuid
import redis
from typing import Union, Callable
import functools


@staticmethod
def call_history(method: Callable) -> Callable:
    """
    Familiarize yourself with redis
    commands RPUSH, LPUSH, LRANGE, etc.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"

        # Append input arguments to the inputs list
        self._redis.rpush(inputs_key, str(args))

        # Execute the wrapped function to retrieve the output
        result = method(self, *args, **kwargs)

        # Store the output in the outputs list
        self._redis.rpush(outputs_key, str(result))

        return result

    return wrapper


@staticmethod
def count_calls(method):
    """
    Familiarize yourself with the INCR command and
    its python equivalent.
    """
    counts = {}

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        counts[key] = counts.get(key, 0) + 1
        result = method(self, *args, **kwargs)
        # print(f"Method {key} has been called {counts} times.")
        return result

    return wrapper


class Cache ():
    """
    has an __init__ () which will store an instance of the Redis
    client as a private variable named _redis.
    """
    def __init__(self) -> None:
        """
        we create a variable redis, connect it to the Redis()
        database running, and the flush it to clear any contents.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    """
    the same class is to have a store() which does have an argument
    data that gives a string as an output. However, the output is to
    be a random key generated by uuid and is to be stored in Redis along
    with the data.
    input data || random key || store them - i guess keys are the ids.
    """
    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        as described above
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: callable =
            None) -> Union[str, bytes, int, float, None]:
        """
        This method gets a key in a string format and an callable argument
        which are to be arguments. The callable argument fn is to be used
        to cnvert the data || i think represented by the key, to its
        original state/format.
        """
        key_value = self._redis.get(key)
        if key_value is not None and fn is not None:
            return fn(key_value)
        return key_value

    def get_str(self, key: str) -> Union[str, None]:
        """
        The get_str method is a convenience method for retrieving
        a string value associated with a key.
        It uses the get method with a conversion function that
        decodes bytes using UTF-8 (d.decode("utf-8"))
        if the value is not None.
        If the value is None, it returns None.
        """
        return self.get(key,
                        fn=lambda d: d.decode("utf-8")
                        if d else None)

    def get_int(self, key: str) -> Union[int, None]:
        """
        The get_int method is a convenience method for retrieving
        an integer value associated with a key.
        It uses the get method with a conversion function
        that converts bytes to an integer (int(d))
        if the value is not None. If the value is None,
        it returns None.
        """
        return self.get(key, fn=lambda d: int(d)
                        if d else None)
