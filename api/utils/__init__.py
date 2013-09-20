# -*- coding: utf-8 -*-
from django.template.defaultfilters import slugify


def sane_repr(*attrs):
    if 'id' not in attrs and 'pk' not in attrs:
        attrs = ('id',) + attrs

    def _repr(self):
        cls = type(self).__name__

        pairs = ('%s=%s' % (a, repr(getattr(self, a, None)))
                 for a in attrs)

        return u'<%s at 0x%x: %s>' % (cls, id(self), ', '.join(pairs))

    return _repr


def slugify_instance(inst, label, **kwargs):
    base_slug = slugify(label)
    manager = type(inst).objects
    inst.slug = base_slug
    n = 0
    while manager.filter(slug=inst.slug, **kwargs).exists():
        n += 1
        inst.slug = base_slug + '-' + str(n)
