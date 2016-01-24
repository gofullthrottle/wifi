import os


ENV = "NEW_RELIC_CONFIG_FILE"

"""
these two objects will be imported from PostHandler,
if they are empty new relic monitoring will not happen
"""
application = None
agent = None

monitor = False
config = os.environ.get(ENV, "")
if config and os.path.isfile(config):
    monitor = True
else:
    config = os.path.abspath("../newrelic/newrelic.ini")
    print config
    if os.path.isfile(config):
        monitor = True
        os.environ[ENV] = config
if monitor:
    import newrelic.agent as agent
    application = agent.application()
