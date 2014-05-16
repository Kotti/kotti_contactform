# Thanks to Reed O'Brien: https://gist.github.com/reedobrien/701444
import httplib2
from urllib import urlencode

import colander
from colander import null
from colander import Invalid

from deform.widget import CheckedInputWidget


class RecaptchaWidget(CheckedInputWidget):
    template = 'recaptcha_widget'
    readonly_template = 'recaptcha_widget'
    requirements = ()
    url = "http://www.google.com/recaptcha/api/verify"
    headers={'Content-type': 'application/x-www-form-urlencoded'}

    def serialize(self, field, cstruct, readonly=False):
        from kotti_settings.util import get_setting
        if cstruct in (null, None):
            cstruct = ''
        confirm = getattr(field, 'confirm', '')
        template = readonly and self.readonly_template or self.template
        return field.renderer(template, field=field, cstruct=cstruct,
                              public_key=get_setting('public_key'),
                              theme=get_setting('recaptcha_theme')
                              )

    def deserialize(self, field, pstruct):
        from kotti_settings.util import get_setting
        if pstruct is null:
            return null
        challenge = pstruct.get('recaptcha_challenge_field') or ''
        response = pstruct.get('recaptcha_response_field') or ''
        if not response:
            raise Invalid(field.schema, 'No input')
        if not challenge:
            raise Invalid(field.schema, 'Missing challenge')
        privatekey = get_setting('private_key')
        remoteip = self.request.remote_addr
        data = urlencode(dict(privatekey=privatekey,
                              remoteip=remoteip,
                              challenge=challenge,
                              response=response))
        h = httplib2.Http(timeout=10)
        try:
            resp, content = h.request(self.url,
                                      "POST",
                                      headers=self.headers,
                                      body=data)
        except AttributeError as e:
            if e=="'NoneType' object has no attribute 'makefile'":
                ## XXX: catch a possible httplib regression in 2.7 where
                ## XXX: there is no connextion made to the socker so
                ## XXX sock is still None when makefile is called.
                raise Invalid(field.schema,
                              "Could not connect to the captcha service.")
        if not resp['status'] == '200':
            raise Invalid(field.schema,
                          "There was an error talking to the recaptcha \
                          server{0}".format(resp['status']))
        valid, reason = content.split('\n')
        if not valid == 'true':
            if reason == 'incorrect-captcha-sol':
                reason = _(u"Incorrect solution")
            raise Invalid(field.schema, reason.replace('\\n', ' ').strip("'") )
        return pstruct


@colander.deferred
def deferred_recaptcha_widget(node, kw):
    request = kw['request']
    return RecaptchaWidget(request=request)
