from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import mapper
from kotti import metadata
from kotti.resources import Content

class ContactForm(Content):
    type_info = Content.type_info.copy(
        name=u'ContactForm',
        add_view=u'add_contactform',
        addable_to=[u'Document'],
        )

    def __init__(self, recipient=u"", body=u"", **kwargs):
        super(ContactForm, self).__init__(**kwargs)
        self.recipient = recipient
        self.body = body

contactforms = Table(
    'contact_forms', metadata,
    Column('id', Integer, ForeignKey('contents.id'), primary_key=True),
    Column('recipient', String(255), nullable=False),
    Column('body', Text),
)

mapper(ContactForm, contactforms, inherits=Content,
       polymorphic_identity='contact_form')
