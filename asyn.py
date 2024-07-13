import asyncio


async def main():
   await greeting('Jessica')
   await greeting('Jussali')




async def main2():
    task1 = asyncio.create_task(sayAfter(1,'first message having delay of 1s'))
    task2 = asyncio.create_task(sayAfter(3,'Second message having delay of 3s'))
    task3 = asyncio.create_task(greeting('Jessica'))
    task4 = asyncio.create_task(greeting('Novel'))
    # asyncio.gather()
    await task1
    await task2
    print('\n\nTasks created')  # Corrected the typo in the print statement
    await task3
    await task4

#creating multipe corrotine

#first corotine    
async def sayAfter(delay,message):
    await asyncio.sleep(delay)
    print(f'\n=====say-after====== {message}')

#second function 
async  def greeting(name):
    print(f'Hey {name}')
    await asyncio.sleep(3)
    print(f'Im leaving {name}')

"""
using main2 to await multple tasks 

"""
# asyncio.run(main())

"""
Now instead of using main to run and await multiple task , we'll use even loop to attach some tasks 

"""
loop = asyncio.get_event_loop()
loop.run_until_complete(main2())
loop.close()
