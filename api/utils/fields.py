# -*- coding: utf-8 -*-
import shortuuid

from django_extensions.db.fields import UUIDField, UUIDVersionError


class ShortUUIDField(UUIDField):
    """ ShortUUIDFied

    Generates concise (22 characters instead of 36), unambiguous, URL-safe UUIDs.

    Based on `shortuuid`: https://github.com/stochastic-technologies/shortuuid
    """

    def __init__(self, *args, **kwargs):
        super(ShortUUIDField, self).__init__(*args, **kwargs)
        kwargs['max_length'] = 22

    def create_uuid(self):
        if not self.version or self.version == 4:
            return shortuuid.uuid()
        elif self.version == 1:
            return shortuuid.uuid()
        elif self.version == 2:
            raise UUIDVersionError("UUID version 2 is not supported.")
        elif self.version == 3:
            raise UUIDVersionError("UUID version 3 is not supported.")
        elif self.version == 5:
            return shortuuid.uuid(name=self.namespace)
        else:
            raise UUIDVersionError("UUID version %s is not valid." % self.version)
