from mock import *  # NOQA
from nose.tools import *  # NOQA

from method_override.templatetags.method_override import method_override


class TestTemplateTags(object):
    def test_method_override(self):
        result = method_override('PUT')
        assert_equal(
            result, '<input type="hidden" name="_method" value="PUT">'
        )
