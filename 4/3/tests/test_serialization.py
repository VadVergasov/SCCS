from constants import *
from serializer.serializer import Serializer, Deserializer


def test_primitive_1():
    assert a == Deserializer.deserialize(Serializer.serialize(a))


def test_primitive_2():
    assert aa == Deserializer.deserialize(Serializer.serialize(aa))


def test_primitive_3():
    assert b == Deserializer.deserialize(Serializer.serialize(b))


def test_primitive_4():
    assert bb == Deserializer.deserialize(Serializer.serialize(bb))


def test_primitive_5():
    assert c == Deserializer.deserialize(Serializer.serialize(c))


def test_primitive_6():
    assert cc == Deserializer.deserialize(Serializer.serialize(cc))


def test_primitive_7():
    assert d == Deserializer.deserialize(Serializer.serialize(d))


def test_primitive_8():
    assert dd == Deserializer.deserialize(Serializer.serialize(dd))


def test_primitive_9():
    assert e == Deserializer.deserialize(Serializer.serialize(e))


def test_primitive_10():
    assert f == Deserializer.deserialize(Serializer.serialize(f))


def test_collection_1():
    assert list1 == Deserializer.deserialize(Serializer.serialize(list1))


def test_collection_2():
    assert list2 == Deserializer.deserialize(Serializer.serialize(list2))


def test_collection_3():
    assert list3 == Deserializer.deserialize(Serializer.serialize(list3))


def test_collection_4():
    assert tuple1 == Deserializer.deserialize(Serializer.serialize(tuple1))


def test_collection_4():
    assert tuple2 == Deserializer.deserialize(Serializer.serialize(tuple2))


def test_collection_6():
    assert tuple3 == Deserializer.deserialize(Serializer.serialize(tuple3))


def test_collection_7():
    assert bytes1 == Deserializer.deserialize(Serializer.serialize(bytes1))


def test_collection_8():
    assert dict1 == Deserializer.deserialize(Serializer.serialize(dict1))


def test_collection_9():
    assert dict2 == Deserializer.deserialize(Serializer.serialize(dict2))


def test_collection_10():
    assert dict3 == Deserializer.deserialize(Serializer.serialize(dict3))


def test_collection_11():
    assert dict4 == Deserializer.deserialize(Serializer.serialize(dict4))


def test_collection_12():
    assert dict5 == Deserializer.deserialize(Serializer.serialize(dict5))


def test_func_1():
    assert func1() == Deserializer.deserialize(Serializer.serialize(func1))()


def test_func_2():
    assert func2(12) == Deserializer.deserialize(Serializer.serialize(func2))(12)


def test_func_3():
    assert func3(12) == Deserializer.deserialize(Serializer.serialize(func3))(12)


def test_func_4():
    assert func3(12, 12, 12, 12, 12) == Deserializer.deserialize(Serializer.serialize(func3))(12, 12, 12, 12, 12)


def test_func_5():
    assert func4(0.5) == Deserializer.deserialize(Serializer.serialize(func4))(0.5)


def test_func_6():
    assert func5([4, 3, 2, 1]) == Deserializer.deserialize(Serializer.serialize(func5))([4, 3, 2, 1])


def test_func_7():
    assert func6(5) == Deserializer.deserialize(Serializer.serialize(func6))(5)


def test_func_8():
    assert func7(5) == Deserializer.deserialize(Serializer.serialize(func7))(5)


def test_func_9():
    tmp = Deserializer.deserialize(Serializer.serialize(lambda1))

    assert tmp(5) == lambda1(5)


def test_func_10():
    tmp = Deserializer.deserialize(Serializer.serialize(lambda2))

    assert tmp(1, 2, 3) == lambda2(3, 2, 1)


def test_class_1():
    tmp = Deserializer.deserialize(Serializer.serialize(A))
    tmp = tmp()
    a = A()

    assert a.a == tmp.a
    assert a.qwe(2) == tmp.qwe(2)


def test_class_2():
    tmp = Deserializer.deserialize(Serializer.serialize(B))
    tmp = tmp(2)
    b = B(2)

    assert tmp.a == b.a
    assert tmp.func() == b.func()
    assert tmp.qwe(4) == b.qwe(4)


def test_class_3():
    tmp = Deserializer.deserialize(Serializer.serialize(EEEE))
    tmp = tmp()
    eeee = EEEE()

    assert tmp.e == eeee.e
    assert tmp.ee == eeee.ee
    assert tmp.eee == eeee.eee
    assert tmp.eeee == eeee.eeee


def test_class_4():
    tmp = Deserializer.deserialize(Serializer.serialize(first))
    f = tmp()

    tmp = Deserializer.deserialize(Serializer.serialize(second))
    s = tmp()
    so = second()

    assert s.func(4) == so.func(4)
    assert f.func(4) ** 4 == s.func(4)


def test_class_object_1():
    a = A()
    tmp = Deserializer.deserialize(Serializer.serialize(a))

    assert tmp.a == a.a
    assert tmp.qwe(4) == a.qwe(4)


def test_class_5():
    tmp = Deserializer.deserialize(Serializer.serialize(st))

    assert tmp.qwe() == st.qwe()


def test_class_6():
    tmp = Deserializer.deserialize(Serializer.serialize(HardClass))

    h = HardClass()
    tmp = tmp()

    assert tmp.a == h.a
    assert tmp.s == h.s
    assert tmp.func(1, 2) == h.func(1, 2)

    assert tmp.c == h.c
    assert tmp.func1(1, 2, 3, 4) == h.func1(1, 2, 3, 4)
    assert tmp.func2(5) == h.func2(5)


def test_multiple_inheritance():
    tmp = Deserializer.deserialize(Serializer.serialize(CCCC))
    c = CCCC()
    tmp = tmp()

    assert c.a == tmp.a
    assert c.b == tmp.b
    assert c.c == tmp.c


def test_decorator():
    tmp = Deserializer.deserialize(Serializer.serialize(raise_if_to_many_args))
    tmp = tmp(sum_func)

    f = raise_if_to_many_args(sum_func)

    assert f(1, 2, 3) == tmp(1, 2, 3)

def test_recursion():
    tmp = Deserializer.deserialize(Serializer.serialize(fact))

    assert 24 == tmp(4)

def test_lambda():
    tmp = Deserializer.deserialize(Serializer.serialize(lambda x: x**3))

    assert 27 == tmp(3)
