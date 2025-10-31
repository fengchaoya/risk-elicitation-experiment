from os import environ


SESSION_CONFIGS = [
    dict(
        name='experiment',
        app_sequence=['demographic','binary_1','bret','binary_2','payment'],
        num_demo_participants=10,
        time_pressure=True,
    ),
    # dict(
    #     name='surveyapp2',
    #     app_sequence=['bret','binary','payment'],
    #     num_demo_participants=10,
    #     time_pressure=False,
    # ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.10, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['payoff_binary','payoff_bret','payoff_total','version','bq1','bq2','bq3','bq4','bq5','bq6','bq7','bq8','bq9','bq10','dice2']
SESSION_FIELDS = []


POINTS_DECIMAL_PLACES = 1
# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False



ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '5402917984619'
