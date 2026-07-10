counter = 0

def increment():
    global counter
    counter = counter + 1
    return counter

print(increment())
print(increment())


def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("apple"))
print(add_item("banana"))
print(add_item("cherry"))


def add_item_fixed(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart
    

print(add_item_fixed("apple", cart=None))
print(add_item_fixed("banana"))
print(add_item_fixed("cherry"))
print(add_item_fixed("x"))
print(add_item_fixed("y"))


def describe(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)


describe("Rahul", 25, "Bengaluru", role="analyst", years_exp=3)

'''
Its a design decision to have named positional arguments firts followed by variable positional arguments
followed by keyword arguments, *args is between named positional and keyword arguments to enforce a keyword argument
to prevent calles passing arguments positionally and getting confused about the order

sorted(iterable, *, key=None, reverse=False) — that lone * in sorted's actual signature exists purely to force key and reverse to be keyword-only, so nobody accidentally calls sorted(mylist, str.lower, True) and has to remember argument order.

*args is always greedy and consumes all the positional arguments at once and only having a keyword arguments tells it where to stop
python refuses positional mapping after *args and always expects a keyword argument
'''
def describe(name, *args, **kwargs):
    print(args)
    print(name)
    print(kwargs)


describe("Rahul", 25, "Bengaluru", role="analyst", years_exp=3)

# describe("Rahul", 25)
# describe("Rahul", 25, "Bengaluru", name="Rahul")  # this would work now, awkwardly