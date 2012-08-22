from zope.component import getAdapters
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.interfaces import IVocabularyFactory
from zope import interface

from zojax.content.hooks.interfaces import IContentHook

class HooksVocabulary(object):
    interface.implements(IVocabularyFactory)
    def __call__(context):
        return SimpleVocabulary([(name, form) for name, form in
                                getAdapters((self.context, self, self.request), IContentHook)])