#
# Big test program to test the SLL, DLL (partially), Deque, Stack, and Queue implementations.
# The nice way to do that is to ensure my data structures behave the same as Python models.
#

from collections import deque  # Python's deque (reference model)

from dll import DLList  # My implementations
from sll import SLList
from deque import Deque
from stack import Stack
from queue import Queue

import random

random.seed(42)  # Fix the seed, such that result is reproducible.

# -------------------------- Small helpers --------------------------


def _fail(msg, i, model, obj):
    print("\nFAILED:", msg)
    print("step:", i)
    print("model:", model, "len:", len(model))
    try:
        print("obj  :", str(obj), "len:", len(obj), "empty:", obj.is_empty())
    except Exception as e:
        print("obj  : (error printing)", type(e).__name__, e)
    return False


def _deep_str_check(model_list, obj):
    # Compare string forms using list(model) formatting.
    # Assumes your __str__ prints like Python list: [a, b, c]
    return str(model_list) == str(obj)


# -------------------------- Deque tester --------------------------
# NOTE: pop() and popleft() in your Deque do NOT return the removed item.


def testing_deque(n, lst, check_every=250):
    d = deque()
    s = Deque(lst)

    ADD_PROB = 0.60
    REM_PROB = 0.55

    for i in range(n):
        do_deep = i % check_every == 0

        # Add
        if random.random() < ADD_PROB:
            elem = random.randrange(0, 1000)
            if random.random() < 0.5:
                d.append(elem)
                s.append(elem)
            else:
                d.appendleft(elem)
                s.appendleft(elem)

        # Remove (no return checking)
        if len(d) > 0 and random.random() < REM_PROB:
            if random.random() < 0.5:
                d.pop()
                s.pop()
            else:
                d.popleft()
                s.popleft()

        # Invariants
        if len(d) != len(s):
            print(list(d), str(s), len(d), len(s))
            return False

        if (len(d) == 0) != s.is_empty():
            return False

        if len(d) > 0:
            if d[0] != s.front():
                return False
            if d[-1] != s.back():
                return False

        if do_deep:
            if not _deep_str_check(list(d), s):
                print(str(list(d)), str(s))
                return False

    # Final deep check
    if not _deep_str_check(list(d), s):
        print(str(list(d)), str(s))
        return False

    return True


# -------------------------- Direct SLL/DLL tester --------------------------
# Tests SLList and DLList directly against Python list.
# NOTE: pop_front/pop_back do NOT return the removed item.


def testing_list_like(n, lst, check_every=250):
    model = []

    ADD_PROB = 0.60
    REM_PROB = 0.55

    for i in range(n):
        do_deep = i % check_every == 0

        # Add
        if random.random() < ADD_PROB:
            elem = random.randrange(0, 1000)
            if random.random() < 0.5:
                model.append(elem)
                lst.push_back(elem)
            else:
                model.insert(0, elem)
                lst.push_front(elem)

        # Remove (no return checking)
        if len(model) > 0 and random.random() < REM_PROB:
            if random.random() < 0.5:
                model.pop(0)
                lst.pop_front()
            else:
                model.pop()
                lst.pop_back()

        # Invariants
        if len(model) != len(lst):
            return _fail("length mismatch", i, model, lst)

        if (len(model) == 0) != lst.is_empty():
            return _fail("is_empty mismatch", i, model, lst)

        if len(model) > 0:
            if model[0] != lst.front():
                return _fail("front mismatch", i, model, lst)
            if model[-1] != lst.back():
                return _fail("back mismatch", i, model, lst)

        if do_deep:
            if not _deep_str_check(model, lst):
                return _fail("string mismatch", i, model, lst)

    if not _deep_str_check(model, lst):
        return _fail("final string mismatch", n, model, lst)

    return True


# -------------------------- Stack tester --------------------------
# Reference model is Python list used as a stack (top is at end).
# NOTE: pop in your Stack does NOT return the removed item.


def _stack_peek(stk):
    # Try common names, fall back to back()
    if hasattr(stk, "top"):
        return stk.top()
    if hasattr(stk, "peek"):
        return stk.peek()
    if hasattr(stk, "back"):
        return stk.back()
    # If none exist, raise to make it obvious
    raise AttributeError("Stack has no top/peek/back method")


