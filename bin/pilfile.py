#!/home/ubuntu/workspace/src/collective.videolink/venv/bin/python
#
# The Python Imaging Library.
# $Id$
#
# a utility to identify image files
#
# this script identifies image files, extracting size and
# pixel mode information for known file formats.  Note that
# you don't need the PIL C extension to use this module.
#
# History:
# 0.0 1995-09-01 fl   Created
# 0.1 1996-05-18 fl   Modified options, added debugging mode
# 0.2 1996-12-29 fl   Added verify mode
# 0.3 1999-06-05 fl   Don't mess up on class exceptions (1.5.2 and later)
# 0.4 2003-09-30 fl   Expand wildcards on Windows; robustness tweaks
#

from __future__ import print_function



import sys
sys.path[0:0] = [
  '/home/ubuntu/workspace/buildout-cache/eggs/Plone-5.1rc2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Pillow-4.3.0-py2.7-linux-x86_64.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.PrintingMailHost-1.0-py2.7.egg',
  '/home/ubuntu/workspace/src/collective.videolink/src',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.robotframework-1.1.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/robotframework_ride-1.5.2.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/watchdog-0.8.3-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/robotframework_debuglibrary-0.8.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.testrunner-4.4.4-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.schema-4.5.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.i18n-4.2.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.configuration-3.7.4-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.component-4.4.1-py2.7.egg',
  '/home/ubuntu/workspace/src/collective.videolink/venv/lib/python2.7/site-packages',
  '/home/ubuntu/workspace/buildout-cache/eggs/selenium-2.53.6-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/robotsuite-1.7.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/robotframework_selenium2library-1.7.4-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/robotframework-3.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.uuid-1.0.4-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.testing-5.0.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.testing-5.0.8-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/five.globalrequest-1.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Babel-1.3-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.PluggableAuthService-1.11.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.PlonePAS-5.0.14-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.MailHost-2.13.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.CMFPlone-5.1rc2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.CMFCore-2.2.12-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/z3c.unconfigure-1.0.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/requests-2.18.4-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.patternslib-0.2.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/olefile-0.44-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.upgrade-2.0.10-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.iterate-3.3.6-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.dexterity-2.4.7-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.caching-1.2.19-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.CMFPlacefulWorkflow-1.7.3-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.ATContentTypes-2.3.7-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.Archetypes-1.14.3-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/archetypes.multilingual-3.0.6-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/pathtools-0.1.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/argh-0.26.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/PyYAML-3.12-py2.7-linux-x86_64.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.interface-4.4.3-py2.7-linux-x86_64.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.exceptions-3.6.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/six-1.10.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.event-3.5.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.i18nmessageid-4.1.0-py2.7-linux-x86_64.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/pytz-2017.3-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/unittest2-0.5.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/lxml-4.1.1-py2.7-linux-x86_64.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/docutils-0.14-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/decorator-4.1.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.publisher-4.3.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.lifecycleevent-3.6.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.browserpage-4.1.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.testing-3.9.7-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Zope2-2.13.26-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.GenericSetup-1.8.8-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.memoize-1.2.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/five.localsitemanager-2.0.6-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.dottedname-4.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.globalrequest-1.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.PluginRegistry-1.4-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.deprecation-4.3.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.session-3.6.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.protect-3.1.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.i18n-3.0.7-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.sendmail-3.7.5-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.deferredimport-3.5.3-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Persistence-2.13.2-py2.7-linux-x86_64.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/DocumentTemplate-2.13.4-py2.7-linux-x86_64.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/DateTime-4.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Acquisition-4.4.2-py2.7-linux-x86_64.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/AccessControl-3.0.13-py2.7-linux-x86_64.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.traversing-4.1.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.tales-3.5.3-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.tal-3.5.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.structuredtext-3.5.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.site-3.9.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.pagetemplate-4.2.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.location-3.9.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.container-3.11.2-py2.7-linux-x86_64.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.cachedescriptors-3.5.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.app.locales-3.7.5-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/z3c.autoinclude-0.3.7-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/transaction-2.1.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/slimit-0.8.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/pyScss-1.3.5-py2.7-linux-x86_64.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plonetheme.barceloneta-1.7.5-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.theme-3.0.3-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.subrequest-1.8.4-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.schema-1.0.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.registry-1.1.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.portlets-2.3-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.portlet.static-3.1.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.portlet.collection-3.3.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.outputfilters-3.0.3-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.locking-2.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.intelligenttext-2.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.indexer-1.0.4-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.contentrules-2.0.6-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.browserlayer-2.2.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.batching-1.1.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.workflow-3.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.vocabularies-4.0.4-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.viewletmanager-2.0.10-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.uuid-1.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.users-2.4-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.theming-2.0.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.registry-1.6.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.redirector-1.3.5-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.portlets-4.3.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.multilingual-5.1.3-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.locales-5.1.3-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.linkintegrity-3.3.3-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.layout-2.7.5-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.i18n-3.0.4-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.folder-1.2.4-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.discussion-3.0.4-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.customerize-1.3.7-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.controlpanel-3.0.4-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.contenttypes-1.4.7-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.contentrules-4.0.17-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.contentmenu-2.2.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.contentlisting-1.3.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.content-3.4.5-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.api-1.8.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/mockup-2.6.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/five.pt-2.2.5-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/five.customerize-1.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/borg.localrole-3.1.4-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/ZODB3-3.11.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.statusmessages-5.0.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.contentmigration-2.1.17-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.ResourceRegistries-3.0.5-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.PortalTransforms-3.1.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.PlacelessTranslationService-2.0.7-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.MimetypesRegistry-2.1.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.ExternalEditor-1.1.3-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.ExtendedPathIndex-3.2.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.DCWorkflow-2.2.5-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.CMFUid-2.2.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.CMFQuickInstallerTool-3.0.15-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.CMFFormController-3.1.5-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.CMFEditions-3.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.CMFDynamicViewFTI-4.1.5-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.CMFDiffTool-3.1.4-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/ExtensionClass-4.3.0-py2.7-linux-x86_64.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.app.publication-3.12.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.ZSQLMethods-2.13.5-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.security-4.1.1-py2.7-linux-x86_64.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/urllib3-1.22-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/idna-2.6-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/chardet-3.0.4-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/certifi-2017.11.5-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.ZCatalog-3.0.3-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.ramcache-1.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.viewlet-3.7.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.annotation-3.5.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/z3c.form-3.2.11-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.z3cform-0.9.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.supermodel-1.3.4-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.schemaeditor-2.0.18-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.rfc822-1.1.3-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.namedfile-4.2.4-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.formwidget.namedfile-2.0.5-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.dexterity-2.5.4-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.behavior-1.2.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.autoform-1.7.4-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.z3cform-3.0.3-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.textfield-1.2.9-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/z3c.zcmlhook-1.0b1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.browserresource-4.1.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.cachepurging-1.0.13-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.caching-1.1.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/python_dateutil-2.6.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.widgets-2.2.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.imaging-2.0.6-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.collection-1.2.5-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.blob-1.7.3-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/ZConfig-3.1.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.validation-2.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.datetime-3.4.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.contenttype-4.2.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.folder-1.0.9-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/collective.monkeypatcher-1.1.3-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.proxy-4.3.0-py2.7-linux-x86_64.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.browser-2.1.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/nt_svcutils-2.13.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/ZServer-3.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Record-2.13.0-py2.7-linux-x86_64.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.ZCTextIndex-2.13.5-py2.7-linux-x86_64.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.TemporaryFolder-3.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.StandardCacheManagers-2.13.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.Sessions-3.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.PythonScripts-2.13.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.MIMETools-2.13.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.ExternalMethod-2.13.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.BTreeFolder2-2.14.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/initgroups-4.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.testbrowser-3.11.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.size-3.4.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.sequencesort-3.4.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.ptresource-3.9.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.processlifetime-1.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.contentprovider-3.7.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.browsermenu-4.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zLOG-3.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zExceptions-2.13.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zdaemon-4.2.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/tempstorage-4.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/ZopeUndo-4.3-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/RestrictedPython-3.6.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.OFSP-2.13.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/MultiMapping-3.1-py2.7-linux-x86_64.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Missing-3.2-py2.7-linux-x86_64.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.keyring-3.0.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/repoze.xmliter-0.6-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.transformchain-1.2.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Unidecode-0.4.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.broken-3.6.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.filerepresentation-3.6.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zc.buildout-2.5.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/ply-3.4-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/pathlib-1.0.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/enum34-1.1.6-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.componentvocabulary-1.0.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.querystring-1.4.7-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/roman-1.4.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.resourceeditor-2.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.resource-1.2.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/diazo-1.2.8-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/feedparser-5.2.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/z3c.relationfield-0.7-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.relationfield-1.3.5-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.intid-1.1.3-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.versioningbehavior-1.3.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.lockingbehavior-1.0.5-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.app.event-3.0.7-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.stringinterp-1.2.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/simplejson-3.12.0-py2.7-linux-x86_64.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Chameleon-2.25-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/z3c.pt-3.0.0a1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/sourcecodegen-0.6.14-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/BTrees-4.4.1-py2.7-linux-x86_64.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/persistent-4.2.4.2-py2.7-linux-x86_64.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/ZODB-5.3.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/ZEO-5.1.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Markdown-2.6.9-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/python_gettext-3.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.ZopeVersionControl-1.1.3-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.copy-3.5.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.error-3.7.4-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.authentication-3.7.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/piexif-1.0.13-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.scale-3.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.synchronize-1.0.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.alterego-1.1.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/z3c.formwidget.query-0.16-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/z3c.caching-2.0a1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/archetypes.schemaextender-2.1.7-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/mechanize-0.2.5-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/future-0.16.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/cssselect-1.0.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.intid-3.7.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zc.relation-1.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/z3c.objpath-1.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/five.intid-1.1.2-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.formwidget.recurrence-2.1.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/plone.event-1.3.4-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/icalendar-4.0.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/Products.DateRecurringIndex-2.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zodbpickle-0.7.0-py2.7-linux-x86_64.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zc.lockfile-1.2.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/trollius-2.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/futures-3.1.1-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.untrustedpython-4.0.0-py2.7.egg',
  '/home/ubuntu/workspace/buildout-cache/eggs/zope.keyreference-3.6.4-py2.7.egg',
  ]


