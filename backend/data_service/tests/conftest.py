from pytest import fixture


@fixture
def test_value():
    return "521.17123"


@fixture
def test_raw():
    return "521.17345"


@fixture
def test_pre():
    return "521.17678"


@fixture
def test_error():
    return "test_error_message"


@fixture
def test_rate():
    return "0.023780"


@fixture
def test_timestamp():
    return "2023-01-13T16:00:42+0100"
