#from Acquisition import aq_inner
#from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone import api
from Products.Five import BrowserView

class RedirectView(BrowserView):
     
    def call(self, index='', value=''):
    	"""redirect to indexed content"""
    	    	
    	catalog = api.portal.get_tool(name='portal_catalog')
    	content_items = catalog(portal_type=value)
    	return content_items[0]
    