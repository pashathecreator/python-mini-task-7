import pytest
from main import deprecated

def test_deprecated_with_both_parameters(capfd):
    @deprecated(since="1.0", will_be_removed="2.0")
    def func():
        return "Function result"

    result = func()
    captured = capfd.readouterr()  
    assert captured.out.strip() == "Warning: function func is deprecated since version 1.0. It will be removed in version 2.0"
    assert result == "Function result"

def test_deprecated_with_since_only(capfd):
    @deprecated(since="1.0")
    def func():
        return "Function result"

    result = func()
    captured = capfd.readouterr()  
    assert captured.out.strip() == "Warning: function func is deprecated since version 1.0. It will be removed in future versions."
    assert result == "Function result"

def test_deprecated_with_will_be_removed_only(capfd):
    @deprecated(will_be_removed="2.0")
    def func():
        return "Function result"

    result = func()
    captured = capfd.readouterr() 
    assert captured.out.strip() == "Warning: function func is deprecated. It will be removed in version 2.0"
    assert result == "Function result"

def test_deprecated_without_parameters(capfd):
    @deprecated
    def func():
        return "Function result"

    result = func()
    captured = capfd.readouterr()  
    assert captured.out.strip() == "Warning: function foo is deprecated. It will be removed in future versions."
    assert result == "Function result"