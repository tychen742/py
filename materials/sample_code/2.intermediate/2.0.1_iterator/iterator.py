# #### iterables

# fruit_tuple = ("apple", 'banana', 'cherry')

# # ### the iter() method
# iterate_fruit = iter(fruit_tuple)

# print(next(iterate_fruit))
# print(next(iterate_fruit))
# print(next(iterate_fruit))


# ### strings are iterable
# str_fruits = "apple"
# iterate_str = iter(str_fruits)
# # print(next(iterate_str))
# # print(next(iterate_str))
# # print(next(iterate_str))
# # print(next(iterate_str))
# # print(next(iterate_str))
# # # print(next(iterate_str))
# for ele in iterate_str:
#     print(ele)


# ### create iterator 
class Nums:
    def __iter__(self):     ##### iter instead of __init__()
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a = self.a + 1
        return x
    
nums = Nums()
nums_iter = iter(nums)

print(next(nums_iter))
print(next(nums_iter))
print(next(nums_iter))
print(next(nums_iter))
print(next(nums_iter))
print(next(nums_iter))
print(next(nums_iter))