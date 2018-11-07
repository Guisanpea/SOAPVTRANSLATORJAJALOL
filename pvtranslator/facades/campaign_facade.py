from pvtranslator.entities.campaign import Campaign
from sqlalchemy.orm import sessionmaker


class CampaignFacade:
    session = None

    def __init__(self):
        session = sessionmaker()
        self.session = session()

    def create_campaign(self, campaign: Campaign):
        self.session.add(campaign)
        self.session.commit()

    def delete_campaign(self, campaign: Campaign):
        self.session.delete(campaign)
        self.session.commit()

    def read_campaigns(self):
        return self.session.query(Campaign).order_by(Campaign.date)

    def commit_campaign_update(self):
        self.session.commit()
