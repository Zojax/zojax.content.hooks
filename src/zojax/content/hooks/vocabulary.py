from zope.component import getAdapters
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope import interface

from zojax.content.hooks.interfaces import IContentHook

class HooksVocabulary(object):
    interface.implements(IVocabularyFactory)
    def __call__(self, context):
        terms = []

        # see #420, blog posting options need to be sorted
        hooks = sorted(getAdapters((context,), IContentHook), key=lambda item: item[1].order)

        for name, form in hooks:
            terms.append(SimpleTerm(value=name, token=name, title=form.title))
        return SimpleVocabulary(terms)
