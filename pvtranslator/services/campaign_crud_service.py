from spyne import ServiceBase, rpc, Unicode, Integer, Iterable, UnsignedInteger32

from pvtranslator.entities.campaign import Campaign
from pvtranslator.facades.campaign_facade import CampaignFacade
from pvtranslator.start import start_engine


class CampaignCrudService(ServiceBase):

    # create campaign if it's possible and return id
    @rpc(Campaign, _returns=UnsignedInteger32)
    def create_campaign(ctx, campaign):
        campaign_id = -1

        if campaign.id is None:
            scoped_session = start_engine()
            session = scoped_session()
            facade = CampaignFacade(session)
            facade.create_campaign(campaign=campaign)
            campaign_id = facade.get_campaign_by_name(name=campaign.name).id

        session.close()
        return campaign_id