class Underscore:
    # 1. Map: applies the callback to every element and returns a new list with the results
    def map(self, iterable, callback):
        result = []
        for item in iterable:
            result.append(callback(item))
        return result

    # 2. Find: returns the first element that satisfies the callback condition
    def find(self, iterable, callback):
        for item in iterable:
            if callback(item):
                return item
        return None  # no matching element found

    # 3. Filter: keeps only the elements for which the callback returns True
    def filter(self, iterable, callback):
        result = []
        for item in iterable:
            if callback(item):
                result.append(item)
        return result

    # 4. Reject: opposite of filter — keeps only the elements for which the callback returns False
    def reject(self, iterable, callback):
        result = []
        for item in iterable:
            if not callback(item):
                result.append(item)
        return result


# =========================================================================
# Tests
# =========================================================================

# create an instance of the class
_ = Underscore()

# map: multiply every number by 2
print(_.map([1, 2, 3], lambda x: x * 2))
# expected: [2, 4, 6]

# find: first number greater than 4
print(_.find([1, 2, 3, 4, 5, 6], lambda x: x > 4))
# expected: 5

# filter: keep even numbers only
print(_.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))
# expected: [2, 4, 6]

# reject: drop even numbers, keep odd ones
print(_.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))
# expected: [1, 3, 5]