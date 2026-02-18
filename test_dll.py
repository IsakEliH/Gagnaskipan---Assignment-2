# test_lists_verbose.py
# Verbose tester for BOTH SLList and DLList.
# Works even if pop_front/pop_back do NOT return the removed item.

from dll import DLList, Position
from sll import SLList


SHOW_INTERNALS = True  # extra head/tail or sentinels prints


def banner(title: str):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def snapshot(lst, label: str = ""):
    if label:
        print(f"\n--- {label} ---")

    py = [x for x in lst]
    print(f"type      : {type(lst).__name__}")
    print(f"str(lst)  : {str(lst)}")
    print(f"list(lst) : {py}")
    print(f"len(lst)  : {len(lst)}")
    print(f"is_empty  : {lst.is_empty()}")

    if SHOW_INTERNALS:
        # DLL internals
        if hasattr(lst, "sentinel_front") and hasattr(lst, "sentinel_back"):
            sf = lst.sentinel_front
            sb = lst.sentinel_back
            print(
                "internals : "
                f"SF.next={'SENTINEL_BACK' if sf.next is sb else getattr(sf.next, 'item', None)}, "
                f"SB.prev={'SENTINEL_FRONT' if sb.prev is sf else getattr(sb.prev, 'item', None)}"
            )
        # SLL internals
        elif hasattr(lst, "_head") and hasattr(lst, "_tail"):
            head_item = None if lst._head is None else lst._head.item
            tail_item = None if lst._tail is None else lst._tail.item
            print(f"internals : head={head_item}, tail={tail_item}")


def assert_raises(exc_type, fn, *args, **kwargs):
    try:
        fn(*args, **kwargs)
    except exc_type:
        print(f"✅ Raised expected {exc_type.__name__}")
        return
    except Exception as e:
        raise AssertionError(
            f"Expected {exc_type.__name__}, got {type(e).__name__}: {e}"
        )
    raise AssertionError(f"Expected {exc_type.__name__}, but no exception was raised")


# ---------- Unified operations (work for both lists) ----------


def push_front_any(lst, item):
    print(f"OP: {type(lst).__name__}.push_front({item})")
    lst.push_front(item)
    snapshot(lst, "after push_front")


def push_back_any(lst, item):
    print(f"OP: {type(lst).__name__}.push_back({item})")
    lst.push_back(item)
    snapshot(lst, "after push_back")


def pop_front_any(lst):
    """
    Does NOT assume pop_front returns anything.
    Verifies state change instead.
    """
    before = [x for x in lst]
    print(f"OP: {type(lst).__name__}.pop_front()")
    rv = lst.pop_front()
    print(f"  returned: {rv}")
    after = [x for x in lst]
    snapshot(lst, "after pop_front")
    return before, after, rv


def pop_back_any(lst):
    """
    Does NOT assume pop_back returns anything.
    Verifies state change instead.
    """
    before = [x for x in lst]
    print(f"OP: {type(lst).__name__}.pop_back()")
    rv = lst.pop_back()
    print(f"  returned: {rv}")
    after = [x for x in lst]
    snapshot(lst, "after pop_back")
    return before, after, rv


# ---------- DLL-only helpers ----------


def dll_append(dll: DLList, item):
    print(f"OP: DLList append via sentinel_back, insert_before({item})")
    dll.insert_before(Position(dll.sentinel_back), item)
    snapshot(dll, f"after dll_append {item}")


def dll_prepend(dll: DLList, item):
    print(f"OP: DLList prepend via sentinel_front, insert_after({item})")
    dll.insert_after(Position(dll.sentinel_front), item)
    snapshot(dll, f"after dll_prepend {item}")


# ---------- Tests that apply to BOTH SLL and DLL ----------


def test_empty_basics(lst):
    banner(f"{type(lst).__name__}: test_empty_basics")
    snapshot(lst, "initial")
    assert lst.is_empty() is True
    assert len(lst) == 0
    assert str(lst) == "[]"
    assert [x for x in lst] == []


def test_empty_raises(lst):
    banner(f"{type(lst).__name__}: test_empty_raises")
    snapshot(lst, "initial")
    print("OP: front()")
    assert_raises(IndexError, lst.front)
    print("OP: back()")
    assert_raises(IndexError, lst.back)
    print("OP: pop_front()")
    assert_raises(IndexError, lst.pop_front)
    print("OP: pop_back()")
    assert_raises(IndexError, lst.pop_back)


def test_push_back_order(lst):
    banner(f"{type(lst).__name__}: test_push_back_order")
    snapshot(lst, "initial")
    push_back_any(lst, 1)
    push_back_any(lst, 2)
    push_back_any(lst, 3)
    assert [x for x in lst] == [1, 2, 3]
    assert lst.front() == 1
    assert lst.back() == 3


def test_push_front_order(lst):
    banner(f"{type(lst).__name__}: test_push_front_order")
    snapshot(lst, "initial")
    push_front_any(lst, 1)
    push_front_any(lst, 2)
    push_front_any(lst, 3)
    assert [x for x in lst] == [3, 2, 1]
    assert lst.front() == 3
    assert lst.back() == 1


