#from Acquisition import aq_inner
from plone import api

from Products.Five import BrowserView
#from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class RedirectView(BrowserView):
     
    def call(self, index='', value=''):
    	"""redirect to indexed content"""
    	return "will give you a page"
    	
    