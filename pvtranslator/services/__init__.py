from spyne.protocol.soap.soap11 import Soap11
from spyne import Application
from pvtranslator.services.campaign_crud_service import CampaignCrudService
from pvtranslator.services.module_crud_service import ModuleCrudService


# return spyne application build with all services
def get_application():

    application = Application([CampaignCrudService, ModuleCrudService],
                              tns='pvtranslator',
                              in_protocol=Soap11(),
                              out_protocol=Soap11()
                              )
    return application
