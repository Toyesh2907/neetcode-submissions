class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        try:
            self.timeMap[key].append([value, timestamp])
        except KeyError:
            self.timeMap[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
    
        arr = self.timeMap[key]
    
        left, right = 0, len(arr) - 1
        ans = ""
    
        while left <= right:
            middle = (left + right) // 2
    
            if arr[middle][1] <= timestamp:
                ans = arr[middle][0]
                left = middle + 1
            else:
                right = middle - 1
    
        return ans