def testing_stack(n, lst, check_every=250):
    model = []
    s = Stack(lst)

    ADD_PROB = 0.60
    REM_PROB = 0.55

    for i in range(n):
        do_deep = i % check_every == 0

        # Push
        if random.random() < ADD_PROB:
            elem = random.randrange(0, 1000)
            model.append(elem)
            s.push(elem)

        # Pop (no return checking)
        if len(model) > 0 and random.random() < REM_PROB:
            model.pop()
            s.pop()

        # Invariants
        if len(model) != len(s):
            return _fail("stack length mismatch", i, model, s)

        if (len(model) == 0) != s.is_empty():
            return _fail("stack is_empty mismatch", i, model, s)

        if len(model) > 0:
            if model[-1] != _stack_peek(s):
                return _fail("stack top mismatch", i, model, s)

        # Deep check (string), optional, depends on your __str__ choice
        if do_deep:
            if not _deep_str_check(model, s):
                return _fail("stack string mismatch", i, model, s)

    if not _deep_str_check(model, s):
        return _fail("final stack string mismatch", n, model, s)

    return True


# -------------------------- Queue tester --------------------------
# Reference model is Python deque (front is left).
# NOTE: dequeue in your Queue does NOT return the removed item.


def _queue_enqueue(q, x):
    if hasattr(q, "enqueue"):
        q.enqueue(x)
        return
    if hasattr(q, "push_back"):
        q.push_back(x)
        return
    raise AttributeError("Queue has no enqueue/push_back method")


def _queue_dequeue(q):
    if hasattr(q, "dequeue"):
        q.dequeue()
        return
    if hasattr(q, "pop_front"):
        q.pop_front()
        return
    raise AttributeError("Queue has no dequeue/pop_front method")


def testing_queue(n, lst, check_every=250):
    model = deque()
    q = Queue(lst)

    ADD_PROB = 0.60
    REM_PROB = 0.55

    for i in range(n):
        do_deep = i % check_every == 0

        # Enqueue
        if random.random() < ADD_PROB:
            elem = random.randrange(0, 1000)
            model.append(elem)
            _queue_enqueue(q, elem)

        # Dequeue (no return checking)
        if len(model) > 0 and random.random() < REM_PROB:
            model.popleft()
            _queue_dequeue(q)

        # Invariants
        if len(model) != len(q):
            return _fail("queue length mismatch", i, list(model), q)

        if (len(model) == 0) != q.is_empty():
            return _fail("queue is_empty mismatch", i, list(model), q)

        if len(model) > 0:
            if model[0] != q.front():
                return _fail("queue front mismatch", i, list(model), q)

        if do_deep:
            if not _deep_str_check(list(model), q):
                return _fail("queue string mismatch", i, list(model), q)

    if not _deep_str_check(list(model), q):
        return _fail("final queue string mismatch", n, list(model), q)

    return True


# -------------------------- Main --------------------------

if __name__ == "__main__":
    # Bigger numbers.
    # Note: If your SLL has O(n) pop_back, that can be slower, adjust if needed.
    N_LIST = 80000
    N_DEQUE = 200000
    N_STACK = 160000
    N_QUEUE = 160000

    CHECK_EVERY = 250

    print("\n--- Direct list-like tests ---")
    random.seed(42)
    print("SLList list-like:", testing_list_like(N_LIST, SLList(), CHECK_EVERY))
    random.seed(43)
    print("DLList list-like:", testing_list_like(N_LIST, DLList(), CHECK_EVERY))

    print("\n--- Deque tests using SLList and DLList internals ---")
    random.seed(44)
    print("Deque(SLList):", testing_deque(N_DEQUE, SLList(), CHECK_EVERY))
    random.seed(45)
    print("Deque(DLList):", testing_deque(N_DEQUE, DLList(), CHECK_EVERY))

    print("\n--- Stack tests using SLList and DLList internals ---")
    random.seed(46)
    print("Stack(SLList):", testing_stack(N_STACK, SLList(), CHECK_EVERY))
    random.seed(47)
    print("Stack(DLList):", testing_stack(N_STACK, DLList(), CHECK_EVERY))

    print("\n--- Queue tests using SLList and DLList internals ---")
    random.seed(48)
    print("Queue(SLList):", testing_queue(N_QUEUE, SLList(), CHECK_EVERY))
    random.seed(49)
    print("Queue(DLList):", testing_queue(N_QUEUE, DLList(), CHECK_EVERY))

    print("\n--- Extra stress rounds (different seeds) ---")
    for round_i in range(6):
        seed = 100 + round_i
        random.seed(seed)
        ok1 = testing_deque(80000, SLList(), 300)
        random.seed(seed + 1000)
        ok2 = testing_deque(80000, DLList(), 300)

        random.seed(seed + 2000)
        ok3 = testing_stack(60000, SLList(), 300)
        random.seed(seed + 3000)
        ok4 = testing_stack(60000, DLList(), 300)

        random.seed(seed + 4000)
        ok5 = testing_queue(60000, SLList(), 300)
        random.seed(seed + 5000)
        ok6 = testing_queue(60000, DLList(), 300)

        print("round", round_i, ":", ok1 and ok2 and ok3 and ok4 and ok5 and ok6)
