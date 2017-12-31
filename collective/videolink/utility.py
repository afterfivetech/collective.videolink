from zope.annotation.interfaces import IAnnotations
from zope.interface.declarations import alsoProvides
from zope.interface.declarations import noLongerProvides
import hashlib
from zope.interface.declarations import providedBy
from collective.videolink.interfaces import IVideoLinkThumb, IVideoLinkOembedable
import requests


def add_thumbnail(context, event):
    """
    annotates the current context with a thumbnail based on its remote_url
    updates the thumbnail if the remote_url has changed on save
    
    @param context: Zope object for which the event was fired for. Usually this is Plone content object.

    @param event: Subclass of event.
    """
    if '/portal_factory/' in context.absolute_url():
        return context
    if old_hashed_url(context) and not hashed_url_changed(context):
        return context
    unmark_video_link(context)
    _thumbnail = get_thumbnail(context)    
    if _thumbnail:
        update_thumbnail(context)
        mark_video_link(context)
    else:
        remove_thumbnail(
              unmark_video_link(context)
              )
        
        return context

def hashed_url_changed(context):
    candidate_hashed_remote_url = hashlib.md5(
                                      get_remote_url(context)
                                  ).digest()
    
    return hashed_url(context) == candidate_hashed_remote_url

def get_json(context):
    """Get the embed_json for a given context"""
    remote_url = get_remote_url(context)
    query = "https://noembed.com/embed?url={}".format(remote_url)
    response = requests.get(query)
    return response.json()

def get_remote_url(context):
    try:
        remote_url = context.getRemoteUrl()
    except AttributeError:
        remote_url = context.remoteUrl
    return remote_url
    
def get_thumbnail(context):
    """ given a context, use noembed.com to retrieve 
        a thumbnail
    """
    output = get_json(context)
    return output.get('thumbnail_url',None)
    
def mark_video_link(context):
    alsoProvides(context,
                     IVideoLinkThumb,
                     IVideoLinkOembedable
                     )
    context.portal_catalog.reindexObject(self.context, 
                                         idxs=['object_provides'], 
                                         update_metadata=1
                                         )
    return context
    
def old_hashed_url(context):
    annotations = IAnnotations(context)
    data = annotations.get('collective.videolink.data', {})
    return data.get('hashed_remote_url', None)
    
def remove_thumbnail(context):
    annotations = IAnnotations(context)
    if 'thumbnail' in annotations['collective.videolink.data']:
        del annotations['collective.videolink.data']['thumbnail']
    return context
    
def unmark_video_link(context):
    noLongerProvides(context, IVideoLinkThumb)
    noLongerProvides(context, IVideoLinkOembedable)
    # idea borrowed from https://gist.github.com/jensens/3518210#file-action-py-L17-L19
    context.portal_catalog.reindexObject(context, 
                                         idxs=['object_provides'], 
                                         update_metadata=1
                                         )
    return context

def update_thumbnail(context):
    annotations = IAnnotations(context)
    annotations['collective.videolink.data']['thumbnail'] = get_thumbnail(context)