# Source: https://www.codewars.com/kata/55b42574ff091733d900002f
# Make a program that filters a list of strings and returns a list with only your friends name in it.
#
# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
#
# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
#
# i.e.
#
# friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
# Note: keep the original order of the names in the output.

def friend(x):
    friend_list = []
    for name in x:
        if len(name) == 4:
            friend_list.append(name)
    print(friend_list)
    return friend_list


# test cases
friend(["Ryan", "Kieran", "Mark",]) # => ["Ryan", "Mark"])
friend(["Ryan", "Jimmy", "abc", "d", "Cool Man"]) # => ["Ryan"])
friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]) # => ["Jimm", "Cari", "aret"])
