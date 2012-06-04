from plone.app.layout.globals.interfaces import IViewView
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from osha.whoswho.interfaces import IWhosWhoView
from zope.interface import implements

import Acquisition


class WhoswhoView(BrowserView):
    """View for displaying WhosWho Items by alphabet
    """
    implements(IWhosWhoView, IViewView)
    template = ViewPageTemplateFile('templates/whoswho_view.pt')

    def __call__(self):
        context = Acquisition.aq_inner(self.context)
        return self.template()
