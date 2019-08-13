# 两数之和

def twoSum(nums, target):

    temp_dict = {nums[0]: [0] }

    for i in range(1,len(nums)):
        key = nums[i]
        if key in temp_dict.keys():
            value = temp_dict[key]
            value.append(i)
        else:
            value = [i]
            temp_dict[key] = value

    # print(temp_dict)

    for key, value in temp_dict.items():
        frac = target - key

        if frac == key:
            if len(temp_dict[frac]) > 1:
                return [value[0], value[1]]
            else:
                print('not exist')
        elif frac in temp_dict.keys():

            return [value[0], temp_dict[frac][0]]



def twoSum_improve(nums, target):
    # temp_dict = {nums[i]:i for i in range(len(nums))}
    temp_dict = {}
    for index, num in enumerate(nums):
        temp_dict[num] = index
    for index, value in enumerate(nums):
        frac = target - value

        if frac in temp_dict.keys() and index != temp_dict[frac] :
            return [index, temp_dict[frac]]
    return None

def twoSum_improve_2(nums, target):
    temp_dict = {}
    for index, value in enumerate(nums):
        frac = target - value

        if frac in temp_dict.keys() :
            return [index, temp_dict[frac]]
        temp_dict[value] = index



if __name__ == '__main__':
    nums = [2,5,5,15]
    target = 10

    print(twoSum_improve_2(nums, target))
