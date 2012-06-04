from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import quickInstallProduct
from plone.testing import z2


class OshaWhosWho(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import osha.whoswho
        self.loadZCML('configure.zcml', package=osha.whoswho)

        z2.installProduct(app, 'Products.VocabularyPickerWidget')
        z2.installProduct(app, 'Products.ATVocabularyManager')
        z2.installProduct(app, 'osha.whoswho')

    def setUpPloneSite(self, portal):
        quickInstallProduct(portal, 'Products.VocabularyPickerWidget')
        quickInstallProduct(portal, 'Products.ATVocabularyManager')
        applyProfile(portal, 'osha.whoswho:default')

    def tearDownZope(self, app):
        z2.uninstallProduct(app, 'Products.VocabularyPickerWidget')
        z2.uninstallProduct(app, 'Products.ATVocabularyManager')
        z2.uninstallProduct(app, 'osha.whoswho')


OSHA_WHOSWHO_FIXTURE = OshaWhosWho()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(OSHA_WHOSWHO_FIXTURE,),
    name="OshaWhosWho:Integration")
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(OSHA_WHOSWHO_FIXTURE,),
    name="OshaWhosWho:Functional")
