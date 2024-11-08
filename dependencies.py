from dependency_injector import containers, providers
from database import engine, get_session


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["app.api"])

    db_engine = providers.Singleton(lambda: engine)
    db_session = providers.Resource(get_session)