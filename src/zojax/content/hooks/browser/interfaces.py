from zope.i18nmessageid import MessageFactory
from zope import interface, schema

from zojax.widget.checkbox.field import CheckboxList

_ = MessageFactory('zojax.content.hooks')

class IContexHookForm(interface.Interface):

    checkOptions = CheckboxList(
        title = _(u'Blog options'),
        vocabulary = 'zojax.content.hooks',
        required = False)
