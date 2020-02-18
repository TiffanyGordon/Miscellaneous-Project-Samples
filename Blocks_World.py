#Blocks World state

from collections import deque

'''The table will have 3 open slots and each slot can hold up to 3 blocks.
In an effort to better control the in/out flow, I have chosen a deque to comprise each
tower.  With the availability of pop and append for deque objects, this will prevent
the erroneous movement of blocks that are not at the top of a stack and will ensure
that blocks are added to the top of a stack when moved to a new position.'''

class blocks_world_state:
    def state_description():
        stack1 = deque([], maxlen=3)
        stack2 = deque([], maxlen=3)
        stack3 = deque([], maxlen=3)
        table = [stack1, stack2, stack3]
        return table

    # user will input start state
    def start_state():
        start = input("Please input start state in the following format: [x, x, x]")
        return blocks_world_state(start)

    #user will input goal state
    def goal_state():
        goal = input("Please input goal state in the following format: [xxx]")
        return blocks_world_state(goal)

    def is_empty(item):
        if item:
            return False
        else:
            return True

    #this will take one of the stacks as its parameter and check if there is room for more blocks
    def full(item):
        if len(item) == 3:
            return True
        else:
            return False

    def is_top(item):
        if (item.index(len(item))) == null:
            return True
        else:
            return False

    def move(item, cur_loc, next_loc):
        if is_top(item) and not full(next_loc):
            next_loc.append(item)
            cur_loc.pop()
        else:
            print('attempted invalid move')
        return cur_loc, next_loc

    '''Ideally, successors would look at the index of the current item,
    check the length of the deque(s) next to it, and add the index of the empty
    slot to the list of neighbors. I am stuck on how to differentiate the index of the
    deque from the index of items/slots within the deque.'''

    def successors(self):
        successor_states = []
        neighbors = {}

        return successor_states
