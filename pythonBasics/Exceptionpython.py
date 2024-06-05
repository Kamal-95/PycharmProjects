# Itemsincart = 0
#
# if Itemsincart != 2:
#     raise Exception("Product Card count not matching")


# Itemsincart = 0
#
# if Itemsincart != 0:
#     raise Exception("Product Card count not matching")

# Itemsincart = 0
#
# if Itemsincart != 2:
#     assert(Itemsincart == 2)

# Itemsincart = 0
#
# if Itemsincart != 2:
#     assert(Itemsincart == 0)



# try:
#     with open("testlog.text","r") as readerfile:
#         print(readerfile.read())
# except:
#     print("I reached this block because of failure")

# try:
#     with open("test.text","r") as readerfile:
#         print(readerfile.read())
# except:
#     print("I reached this block because of failure")

try:
    with open("testlog.text", "r") as readerfile:
        print(readerfile.read())

except Exception as e:
    print(e)

finally:
    print("cleaning Up records")











