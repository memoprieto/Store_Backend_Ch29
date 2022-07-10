
def start_tests():
    print("----- List tests -----")

    nums = [1,2,3,4,5,6]

    # read from the list
    print( nums[0] )
    print( nums[1] )


    # add element to a list
    nums.append(9)
    print(nums)


    # for loop
    for n in nums:
        print(n)


    # for loop from 0 to 20
    for number in range(0,21):
        print(number)
    

def test1():
    print("test 1")

    prices = [123,3,23,6475,58,89,45,34,87,34,-12,23,123-23,-123,0,123,0-29,10]

    # 1 - print numbers lower than 50
    # 2 - count how many numbers are lower than 50
    # 3 - the sum of all numbers
    # 4 - the sum of all numbers greater than zero
    # 5 - count how many zeros there are

    count=0
    sum=0
    sum_non_zero=0
    zeros=0
    for n in prices:
        sum +=n

        if n>0:
            sum_non_zero +=n

        if n==0:
            zeros +=1

        if n<50:
            print(n)
            count +=1    

    print(f"There are {count} prices lower than $50")

def test2():
    print("--- TEST 2 ---")   

    users = users =  [
    {
        "gender": "F",
        "name": "Louis",
        "color": "Green"
    },
    {
        "gender": "M",
        "name": "Manuel",
        "color": "Gray"
    },
    {
        "gender": "F",
        "name": "Rossy",
        "color": "Pink"
    },
    {
        "gender": "F",
        "name": "Renny",
        "color": "pink"
    },
    {
        "gender": "M",
        "name": "Roman",
        "color": "Purple"
    },
    {
        "gender": "m",
        "name": "John",
        "color": "Pink"
    },
    {
        "gender": "F",
        "name": "Susan",
        "color": "Black"
    },
]


    # 1 - print all the names
    # 2 - print how many users there are in the list
    # 3 - print the name of users who likes pink or PINK or Pink or PiNK

    print(len(users))
    print(len("sergio"))

    for user in users:
        # get the name of user (dictionary)
        print(user["name"])

        # if the color of the user (in lower case) is equal to 'pink'
        # print the user´s name
    for user in users:
        if user["color"].lower()=="pink":
            print(user["name"])

def test3():
    print("--- TEST 3 ---")

    prices = [123,3,23,6475,58,89,45,34,87,34,-12,23, 123,-23,-123, 0, 123, 0, -29, 10]

    # find the most expensive product price
    # solution = prices[0]
    # for price in prices
    # if price is greater then your solution
    #    your solution is equal to price

    # outside the loop, prince the result

    solution = prices[0]
    for num in prices:
        if num>solution:
            solution=num
    
    print("The greatest number is " + str(solution))


start_tests()
test1()
test2()
test3()