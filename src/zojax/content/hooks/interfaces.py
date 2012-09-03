from zope import interface, schema
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('zojax.content.hooks')


class IContentHook(interface.Interface):
    title = schema.TextLine(
        title = _(u'Title'),
        description = _(u'Hook title.'),
        default = u'',
        missing_value = u'')

    selectable = schema.Bool(title=_(u'Show states on map'), default=False)

    def isAvailable(self):
        pass

    def __call__(self):
        pass

class IContentHookable(interface.Interface):
    pass
