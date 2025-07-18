# Time Complexity : O(1) for all operations
# Space Complexity : O(maxNumbers) for the sets
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        # Initialize with all numbers from 0 to maxNumbers-1 available
        self.available = set(range(maxNumbers))
        self.used = set()

    def get(self) -> int:
        # Get any available number, return -1 if none available
        if not self.available:
            return -1
        
        # Get and remove a number from available set
        number = self.available.pop()
        self.used.add(number)
        return number

    def check(self, number: int) -> bool:
        # Check if the number is available (not in used set)
        return number in self.available

    def release(self, number: int) -> None:
        # Release a number back to available pool
        if number in self.used:
            self.used.remove(number)
            self.available.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)