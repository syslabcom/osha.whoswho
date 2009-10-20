from Products.Five import zcml
from Products.Five import fiveconfigure

from Testing import ZopeTestCase as ztc

from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup
from Products.PloneTestCase import layer

SiteLayer = layer.PloneSite

class OSHAWhosWhoLayer(SiteLayer):
    @classmethod
    def setUp(cls):
        """Set up additional products and ZCML required to test this product.
        """
        ztc.installProduct('VocabularyPickerWidget')
        ztc.installProduct('ATVocabularyManager')
        ptc.setupPloneSite(products=[
            'osha.whoswho', 
            'Products.VocabularyPickerWidget', 
            'Products.ATVocabularyManager'
            ], extension_profiles=[
            "osha.whoswho:default",
            ])

        # Load the ZCML configuration for this package and its dependencies

        fiveconfigure.debug_mode = True
        import osha.whoswho
        zcml.load_config('configure.zcml', osha.whoswho)
        fiveconfigure.debug_mode = False

        
        SiteLayer.setUp()

# The order here is important: We first call the deferred function and then 
# let PloneTestCase install it during Plone site setup

class TestCase(ptc.PloneTestCase):
    """Base class used for test cases
    """
    layer = OSHAWhosWhoLayer

class FunctionalTestCase(ptc.FunctionalTestCase):
    """Test case class used for functional (doc-)tests
    """
    layer = OSHAWhosWhoLayer
