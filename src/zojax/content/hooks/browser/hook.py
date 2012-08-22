from zojax.layoutform import button, Fields, PageletEditSubForm
from zojax.content.type.interfaces import IDraftedContent
from zojax.content.discussion.interfaces import IContentDiscussion


class Hook(PageletEditSubForm):

    prefix = 'content.discussion'

    @property
    def fields(self):
        return Fields(self.extension.__schema__)

    def getContent(self):
        return self.extension

    def update(self):
        self.drafted = IDraftedContent.providedBy(self.context)
        self.extension = IContentDiscussion(self.context, None)

        super(ContentDiscussonEdit, self).update()

    def isAvailable(self):
        return self.extension is not None
