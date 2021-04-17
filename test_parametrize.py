import pytest
def add_function(a,b):
    return a+b

def test1_add1():
    assert add_function(1,1)==2
def test1_add2():
    assert add_function(1,-1)==0
def test1_add3():
    assert add_function(1,-1)==-2
def test1_add4():
    assert add_function(1000,10000)==2

# 参数化，参数加别名，ids
@pytest.mark.parametrize("a,b,expected",
                        [(3,5,8),
                        (-1,-3,-4),
                        (10000,1000,11000),
                        ],ids=["int","minus","bigint"])
def test_add(a,b,expected):
    assert add_function(a,b) == expected


# 参数排列组合
@pytest.mark.parametrize("a",[0,0,200])
@pytest.mark.parametrize("b",[-2,10000,123])
def test_foo(a,b):
    print("测试数据组合：a->%s,b->%s"%(a,b))
