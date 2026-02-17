# test_dll.py
from dll import DLList, Position
from dll_node import Node


def assert_raises(exc_type, fn, *args, **kwargs):
    try:
        fn(*args, **kwargs)
    except exc_type:
        return
    except Exception as e:
        raise AssertionError(f"Expected {exc_type.__name__}, got {type(e).__name__}: {e}")
    raise AssertionError(f"Expected {exc_type.__name__}, but no exception was raised")


def append_using_positions(dll: DLList, item):
    """
    Append without using push_back/front, so this test helper does not depend
    on your _get_endpoint() logic.
    """
    if dll.is_empty():
        return dll.insert_after(Position(Node(None)), item)  # dummy Position ok on empty
    return dll.insert_after(dll.back_pos(), item)


def prepend_using_positions(dll: DLList, item):
    if dll.is_empty():
        return dll.insert_before(Position(Node(None)), item)
    return dll.insert_before(dll.front_pos(), item)


def to_pylist(dll: DLList):
    return [x for x in dll]


def test_empty_list_basics():
    dll = DLList()
    assert dll.is_empty() is True
    assert len(dll) == 0
    assert str(dll) == "[]"
    assert to_pylist(dll) == []
    assert dll.front_pos() is None
    assert dll.back_pos() is None


def test_empty_list_raises():
    dll = DLList()
    assert_raises(IndexError, dll.front)
    assert_raises(IndexError, dll.back)
    assert_raises(IndexError, dll.pop_front)
    assert_raises(IndexError, dll.pop_back)


def test_append_order_without_push_methods():
    dll = DLList()
    append_using_positions(dll, 1)
    append_using_positions(dll, 2)
    append_using_positions(dll, 3)
    assert len(dll) == 3
    assert to_pylist(dll) == [1, 2, 3]
    assert dll.front() == 1
    assert dll.back() == 3
    assert str(dll) == "[1, 2, 3]"


def test_prepend_order_without_push_methods():
    dll = DLList()
    prepend_using_positions(dll, 1)
    prepend_using_positions(dll, 2)
    prepend_using_positions(dll, 3)
    assert to_pylist(dll) == [3, 2, 1]
    assert dll.front() == 3
    assert dll.back() == 1
    assert str(dll) == "[3, 2, 1]"


def test_push_back_order():
    dll = DLList()
    dll.push_back(1)
    dll.push_back(2)
    dll.push_back(3)
    assert to_pylist(dll) == [1, 2, 3]  # this will catch endpoint bugs
    assert dll.front() == 1
    assert dll.back() == 3


def test_push_front_order():
    dll = DLList()
    dll.push_front(1)
    dll.push_front(2)
    dll.push_front(3)
    assert to_pylist(dll) == [3, 2, 1]
    assert dll.front() == 3
    assert dll.back() == 1


def test_pop_front_and_back():
    dll = DLList()
    append_using_positions(dll, 1)
    append_using_positions(dll, 2)
    append_using_positions(dll, 3)

    assert dll.pop_front() == 1
    assert to_pylist(dll) == [2, 3]

    assert dll.pop_back() == 3
    assert to_pylist(dll) == [2]

    assert dll.pop_front() == 2
    assert to_pylist(dll) == []
    assert dll.is_empty() is True
    assert str(dll) == "[]"


def test_insert_before_and_after_middle():
    dll = DLList()
    p1 = append_using_positions(dll, 1)
    p3 = append_using_positions(dll, 3)

    # insert 2 before 3
    p2 = dll.insert_before(p3, 2)
    assert to_pylist(dll) == [1, 2, 3]
    assert dll.get_at(p2) == 2

    # insert 1.5 after 1
    p15 = dll.insert_after(p1, 1.5)
    assert to_pylist(dll) == [1, 1.5, 2, 3]
    assert dll.get_at(p15) == 1.5


def test_remove_middle():
    dll = DLList()
    append_using_positions(dll, 1)
    p2 = append_using_positions(dll, 2)
    append_using_positions(dll, 3)

    removed = dll.remove(p2)
    assert removed == 2
    assert to_pylist(dll) == [1, 3]
    assert len(dll) == 2


def test_replace():
    dll = DLList()
    append_using_positions(dll, "a")
    p = append_using_positions(dll, "b")
    append_using_positions(dll, "c")

    old = dll.replace(p, "B")
    assert old == "b"
    assert to_pylist(dll) == ["a", "B", "c"]


def test_positions_front_back():
    dll = DLList()
    append_using_positions(dll, 10)
    append_using_positions(dll, 20)
    append_using_positions(dll, 30)

    fp = dll.front_pos()
    bp = dll.back_pos()

    assert fp is not None and bp is not None
    assert dll.get_at(fp) == 10
    assert dll.get_at(bp) == 30


def test_prev_next_positions_types_and_values():
    dll = DLList()
    append_using_positions(dll, 1)
    append_using_positions(dll, 2)
    append_using_positions(dll, 3)

    fp = dll.front_pos()
    assert fp is not None

    np = dll.next_pos(fp)
    # should be a Position, not a Node
    assert np is None or isinstance(np, Position)
    if np is not None:
        assert dll.get_at(np) == 2
        pp = dll.prev_pos(np)
        assert pp is None or isinstance(pp, Position)
        if pp is not None:
            assert dll.get_at(pp) == 1


def test_str_formatting_no_trailing_comma():
    dll = DLList()
    append_using_positions(dll, 1)
    assert str(dll) == "[1]"
    append_using_positions(dll, 2)
    assert str(dll) == "[1, 2]"


def test_iteration_matches_len():
    dll = DLList()
    for i in range(1, 11):
        append_using_positions(dll, i)
    assert len(dll) == 10
    assert len(to_pylist(dll)) == 10
    assert to_pylist(dll) == list(range(1, 11))


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
        test_prev_next_positions_types_and_values,
        test_str_formatting_no_trailing_comma,
        test_iteration_matches_len,
    ]

    for t in tests:
        t()
    print(f"OK, {len(tests)} tests passed")


if __name__ == "__main__":
    run_all()
