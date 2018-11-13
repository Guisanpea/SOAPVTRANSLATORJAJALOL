from spyne import Unicode

from pvtranslator.entities.campaign import Campaign


class CampaignFacade:
    session = None

    def __init__(self, session):
        self.session = session

    def create_campaign(self, campaign: Campaign):
        self.session.add(campaign)
        self.session.commit()

    def delete_campaign(self, campaign: Campaign):
        self.session.delete(self.get_campaign_by_id(campaign.id))
        self.session.commit()

    def read_campaigns(self):
        return self.session.query(Campaign).order_by(Campaign.date)

    def update_campaign(self, campaign: Campaign):
        persistent_campaign = self.get_campaign_by_id(campaign.id)
        persistent_campaign.name = campaign.name
        persistent_campaign.date = campaign.date
        persistent_campaign.module_id = campaign.module_id
        self.session.commit()

    def get_campaign_by_name(self, name: Unicode):
        query = self.session.query(Campaign).filter_by(name=name)
        campaign_query = query.all()
        if len(campaign_query) == 0:
            return None
        else:
            return campaign_query[0]

    def get_campaign_by_id(self, campaign_id):
        query = self.session.query(Campaign).filter_by(id=campaign_id)
        campaign_query = query.all()
        if len(campaign_query) == 0:
            return None
        else:
            return campaign_query[0]

    def get_campaigns_from_module_id(self, module_id):
        query = self.session.query(Campaign).filter_by(module_id=module_id)
        campaign_query = query.all()
        if len(campaign_query) == 0:
            return []
        else:
            return campaign_query
