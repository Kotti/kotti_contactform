from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import Boolean
from kotti.resources import Content
from kotti_contactform import _


class ContactForm(Content):
    __tablename__ = 'contact_forms'
    __mapper_args__ = dict(polymorphic_identity='contact_form')
    id = Column('id', Integer, ForeignKey('contents.id'), primary_key=True)
    recipient = Column(String(255), nullable=False)
    body = Column(Text)
    show_attachment = Column(Boolean(), nullable=False)
    type_info = Content.type_info.copy(
        name=u'ContactForm',
        title=_(u'Contact form'),
        add_view=u'add_contactform',
        addable_to=[u'Document'],
    )

    def __init__(self, recipient=u"", body=u"",
                 show_attachment=True, **kwargs):
        super(ContactForm, self).__init__(**kwargs)
        self.recipient = recipient
        self.body = body
        self.show_attachment = show_attachment
