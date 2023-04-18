from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing.zope import WSGI_SERVER_FIXTURE

import training


class TRAININGLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=training)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "training:default")
        applyProfile(portal, "training:initial")


TRAINING_FIXTURE = TRAININGLayer()


TRAINING_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TRAINING_FIXTURE,),
    name="TRAININGLayer:IntegrationTesting",
)


TRAINING_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(TRAINING_FIXTURE, WSGI_SERVER_FIXTURE),
    name="TRAININGLayer:FunctionalTesting",
)


TRAININGACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        TRAINING_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        WSGI_SERVER_FIXTURE,
    ),
    name="TRAININGLayer:AcceptanceTesting",
)
