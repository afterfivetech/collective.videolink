from zope.annotation.interfaces import IAnnotations
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
    if data.has_key('thumbnail'):
         return data['thumbnail']

    try:
        remote_url = context.getRemoteUrl()
    except AttributeError:
        remote_url = context.remoteUrl

    annotations['collective.videolink.data'] = {}
    query = "https://noembed.com/embed?url={}".format(remote_url)
    response = requests.get(query)
    embed_json = response.json()
    annotations['collective.videolink.data']['thumbnail'] = thumbnail_url = embed_json['thumbnail_url']
    return thumbnail_url