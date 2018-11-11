from spyne import ServiceBase, rpc, UnsignedInteger32, Integer, Iterable
from pvtranslator.entities.campaign import Campaign
from pvtranslator.facades.campaign_facade import CampaignFacade
from pvtranslator.start import start_engine


class CampaignCrudService(ServiceBase):

    # create campaign if it's possible and return id
    @rpc(Campaign,  _returns=UnsignedInteger32)
    def create_campaign(ctx, campaign):
        campaign_id = -1
        if campaign.id is None:
            scoped_session = start_engine()
            session = scoped_session()
            campaign_facade = CampaignFacade(session)
            campaign_facade.create_campaign(campaign=campaign)
            campaign_id = campaign_facade.get_campaign_by_name(name=campaign.name).id
            session.close()
        return campaign_id

    # delete campaign in cascade
    @rpc(Campaign)
    def delete_campaign(ctx, campaign):
        scoped_session = start_engine()
        session = scoped_session()
        facade = CampaignFacade(session)
        facade.delete_module(campaign=campaign)
        session.close()

    # update campaign
    @rpc(Campaign)
    def update_campaign(ctx, campaign):
        scoped_session = start_engine()
        session = scoped_session()
        facade = CampaignFacade(session)
        facade.update_module(module=campaign)
        session.close()

    # return campaign by id
    @rpc(Integer, _returns=Campaign)
    def get_campaign_by_id(ctx, campaign_id):
        scoped_session = start_engine()
        session = scoped_session()
        facade = CampaignFacade(session)
        campaign = facade.get_campaign_by_id(campaign_id=campaign_id)
        session.close()
        return campaign

    # return campaigns by module_id
    @rpc(Integer, _returns=Iterable(Campaign))
    def get_module_campaigns(ctx, module_id):
        scoped_session = start_engine()
        session = scoped_session()
        facade = CampaignFacade(session)
        campaigns = facade.get_campaigns_from_module_id(module_id=module_id)
        session.close()
        return campaigns
