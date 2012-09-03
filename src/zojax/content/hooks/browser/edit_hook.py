from zope import component

from zojax.content.hooks.browser.interfaces import IContexHookForm
from zojax.content.hooks.interfaces import IContentHook, IContentHookable
from zojax.content.space.interfaces import ISpace
from zojax.content.space.utils import getSpace
from zojax.layoutform import Fields, PageletEditSubForm
from zojax.layoutform.subform import PageletAddSubForm


class EditHook(PageletEditSubForm):
    prefix = 'content.hooks'
    ignoreContext = True

    @property
    def fields(self):
        if self.isAvailable():
            return Fields(IContexHookForm)
        else:
            return Fields()

    def postUpdate(self):
        if 'content.hooks.widgets.checkOptions' in self.request.keys():
            for option in self.request.get('content.hooks.widgets.checkOptions'):
                (component.getAdapter(self.parentForm.getContent(), IContentHook, option)).__call__()

    def applyChanges(self, data):
        pass

    def isAvailable(self):
        cur_space = getSpace(self.parentForm)
        if cur_space.get('blog'):
            cur_space = cur_space.__parent__
            while ISpace.providedBy(cur_space):
                if cur_space.get('blog'):
                    return True
                cur_space = cur_space.__parent__
            return False
        else:
            return False

class EditIsoHook(PageletAddSubForm):
    prefix = 'content.iso.hooks'
    ignoreContext = True

    @property
    def fields(self):
        if self.isAvailable():
            return Fields(IContexHookForm)
        else:
            return Fields()

    def postUpdate(self):
        if 'content.iso.hooks.widgets.checkOptions' in self.request.keys() and self.parentForm._addedObject:
            for option in self.request.get('content.iso.hooks.widgets.checkOptions'):
                (component.getAdapter(self.parentForm._addedObject, IContentHook, option)).__call__()

    def applyChanges(self, data):
        pass

    def isAvailable(self):
        cur_space = getSpace(self.parentForm)
        if cur_space.get('blog'):
            cur_space = cur_space.__parent__
            while ISpace.providedBy(cur_space):
                if cur_space.get('blog'):
                    return True
                cur_space = cur_space.__parent__
            return False
        else:
            return False