def test_mixed_pushes(lst):
    banner(f"{type(lst).__name__}: test_mixed_pushes")
    snapshot(lst, "initial")
    push_back_any(lst, 2)  # [2]
    push_front_any(lst, 1)  # [1,2]
    push_back_any(lst, 3)  # [1,2,3]
    push_front_any(lst, 0)  # [0,1,2,3]
    assert [x for x in lst] == [0, 1, 2, 3]
    assert str(lst) == "[0, 1, 2, 3]"


def test_pop_front_and_back_no_return_assumed(lst):
    banner(f"{type(lst).__name__}: test_pop_front_and_back_no_return_assumed")
    snapshot(lst, "initial")

    # Build [1,2,3]
    push_back_any(lst, 1)
    push_back_any(lst, 2)
    push_back_any(lst, 3)

    before, after, _ = pop_front_any(lst)
    assert before == [1, 2, 3]
    assert after == [2, 3]

    before, after, _ = pop_back_any(lst)
    assert before == [2, 3]
    assert after == [2]

    before, after, _ = pop_front_any(lst)
    assert before == [2]
    assert after == []
    assert lst.is_empty() is True
    assert str(lst) == "[]"


def test_pop_until_empty_then_reuse(lst):
    banner(f"{type(lst).__name__}: test_pop_until_empty_then_reuse")
    snapshot(lst, "initial")

    for i in range(5):
        push_back_any(lst, i)

    while not lst.is_empty():
        before = [x for x in lst]
        pop_front_any(lst)
        after = [x for x in lst]
        assert after == before[1:]

    assert [x for x in lst] == []
    push_back_any(lst, 99)
    assert [x for x in lst] == [99]


def test_iteration_matches_len(lst):
    banner(f"{type(lst).__name__}: test_iteration_matches_len")
    snapshot(lst, "initial")

    for i in range(1, 11):
        push_back_any(lst, i)

    py = [x for x in lst]
    print("Final list:", py)
    assert len(lst) == 10
    assert len(py) == 10
    assert py == list(range(1, 11))


# ---------- DLL-only tests ----------


def test_dll_positions_and_insert_remove_replace():
    dll = DLList()
    banner("DLList: test_positions_and_insert_remove_replace")
    snapshot(dll, "initial")

    # Build [1, 3]
    dll_append(dll, 1)
    dll_append(dll, 3)

    p3 = dll.back_pos()
    assert p3 is not None

    print("OP: insert_before(back_pos, 2)")
    p2 = dll.insert_before(p3, 2)
    snapshot(dll, "after insert_before 2")
    assert [x for x in dll] == [1, 2, 3]
    assert dll.get_at(p2) == 2

    p1 = dll.front_pos()
    assert p1 is not None

    print("OP: insert_after(front_pos, 1.5)")
    p15 = dll.insert_after(p1, 1.5)
    snapshot(dll, "after insert_after 1.5")
    assert [x for x in dll] == [1, 1.5, 2, 3]
    assert dll.get_at(p15) == 1.5

    print("OP: replace(p2, 'B')")
    old = dll.replace(p2, "B")
    print(f"  returned old: {old}")
    snapshot(dll, "after replace")
    assert old == 2
    assert [x for x in dll] == [1, 1.5, "B", 3]

    print("OP: remove(p15)")
    removed = dll.remove(p15)
    print(f"  returned removed: {removed}")
    snapshot(dll, "after remove")
    assert removed == 1.5
    assert [x for x in dll] == [1, "B", 3]


def test_dll_prev_next_positions():
    dll = DLList()
    banner("DLList: test_prev_next_positions")
    snapshot(dll, "initial")

    for v in [10, 20, 30]:
        dll_append(dll, v)

    fp = dll.front_pos()
    assert fp is not None

    print("OP: next_pos(front_pos)")
    np = dll.next_pos(fp)
    assert np is not None
    print("  next_pos item:", dll.get_at(np))
    assert dll.get_at(np) == 20

    print("OP: prev_pos(next_pos)")
    pp = dll.prev_pos(np)
    assert pp is not None
    print("  prev_pos item:", dll.get_at(pp))
    assert dll.get_at(pp) == 10


# ---------- Runner ----------


def run_suite_for_list(factory, name: str):
    lst = factory()
    test_empty_basics(lst)

    lst = factory()
    test_empty_raises(lst)

    lst = factory()
    test_push_back_order(lst)

    lst = factory()
    test_push_front_order(lst)

    lst = factory()
    test_mixed_pushes(lst)

    lst = factory()
    test_pop_front_and_back_no_return_assumed(lst)

    lst = factory()
    test_pop_until_empty_then_reuse(lst)

    lst = factory()
    test_iteration_matches_len(lst)

    print(f"\n✅ {name}: common suite passed")


def run_all():
    # Common suite for both
    run_suite_for_list(SLList, "SLList")
    run_suite_for_list(DLList, "DLList")

    # DLL-only extras
    test_dll_positions_and_insert_remove_replace()
    print("\n✅ DLList: positions/insert/remove/replace passed")

    test_dll_prev_next_positions()
    print("\n✅ DLList: prev/next passed")

    print("\nOK, all tests passed")


if __name__ == "__main__":
    run_all()
