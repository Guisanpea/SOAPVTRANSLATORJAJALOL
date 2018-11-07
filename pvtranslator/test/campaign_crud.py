import time

from sqlalchemy.orm import sessionmaker

from pvtranslator.entities.campaign import Campaign
from pvtranslator.facades.campaign_facade import CampaignFacade
from pvtranslator.start import start_engine


def test_create():
    start_engine()

    Session = sessionmaker()
    session = Session()

    campaign = Campaign(name='sample', date=time.localtime(time.time()))

    facade = CampaignFacade()
    facade.create_campaign(campaign=campaign)

    db_user = session.query(Campaign).filter_by(name='sample')

    assert campaign is db_user
