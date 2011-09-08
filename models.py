from dictshield.document import Document
from dictshield.fields import (StringField,
                               IntField,
                               URLField)

from dictshield.fields import ObjectIdField

from brubeck.timekeeping import MillisecondField


###
### Social Models
###

class ShortLink(Document):
    """A UserProfile is essentially any publicly available info about the user.
    Stored in a document separate from the User itself for security.
    """
    link = URLField(max_length=100)
    short_id = StringField(max_length=10) # 10 is HUGE

    created_at = MillisecondField()
    updated_at = MillisecondField()
    dereferences = IntField(default=0)

    def __unicode__(self):
        return u'<shortlink: %s>' % (self.short_id)
