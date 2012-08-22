from zope import interface, schema
from zojax.widget.checkbox.field import CheckboxList
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('zojax.quick.contenttypes')


class IContentHook(interface.Interface):
    title = schema.TextLine(
        title = _(u'Title'),
        description = _(u'Hook title.'),
        default = u'',
        missing_value = u'',
        required = True)

    selectable = schema.Bool(title=_(u'Show states on map'), default=False)

    def isAvailable(self):
        pass

    def __call__(self):
        pass