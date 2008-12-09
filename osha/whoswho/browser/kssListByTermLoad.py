import Acquisition
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from kss.core.ttwapi import ( startKSSCommands, getKSSCommandSet, renderKSSCommands )
import logging
logger = logging.getLogger('osha.whoswho')
from zope.component import getMultiAdapter

class kssListByLetterLoad(BrowserView):
    """called by kss, loads whoswhos by letter
    """

    def __call__(self):
        letter = self.request.get('letter', None)
        oldletter = self.request.get('oldletter', None)
        startKSSCommands(self, self.request)
#        logger.info(letter)
        whoswho_alphabetical = getMultiAdapter((self.context, self.request), name=u'whoswho_alphabetical') 
        res = whoswho_alphabetical.resultsByLetter(letter)
        restag = u"""<dl class="keylist" >"""
        for r in res:
            restag += u"""
                    <dt><a href="%(url)s" rel="nofollow">%(title)s</a>
                    </dt>
                    <dd>%(description)s</dd>
                    """ % dict(url=r[2], title=r[0], description=r[3])
        restag += u"""</dl>"""

        core = getKSSCommandSet('core')
        core.replaceInnerHTML('#slc-index-results h2', letter)
        core.replaceInnerHTML('#slc-index-results #resultcolA', restag)

        core.removeClass('#selected-term', 'current-term')
        core.addClass('#selected-term', 'index-term')

        core.removeClass('#%s-term'%letter, 'index-term')
        core.addClass('#%s-term'%letter, 'current-term')

        core.setAttribute('#selected-term', 'id', '%s-term'%oldletter)
        core.setAttribute('#%s-term'%letter, 'id', 'selected-term')
        core.setAttribute('#oldletter', 'value', letter)


        return renderKSSCommands() 


class kssListByTypeLoad(BrowserView):
    """ called by kss, load whoswho by type
    """

    def __call__(self):
        term = self.request.get('term', '')
        caption = self.request.get('caption', '')
        oldterm = self.request.get('oldterm', '')
        try:
            caption = unicode(caption, 'utf-8')
        except Exception, err:
            print "could not make unicode out of caption: %s" %err
        startKSSCommands(self, self.request)
#        logger.info(term)
        whoswho_type = getMultiAdapter((self.context, self.request), name=u'whoswho_type') 
        res = whoswho_type.resultsBySearchterm(term)

        restag = u"""<dl class="keylist" >"""
        for r in res:
            restag += u"""
                    <dt><a href="%(url)s" rel="nofollow">%(title)s</a>
                    </dt>
                    <dd>%(description)s</dd>
                    """ % dict(url=r.getURL(), 
                            title=unicode(r.Title, 'utf-8'), 
                            description=unicode(r.Description, 'utf-8'))
        restag += u"""</dl>"""

        term_leaf = term.split('::')[-1]
        oldterm_leaf = oldterm.split('::')[-1]
        core = getKSSCommandSet('core')
        core.replaceInnerHTML('#slc-index-results h2', caption)
        core.replaceInnerHTML('#slc-index-results #resultcolA', restag)
        core.removeClass('#selected-term', 'current-term')
        core.addClass('#selected-term', 'index-term')

        core.removeClass('#%s-term'%term_leaf, 'index-term')
        core.addClass('#%s-term'%term_leaf, 'current-term')

        core.setAttribute('#selected-term', 'id', '%s-term'%oldterm_leaf)
        core.setAttribute('#%s-term'%term_leaf, 'id', 'selected-term')
        core.setAttribute('#oldterm', 'value', term)


        return renderKSSCommands()
