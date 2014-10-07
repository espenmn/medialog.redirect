#from Acquisition import aq_inner
#from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone import api
from Products.Five import BrowserView

class RedirectView(BrowserView):
     	
    def __call__(self, index='kortnummer', index_value=''):
    	"""redirect to indexed content"""
    	    	
    	catalog = api.portal.get_tool(name='portal_catalog')
    	#content_items = catalog(index=index_value) 
    	#content_items = catalog(kortnummer=index_value) 
    	content_items = catalog(kortnummer = index_value) 
    	content_url = content_items[0].getURL()
    	return self.context.REQUEST.RESPONSE.redirect(content_url)
    	