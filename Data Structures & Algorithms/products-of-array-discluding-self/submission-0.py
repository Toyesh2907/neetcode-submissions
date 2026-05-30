def calculate_array_product_and_zeros(nums: List[int]) -> Tuple(int, int):
    zero_count = 0
    product = 1
    for number in nums:
        if number == 0:
            zero_count += 1
            if zero_count == 2:
                return 0, 0
        else:
            product *= number
    return product, zero_count

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product, zero_count = calculate_array_product_and_zeros(nums = nums)
        array_length = len(nums)
        if zero_count == 2:
                    return [0] * array_length
        product_except_self = []
        for number in nums:
            if number == 0:
                product_except_self.append(product)
            else:
                if zero_count == 1:
                    product_except_self.append(0)
                else:
                    product_except_self.append(int(product/number))

        return product_except_self