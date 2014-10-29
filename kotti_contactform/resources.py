from kotti.interfaces import IDefaultWorkflow
from kotti.resources import Content
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from zope.interface import implements

from kotti_contactform import _


class ContactForm(Content):

    __tablename__ = 'contact_forms'
    __mapper_args__ = dict(polymorphic_identity='contact_form')

    implements(IDefaultWorkflow)

    id = Column('id', Integer, ForeignKey('contents.id'), primary_key=True)
    sender = Column(String(255), nullable=False)
    recipient = Column(String(255), nullable=False)
    body = Column(Text)
    show_attachment = Column(Boolean(), nullable=False)

    type_info = Content.type_info.copy(
        name=u'ContactForm',
        title=_(u'Contact form'),
        add_view=u'add_contactform',
        addable_to=[u'Document'],
        selectable_default_views=[
            ('view-1-col', u'1 column layout'),
        ],
    )

    def __init__(self, sender=u"", recipient=u"", body=u"",
                 show_attachment=True, **kwargs):

        super(ContactForm, self).__init__(**kwargs)
        self.sender = sender
        self.recipient = recipient
        self.body = body
        self.show_attachment = show_attachment
