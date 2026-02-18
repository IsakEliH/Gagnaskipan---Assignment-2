# test_dll_verbose.py
from dll import DLList, Position
from dll_node import Node


# Toggle this if you want even more internal info
SHOW_SENTINELS = True


def banner(title: str):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def snapshot(dll: DLList, label: str = ""):
    """
    Print a compact state snapshot of the list.
    """
    if label:
        print(f"\n--- {label} ---")

    py = [x for x in dll]
    print(f"str(dll)  : {str(dll)}")
    print(f"list(dll) : {py}")
    print(f"len(dll)  : {len(dll)}")
    print(f"is_empty  : {dll.is_empty()}")

    if SHOW_SENTINELS:
        sf = dll.sentinel_front
        sb = dll.sentinel_back
        # Safe-ish prints without assuming Node has fancy __str__
        print("sentinels : "
              f"SF.next={'SENTINEL_BACK' if sf.next is sb else getattr(sf.next, 'item', None)}, "
              f"SB.prev={'SENTINEL_FRONT' if sb.prev is sf else getattr(sb.prev, 'item', None)}")


def assert_raises(exc_type, fn, *args, **kwargs):
    try:
        fn(*args, **kwargs)
    except exc_type:
        print(f"✅ Raised expected {exc_type.__name__}")
        return
    except Exception as e:
        raise AssertionError(f"Expected {exc_type.__name__}, got {type(e).__name__}: {e}")
    raise AssertionError(f"Expected {exc_type.__name__}, but no exception was raised")

def append_using_positions(dll: DLList, item):
    """
    Append without using _get_endpoint(). Uses sentinel_back when empty.
    """
    print(f"OP: append_using_positions({item})")

    if dll.is_empty():
        # append to back, easiest is insert_before(back sentinel)
        pos = dll.insert_before(Position(dll.sentinel_back), item)
    else:
        pos = dll.insert_after(dll.back_pos(), item)

    snapshot(dll, f"after append {item}")
    return pos


def prepend_using_positions(dll: DLList, item):
    """
    Prepend without using _get_endpoint(). Uses sentinel_front when empty.
    """
    print(f"OP: prepend_using_positions({item})")

    if dll.is_empty():
        # prepend to front, easiest is insert_after(front sentinel)
        pos = dll.insert_after(Position(dll.sentinel_front), item)
    else:
        pos = dll.insert_before(dll.front_pos(), item)

    snapshot(dll, f"after prepend {item}")
    return pos


def test_empty_list_basics():
    banner("test_empty_list_basics")
    dll = DLList()
    snapshot(dll, "initial")

    assert dll.is_empty() is True
    assert len(dll) == 0
    assert str(dll) == "[]"
    assert [x for x in dll] == []
    assert dll.front_pos() is None
    assert dll.back_pos() is None


def test_empty_list_raises():
    banner("test_empty_list_raises")
    dll = DLList()
    snapshot(dll, "initial")

    print("OP: dll.front()")
    assert_raises(IndexError, dll.front)

    print("OP: dll.back()")
    assert_raises(IndexError, dll.back)

    print("OP: dll.pop_front()")
    assert_raises(IndexError, dll.pop_front)

    print("OP: dll.pop_back()")
    assert_raises(IndexError, dll.pop_back)


def test_append_order_without_push_methods():
    banner("test_append_order_without_push_methods")
    dll = DLList()
    snapshot(dll, "initial")

    append_using_positions(dll, 1)
    append_using_positions(dll, 2)
    append_using_positions(dll, 3)

    assert len(dll) == 3
    assert [x for x in dll] == [1, 2, 3]

    print("OP: dll.front()")
    assert dll.front() == 1

    print("OP: dll.back()")
    assert dll.back() == 3

    assert str(dll) == "[1, 2, 3]"


def test_prepend_order_without_push_methods():
    banner("test_prepend_order_without_push_methods")
    dll = DLList()
    snapshot(dll, "initial")

    prepend_using_positions(dll, 1)
    prepend_using_positions(dll, 2)
    prepend_using_positions(dll, 3)

    assert [x for x in dll] == [3, 2, 1]
    assert dll.front() == 3
    assert dll.back() == 1
    assert str(dll) == "[3, 2, 1]"


def test_push_back_order():
    banner("test_push_back_order")
    dll = DLList()
    snapshot(dll, "initial")

    print("OP: dll.push_back(1)")
    dll.push_back(1)
    snapshot(dll, "after push_back 1")

    print("OP: dll.push_back(2)")
    dll.push_back(2)
    snapshot(dll, "after push_back 2")

    print("OP: dll.push_back(3)")
    dll.push_back(3)
    snapshot(dll, "after push_back 3")

    assert [x for x in dll] == [1, 2, 3]
    assert dll.front() == 1
    assert dll.back() == 3


def test_push_front_order():
    banner("test_push_front_order")
    dll = DLList()
    snapshot(dll, "initial")

    print("OP: dll.push_front(1)")
    dll.push_front(1)
    snapshot(dll, "after push_front 1")

    print("OP: dll.push_front(2)")
    dll.push_front(2)
    snapshot(dll, "after push_front 2")

    print("OP: dll.push_front(3)")
    dll.push_front(3)
    snapshot(dll, "after push_front 3")

    assert [x for x in dll] == [3, 2, 1]
    assert dll.front() == 3
    assert dll.back() == 1


