# -*- coding: utf-8 -*-
from general import General
from mock import Mock
from mock import patch

g = General()
print g.hello('jesse')
print g.bye()

mock = Mock()
mock.method(1, 3, 4, name="fred")
mock.method.assert_called_with(1, 3, 4, name="fred")

mock.test(1,2)
mock.test.assert_called_once_with(1,2)

mock.reset_mock()
print mock.called

with patch.object('General', return_value=None) as g:
    with patch('g.hello', return_value="Dog") as hello:
        parent.attach_mock(hello, 'hello')
        print hello()

#