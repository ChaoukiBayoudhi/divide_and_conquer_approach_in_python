class MaxSubarray:
    def __init__(self, arr=None):
        self.arr = arr if arr is not None else []
    
    def find_max_crossing_subarray(self, low, mid, high):
        left_sum = float('-inf')
        sum_val = 0
        max_left = mid
        for i in range(mid, low - 1, -1):
            sum_val += self.arr[i]
            if sum_val > left_sum:
                left_sum = sum_val
                max_left = i

        right_sum = float('-inf')
        sum_val = 0
        max_right = mid + 1
        for j in range(mid + 1, high + 1):
            sum_val += self.arr[j]
            if sum_val > right_sum:
                right_sum = sum_val
                max_right = j

        return max_left, max_right, left_sum + right_sum
    
    def find_max_crossing_subarray_advanced(self, low, mid, high):
        """Advanced version using more Pythonic constructs"""
        # Left part
        left_sums = []
        running_sum = 0
        for i in range(mid, low - 1, -1):
            running_sum += self.arr[i]
            left_sums.append((running_sum, i))
        
        max_left_sum, max_left = max(left_sums, key=lambda x: x[0], default=(float('-inf'), mid))
        
        # Right part
        right_sums = []
        running_sum = 0
        for j in range(mid + 1, high + 1):
            running_sum += self.arr[j]
            right_sums.append((running_sum, j))
        
        max_right_sum, max_right = max(right_sums, key=lambda x: x[0], default=(float('-inf'), mid + 1))
        
        return max_left, max_right, max_left_sum + max_right_sum

    def find_max_subarray(self, low, high):
        if low == high:
            return low, high, self.arr[low]

        mid = (low + high) // 2

        left_low, left_high, left_sum = self.find_max_subarray(low, mid)
        right_low, right_high, right_sum = self.find_max_subarray(mid + 1, high)
        cross_low, cross_high, cross_sum = self.find_max_crossing_subarray(low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum
    
    def find_max_subarray_advanced(self, low, high):
        """Advanced version using more Pythonic constructs"""
        if low == high:
            return low, high, self.arr[low]

        mid = (low + high) // 2

        # Recursive calls
        subarrays = [
            self.find_max_subarray_advanced(low, mid),
            self.find_max_subarray_advanced(mid + 1, high),
            self.find_max_crossing_subarray_advanced(low, mid, high)
        ]
        
        # Return the subarray with maximum sum using max() with a key function
        return max(subarrays, key=lambda x: x[2])
    
    def find_maximum_subarray(self):
        """Convenience method to find the maximum subarray in the entire array"""
        if not self.arr:
            return None, None, 0
        return self.find_max_subarray(0, len(self.arr) - 1)
    
    def find_maximum_subarray_advanced(self):
        """Advanced version of the convenience method"""
        return self.arr and self.find_max_subarray_advanced(0, len(self.arr) - 1) or (None, None, 0)
    
    def set_array(self, arr):
        """Set a new array to work with"""
        self.arr = arr
    
    def set_array_advanced(self, arr):
        """Advanced version using type hinting and validation"""
        from typing import List, Union, Optional
        
        # Type checking (Python 3.5+)
        if not isinstance(arr, (list, tuple)) and arr is not None:
            raise TypeError(f"Expected list or None, got {type(arr).__name__}")
        
        # Use walrus operator for assignment with validation (Python 3.8+)
        if (new_arr := arr or []):
            self.arr = list(new_arr)
        else:
            self.arr = []
        
        return self  # Enable method chaining
    
    def fill_from_keyboard(self):
        """Fill the array with values entered from the keyboard"""
        try:
            n = int(input("Enter the number of elements: "))
            if n < 0:
                print("Number of elements cannot be negative. Setting to 0.")
                n = 0
                
            self.arr = []
            for i in range(n):
                try:
                    value = float(input(f"Enter element {i+1}: "))
                    self.arr.append(value)
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    i -= 1  # Retry this index
            
            print(f"Array filled with {len(self.arr)} elements.")
            return self
        except ValueError:
            print("Invalid input for number of elements. Array not modified.")
            return self
    
    def fill_randomly(self, size=10, min_val=-100, max_val=100):
        """Fill the array with random values
        
        Args:
            size (int): Number of elements to generate
            min_val (int/float): Minimum value for random numbers
            max_val (int/float): Maximum value for random numbers
        """
        import random
        
        if size < 0:
            print("Size cannot be negative. Setting to 0.")
            size = 0
            
        self.arr = [random.uniform(min_val, max_val) for _ in range(size)]
        
        # Convert to integers if min and max are integers
        if isinstance(min_val, int) and isinstance(max_val, int):
            self.arr = [int(random.randint(min_val, max_val)) for _ in range(size)]
            
        print(f"Array filled with {size} random values between {min_val} and {max_val}.")
        return self


# Example usage
if __name__ == "__main__":
    arr = [2, -4, 3, -1, 2, -4, 3]
    
    # Using original methods
    max_subarray = MaxSubarray(arr)
    low, high, max_sum = max_subarray.find_maximum_subarray()
    print(f'Original implementation:')
    print(f'Maximum subarray sum: {max_sum}')
    print(f'Maximum subarray: {arr[low:high+1]}')
    
    # Using advanced methods
    max_subarray_adv = MaxSubarray(arr)
    low_adv, high_adv, max_sum_adv = max_subarray_adv.find_maximum_subarray_advanced()
    print(f'\nAdvanced implementation:')
    print(f'Maximum subarray sum: {max_sum_adv}')
    print(f'Maximum subarray: {arr[low_adv:high_adv+1]}')
    
    # Verify both implementations give the same result
    assert max_sum == max_sum_adv, "Both implementations should give the same result"
    print("\nBoth implementations give the same result!")
    
    # Example of using the new methods
    print("\nFilling array with random values:")
    random_array = MaxSubarray().fill_randomly(size=8, min_val=-10, max_val=10)
    print(f"Random array: {random_array.arr}")
    low, high, max_sum = random_array.find_maximum_subarray()
    print(f'Maximum subarray sum: {max_sum}')
    print(f'Maximum subarray: {random_array.arr[low:high+1]}')
    
    print("\nTo fill from keyboard, uncomment and run the following code:")
    print("# keyboard_array = MaxSubarray().fill_from_keyboard()")
    print("# low, high, max_sum = keyboard_array.find_maximum_subarray()")
    print("# print(f'Maximum subarray sum: {max_sum}')")
    print("# print(f'Maximum subarray: {keyboard_array.arr[low:high+1]}')")
