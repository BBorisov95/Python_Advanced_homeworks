from collections import deque

food_quantity = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

served = True

while orders:

    current_order = orders.popleft()

    if current_order <= food_quantity:
        food_quantity -= current_order
    else:
        served = False
        orders.appendleft(current_order)
        break


if not served:
    print(f'Orders left: {" ".join([str(x) for x in orders])}')
else:
    print('Orders complete')
