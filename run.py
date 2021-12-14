from unrealcv import client
import random
client.connect()  # Connect to the game
if not client.isconnected(
):  # Check if the connection is successfully established
    print(
        'UnrealCV server is not running. Run the game from http://unrealcv.github.io first.'
    )
else:
    import time
    st = time.time()
    count = 10
    results = client.request('vget /objects')
    print(results)
    for _ in range(count):
        results = client.request('vget /object/ThirdPersonCharacter_167,Wall7_4/state')
        print(f"results : {type(results)} {results}")
        # x, y, z = results.strip().split(' ')
        # x = float(x) * random.uniform(0.99, 1.01)
        # y = float(y) * random.uniform(0.99, 1.01)
        # z = float(z) * random.uniform(0.99, 1.01)
        # cmd = f'vset /object/ThirdPersonCharacter_167/location {x} {y} {z}'
        # filename = client.request(cmd)
    print(f"spent time {(time.time() - st)/count}")
    # print(filename)

