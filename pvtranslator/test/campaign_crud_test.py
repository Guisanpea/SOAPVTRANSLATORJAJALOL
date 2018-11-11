import time
from pvtranslator.entities.campaign import Campaign
from pvtranslator.facades.campaign_facade import CampaignFacade
from pvtranslator.start import start_engine


def test_create():
    scoped_session = start_engine()
    session = scoped_session()

    campaign = Campaign(name='sample', date=time.localtime(time.time()), module_id=1)

    facade = CampaignFacade(session)
    facade.create_campaign(campaign=campaign)

    query = session.query(Campaign).filter_by(id=campaign.id)
    campaign_query = query.all()

    assert len(campaign_query) == 1
    assert campaign_query[0] is campaign

    session.close()


def test_update():
    scoped_session = start_engine()
    session = scoped_session()

    # get first campaign
    query = session.query(Campaign).filter_by(id=1)
    campaign_query = query.all()
    campaign = campaign_query[0]
    campaign.name = campaign.name + "_update"

    # update
    facade = CampaignFacade(session)
    facade.update_campaign(campaign)

    # get campaign again
    query = session.query(Campaign).filter_by(id=1)
    campaign_query = query.all()

    assert len(campaign_query) == 1
    assert campaign_query[0] is campaign

    session.close()


def test_delete():

    scoped_session = start_engine()
    session = scoped_session()

    # get first campaign
    query = session.query(Campaign).filter_by(id=1)
    campaign_query = query.all()
    campaign = campaign_query[0]

    # delete
    facade = CampaignFacade(session)
    facade.delete_campaign(campaign)

    # get campaign again
    query = session.query(Campaign).filter_by(id=1)
    campaign_query = query.all()

    assert len(campaign_query) == 0

    session.close()


def test():
    test_create()
    test_update()
    test_delete()