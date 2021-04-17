import pytest
# @pytest.fixture(autouse="true")
@pytest.fixture(params=["参数1","参数2"])


def myfixture(reqeuest):
    print("执行myfixture.带参数%s"%request.param)
