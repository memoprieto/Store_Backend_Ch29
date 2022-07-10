def run_test():
    print("Test 1 - dictionaries")

    me={
        "first": "Guillermo",
        "last": "Prieto",
        "age": 42,
        "hobbies": [],
    }

    #print(me)

    #print(me["first"])
    
    # print full name (first last)
    print(me["first"]+ " " + me["last"])

    # change values
    me["age"] = me["age"] + 1
    me["age"] = 99

    # add new keys
    me["preferred_color"]="Gray"
    print(me)

    # read if exist
    if "middle_name" in me: # checks for existence
        print(me["middle_name"])

    # print the full address on a single line
    # evergreen 123, spring, CA, 812321
    address = me
    

run_test()