def test_pop_front_and_back():
    banner("test_pop_front_and_back")
    dll = DLList()
    snapshot(dll, "initial")

    append_using_positions(dll, 1)
    append_using_positions(dll, 2)
    append_using_positions(dll, 3)

    print("OP: dll.pop_front()")
    v = dll.pop_front()
    print(f"  returned: {v}")
    snapshot(dll, "after pop_front")
    assert v == 1
    assert [x for x in dll] == [2, 3]

    print("OP: dll.pop_back()")
    v = dll.pop_back()
    print(f"  returned: {v}")
    snapshot(dll, "after pop_back")
    assert v == 3
    assert [x for x in dll] == [2]

    print("OP: dll.pop_front()")
    v = dll.pop_front()
    print(f"  returned: {v}")
    snapshot(dll, "after pop_front again")
    assert v == 2
    assert [x for x in dll] == []
    assert dll.is_empty() is True
    assert str(dll) == "[]"


def test_insert_before_and_after_middle():
    banner("test_insert_before_and_after_middle")
    dll = DLList()
    snapshot(dll, "initial")

    p1 = append_using_positions(dll, 1)
    p3 = append_using_positions(dll, 3)

    print("OP: insert_before(p3, 2)")
    p2 = dll.insert_before(p3, 2)
    snapshot(dll, "after insert_before 2")
    assert [x for x in dll] == [1, 2, 3]
    assert dll.get_at(p2) == 2

    print("OP: insert_after(p1, 1.5)")
    p15 = dll.insert_after(p1, 1.5)
    snapshot(dll, "after insert_after 1.5")
    assert [x for x in dll] == [1, 1.5, 2, 3]
    assert dll.get_at(p15) == 1.5


def test_remove_middle():
    banner("test_remove_middle")
    dll = DLList()
    snapshot(dll, "initial")

    append_using_positions(dll, 1)
    p2 = append_using_positions(dll, 2)
    append_using_positions(dll, 3)

    print("OP: remove(p2)")
    removed = dll.remove(p2)
    print(f"  returned: {removed}")
    snapshot(dll, "after remove middle")

    assert removed == 2
    assert [x for x in dll] == [1, 3]
    assert len(dll) == 2


def test_replace():
    banner("test_replace")
    dll = DLList()
    snapshot(dll, "initial")

    append_using_positions(dll, "a")
    p = append_using_positions(dll, "b")
    append_using_positions(dll, "c")

    print("OP: replace(p, 'B')")
    old = dll.replace(p, "B")
    print(f"  returned old: {old}")
    snapshot(dll, "after replace")

    assert old == "b"
    assert [x for x in dll] == ["a", "B", "c"]


def test_positions_front_back():
    banner("test_positions_front_back")
    dll = DLList()
    snapshot(dll, "initial")

    append_using_positions(dll, 10)
    append_using_positions(dll, 20)
    append_using_positions(dll, 30)

    fp = dll.front_pos()
    bp = dll.back_pos()
    assert fp is not None and bp is not None

    print(f"front_pos item: {dll.get_at(fp)}")
    print(f"back_pos item : {dll.get_at(bp)}")
    assert dll.get_at(fp) == 10
    assert dll.get_at(bp) == 30


def test_prev_next_positions_values():
    banner("test_prev_next_positions_values")
    dll = DLList()
    snapshot(dll, "initial")

    append_using_positions(dll, 1)
    append_using_positions(dll, 2)
    append_using_positions(dll, 3)

    fp = dll.front_pos()
    assert fp is not None

    print("OP: next_pos(front_pos)")
    np = dll.next_pos(fp)
    print(f"  next_pos item: {dll.get_at(np)}" if np is not None else "  next_pos is None")
    assert np is not None
    assert dll.get_at(np) == 2

    print("OP: prev_pos(next_pos)")
    pp = dll.prev_pos(np)
    print(f"  prev_pos item: {dll.get_at(pp)}" if pp is not None else "  prev_pos is None")
    assert pp is not None
    assert dll.get_at(pp) == 1


def test_str_formatting_no_trailing_comma():
    banner("test_str_formatting_no_trailing_comma")
    dll = DLList()
    snapshot(dll, "initial")

    append_using_positions(dll, 1)
    assert str(dll) == "[1]"

    append_using_positions(dll, 2)
    assert str(dll) == "[1, 2]"


def test_iteration_matches_len():
    banner("test_iteration_matches_len")
    dll = DLList()
    snapshot(dll, "initial")

    for i in range(1, 11):
        print(f"OP: append {i}")
        append_using_positions(dll, i)

    py = [x for x in dll]
    print("Final list:", py)

    assert len(dll) == 10
    assert len(py) == 10
    assert py == list(range(1, 11))


def run_all():
    tests = [
        test_empty_list_basics,
        test_empty_list_raises,
        test_append_order_without_push_methods,
        test_prepend_order_without_push_methods,
        test_push_back_order,
        test_push_front_order,
        test_pop_front_and_back,
        test_insert_before_and_after_middle,
        test_remove_middle,
        test_replace,
        test_positions_front_back,
        test_prev_next_positions_values,
        test_str_formatting_no_trailing_comma,
        test_iteration_matches_len,
    ]

    for t in tests:
        try:
            t()
            print("\n✅ PASS")
        except AssertionError as e:
            print("\n❌ FAIL:", e)
            raise  # stop immediately so you see the last printed state

    print(f"\nOK, {len(tests)} tests passed")


if __name__ == "__main__":
    run_all()
