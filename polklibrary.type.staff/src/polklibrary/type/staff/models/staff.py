from plone import api
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from zope import schema

class IStaff(model.Schema):

    title = schema.TextLine(
            title=u"Name",
            required=True,
        )

    position = schema.TextLine(
            title=u"Position",
            required=True,
        )
        
    department = schema.TextLine(
            title=u"Department",
            required=True,
        )
        
    email = schema.TextLine(
            title=u"Email",
            required=False,
        )
        
    phone = schema.TextLine(
            title=u"Office Phone",
            required=False,
        )
        
    fax = schema.TextLine(
            title=u"Fax Number",
            required=False,
        )
        
    location = schema.TextLine(
            title=u"Office",
            required=False,
        )
        
    education = RichText(
            title=u"Education",
            default_mime_type='text/structured',
            required=False,
            default=u"",
        )

    professional_background = RichText(
            title=u"Professional Background",
            default_mime_type='text/structured',
            required=False,
            default=u"",
        )

    community_involvment = RichText(
            title=u"University and Community Involvement",
            default_mime_type='text/structured',
            required=False,
            default=u"",
        )
        
    image = NamedBlobImage(
            title=u"Staff Image",
            required=False,
        )
        

        
        