from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing.zope import WSGI_SERVER_FIXTURE

import hidrosalt_consulting


class HIDROSALT_CONSULTINGLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=hidrosalt_consulting)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "hidrosalt_consulting:default")
        applyProfile(portal, "hidrosalt_consulting:initial")


HIDROSALT_CONSULTING_FIXTURE = HIDROSALT_CONSULTINGLayer()


HIDROSALT_CONSULTING_INTEGRATION_TESTING = IntegrationTesting(
    bases=(HIDROSALT_CONSULTING_FIXTURE,),
    name="HIDROSALT_CONSULTINGLayer:IntegrationTesting",
)


HIDROSALT_CONSULTING_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(HIDROSALT_CONSULTING_FIXTURE, WSGI_SERVER_FIXTURE),
    name="HIDROSALT_CONSULTINGLayer:FunctionalTesting",
)


HIDROSALT_CONSULTINGACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        HIDROSALT_CONSULTING_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        WSGI_SERVER_FIXTURE,
    ),
    name="HIDROSALT_CONSULTINGLayer:AcceptanceTesting",
)
