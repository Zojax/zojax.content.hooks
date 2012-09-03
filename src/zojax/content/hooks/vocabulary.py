from zope.component import getAdapters
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope import interface

from zojax.content.hooks.interfaces import IContentHook

class HooksVocabulary(object):
    interface.implements(IVocabularyFactory)
    def __call__(self, context):
        terms = []
        for name, form in getAdapters((context,), IContentHook):
            terms.append(SimpleTerm(value=name, token=name, title=form.title))
        return SimpleVocabulary(terms)