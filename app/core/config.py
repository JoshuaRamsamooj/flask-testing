class DevConfig:

    ENV = 'dev'


class TestConfig:

    ENV = 'test'


config = {
    'dev': DevConfig(),
    'test': TestConfig()
}
