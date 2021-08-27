# Python3 program for demonstrating
# coroutine execution

def print_name(prefix):
    print("Searching prefix:{}".format(prefix))
    while True:
        name = (yield)
        print(f'processing: {name}')
        if prefix in name:
            print(f"\tfound: {name}")


# calling coroutine, nothing will happen
corou = print_name("Dear")

# This will start execution of coroutine and
# Prints first line "Searchig prefix..."
# and advance execution to the first yield expression
corou.__next__()


# sending inputs
corou.send("Atul")
corou.send("Dear Atul")

corou.close()
print(f'closed coroutine')