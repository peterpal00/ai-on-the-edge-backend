import pytest


@pytest.fixture
def test_first_name():
    return "test_first_name"


@pytest.fixture
def test_last_name():
    return "test_last_name"


@pytest.fixture
def test_birth_date():
    return "test_birth_date"


@pytest.fixture
def test_email_address():
    return "test_email_address"


@pytest.fixture
def test_timestamp():
    return "test_timestamp_01234"


@pytest.fixture
def test_uuid4_str():
    return "test_uuid4_01234"


@pytest.fixture
def test_registration_code():
    return "test_reg_code_01234"
