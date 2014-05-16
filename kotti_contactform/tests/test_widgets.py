from deform.tests.test_widget import DummyField
from deform.tests.test_widget import DummyRenderer
from deform.tests.test_widget import DummySchema
from mock import patch
import pytest


class TestRecaptchaWidget:

    def _makeOne(self, **kw):
        from kotti_contactform.widgets import RecaptchaWidget
        return RecaptchaWidget(**kw)

    def test_serialize_null(self):
        from colander import null
        widget = self._makeOne()
        renderer = DummyRenderer()
        field = DummyField(None, renderer=renderer)
        with patch('kotti_settings.util.get_setting') as setting:
            setting.return_value = ''
            widget.serialize(field, null)
            assert renderer.template is widget.template
            assert renderer.kw['field'] is field
            assert renderer.kw['cstruct'] == ''

    def test_serialize_None(self):
        widget = self._makeOne()
        renderer = DummyRenderer()
        field = DummyField(None, renderer=renderer)

        with patch('kotti_settings.util.get_setting') as setting:
            setting.return_value = ''
            widget.serialize(field, None)
            assert renderer.template is widget.template
            assert renderer.kw['field'] is field
            assert renderer.kw['cstruct'] == ''

    def test_serialize_pubkey(self):
        widget = self._makeOne()
        renderer = DummyRenderer()
        schema = DummySchema()
        field = DummyField(schema, renderer=renderer)
        cstruct = 'yo'

        with patch('kotti_settings.util.get_setting') as setting:
            setting.return_value = 'pubkey'
            widget.serialize(field, cstruct)
            assert renderer.template is widget.template
            assert renderer.kw['field'] is field
            assert renderer.kw['cstruct'] == cstruct
            assert renderer.kw['public_key'] == 'pubkey'

    def test_deserialize_null(self):
        from colander import null
        widget = self._makeOne()
        renderer = DummyRenderer()
        schema = DummySchema()
        field = DummyField(schema, renderer=renderer)
        pstruct = null
        with patch('kotti_settings.util.get_setting') as setting:
            setting.return_value = ''
            assert widget.deserialize(field, pstruct) is null

    def test_deserialize_no_response(self):
        from colander import null
        from colander import Invalid
        widget = self._makeOne()
        renderer = DummyRenderer()
        schema = DummySchema()
        field = DummyField(schema, renderer=renderer)
        pstruct = {'recaptcha_challenge_field': 'foo',
                   'recaptcha_response_field': ''}
        with patch('kotti_settings.util.get_setting') as setting:
            setting.return_value = ''
            with pytest.raises(Invalid):
                widget.deserialize(field, pstruct)

    def test_deserialize_no_challenge(self):
        from colander import null
        from colander import Invalid
        widget = self._makeOne()
        renderer = DummyRenderer()
        schema = DummySchema()
        field = DummyField(schema, renderer=renderer)
        pstruct = {'recaptcha_challenge_field': '',
                   'recaptcha_response_field': 'foo'}
        with patch('kotti_settings.util.get_setting') as setting:
            setting.return_value = ''
            with pytest.raises(Invalid):
                widget.deserialize(field, pstruct)

    def test_deserialize_invalid(self):
        from colander import Invalid
        from kotti.testing import DummyRequest
        request = DummyRequest()
        request.remote_addr = 'http://localhost'
        widget = self._makeOne(request=request)
        renderer = DummyRenderer()
        schema = DummySchema()
        field = DummyField(schema, renderer=renderer)
        pstruct = {'recaptcha_challenge_field': 'foo',
                   'recaptcha_response_field': 'foo'}
        with patch('kotti_settings.util.get_setting') as setting:
            setting.return_value = ''
            with pytest.raises(Invalid):
                widget.deserialize(field, pstruct)
