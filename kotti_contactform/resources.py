from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from kotti.resources import Content
from pyramid.i18n import TranslationStringFactory
_ = TranslationStringFactory('kotti_contactform')

class ContactForm(Content):
    __tablename__ = 'contact_forms'
    __mapper_args__ = dict(polymorphic_identity='contact_form')
    id = Column('id', Integer, ForeignKey('contents.id'), primary_key=True)
    recipient = Column(String(255), nullable=False)
    body = Column(Text)
    type_info = Content.type_info.copy(
        name=u'ContactForm',
        title=_(u'Contact form'),
        add_view=u'add_contactform',
        addable_to=[u'Document'],
        )

    def __init__(self, recipient=u"", body=u"", **kwargs):
        super(ContactForm, self).__init__(**kwargs)
        self.recipient = recipient
        self.body = body