import getopt
import glob
import logging
import sys

from PIL import Image

if len(sys.argv) == 1:
    print("PIL File 0.4/2003-09-30 -- identify image files")
    print("Usage: pilfile [option] files...")
    print("Options:")
    print("  -f  list supported file formats")
    print("  -i  show associated info and tile data")
    print("  -v  verify file headers")
    print("  -q  quiet, don't warn for unidentified/missing/broken files")
    sys.exit(1)

try:
    opt, args = getopt.getopt(sys.argv[1:], "fqivD")
except getopt.error as v:
    print(v)
    sys.exit(1)

verbose = quiet = verify = 0
logging_level = "WARNING"

for o, a in opt:
    if o == "-f":
        Image.init()
        id = sorted(Image.ID)
        print("Supported formats:")
        for i in id:
            print(i, end=' ')
        sys.exit(1)
    elif o == "-i":
        verbose = 1
    elif o == "-q":
        quiet = 1
    elif o == "-v":
        verify = 1
    elif o == "-D":
        logging_level = "DEBUG"

logging.basicConfig(level=logging_level)


def globfix(files):
    # expand wildcards where necessary
    if sys.platform == "win32":
        out = []
        for file in files:
            if glob.has_magic(file):
                out.extend(glob.glob(file))
            else:
                out.append(file)
        return out
    return files

for file in globfix(args):
    try:
        im = Image.open(file)
        print("%s:" % file, im.format, "%dx%d" % im.size, im.mode, end=' ')
        if verbose:
            print(im.info, im.tile, end=' ')
        print()
        if verify:
            try:
                im.verify()
            except:
                if not quiet:
                    print("failed to verify image", end=' ')
                    print("(%s:%s)" % (sys.exc_info()[0], sys.exc_info()[1]))
    except IOError as v:
        if not quiet:
            print(file, "failed:", v)
    except:
        import traceback
        if not quiet:
            print(file, "failed:", "unexpected error")
            traceback.print_exc(file=sys.stdout)
