from zope.annotation.interfaces import IAnnotations
from zope.interface.declarations import alsoProvides
from zope.interface.declarations import providedBy
from collective.videolink.interfaces import IVideoLinkThumb, IVideoLinkOembedable
import requests

def add_thumbnail(context, event):
    """
    @param context: Zope object for which the event was fired for. Usually this is Plone content object.

    @param event: Subclass of event.
    """
    if '/portal_factory/' in context.absolute_url():
        return
    annotations = IAnnotations(context)
    try:
        data = annotations['collective.videolink.data']
    except KeyError:
        data = annotations['collective.videolink.data'] = {}
    if 'thumbnail' in data:
        if IVideoLinkThumb in providedBy(context):
            return data['thumbnail']

    try:
        remote_url = context.getRemoteUrl()
    except AttributeError:
        remote_url = context.remoteUrl

    annotations['collective.videolink.data'] = {}
    query = "https://noembed.com/embed?url={}".format(remote_url)
    response = requests.get(query)
    embed_json = response.json()
    if 'error' not in embed_json:
        annotations['collective.videolink.data']['thumbnail'] = thumbnail_url = embed_json['thumbnail_url']
        alsoProvides(context, IVideoLinkThumb, IVideoLinkOembedable)
        return thumbnail_url