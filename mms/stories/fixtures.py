from . import factories

def create_objects():

    factories.StoryUserFactory.create_batch(5)
    factories.StoryFactory.create_batch(5)
    factories.SubmissionFactory.create_batch(5)
    factories.WaypointFactory.create_batch(5)
