from otree.api import *

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'demographic'
    PLAYERS_PER_GROUP = None
    NUM_GAME_ROUNDS = 1
    NUM_ROUNDS = 1



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    version = models.StringField()
    age = models.IntegerField(label="What is your age in years?", min=18, max=120)
    gender = models.StringField(
        label="What is your gender?",
        choices=["Male", "Female","Non-binary/third gender","Prefer not to say"],
        widget=widgets.RadioSelect
    )
    race = models.StringField(
        label="Choose one or more races that you consider yourself to be",
        choices=["White or Caucasian","Black or Africa American","American Indian/Native American or Alaska Native","Asian","Pacific Islander","Other","Prefer not to say"],
        widget=widgets.RadioSelect
    )
    education = models.StringField(
        label="What is your highest level of education you have completed?",
        choices=["High school or less","High school diploma or GED","Some college, but no degree","Associates or technical degree","Bachelor's degree","Graduate or professional degree(MA, MS, MBA, PhD, JD, MD, DDS etc.)"],
        widget=widgets.RadioSelect
    )
    experience = models.StringField(
        label="Before today’s study, how many economics experiments or surveys have you participated in?",
        choices=["0","1","2","3","4","5","More than 5","I don't remember"],
        widget=widgets.RadioSelect
    )
    # attention_check_question_1 = models.StringField(
    #     label="Please select 'Median Income' for this question to show you are paying attention.",
    #     choices=["High Income","Median Income","Low Income","Prefer not to say"],
    #     widget=widgets.RadioSelect
    # )


def creating_session(subsession: Subsession):
    import itertools
    # 创建循环迭代器，轮流分配version1和version2
    versions = itertools.cycle(['binary_first', 'bret_first'])

    for player in subsession.get_players():
        # 分配版本
        player.version = next(versions)
        player.participant.version = player.version

        # # 根据版本设置要跳过的app
        # if player.version == 'version1':
        #     # version1: A->B1->C->D
        #     player.participant.skip_apps = ['B2']
        # else:
        #     # version2: A->C->B2->D
        #     player.participant.skip_apps = ['B1']

# PAGES
class InformConsent(Page):
    form_model = "player"
    form_fields = []
    # @staticmethod
    # def is_displayed(player: Player):
    #     if player.round_number == 1:
    #         return True
    #     else:
    #         return False


class Introduction(Page):
    form_model = "player"
    form_fields = []
    # @staticmethod
    # def is_displayed(player: Player):
    #     if player.round_number == 1:
    #         return True
    #     else:
    #         return False


class SurveyQuestions1(Page):
    form_model = "player"
    form_fields = ["age","gender","race"]
    # @staticmethod
    # def is_displayed(player: Player):
    #     if player.round_number == 1:
    #         return True
    #     else:
    #         return player.participant.vars["failed_attention_check"]


class SurveyQuestions2(Page):
    form_model = "player"
    form_fields = ["education", "experience"]
    # @staticmethod
    # def is_displayed(player: Player):
    #     if player.round_number == 1:
    #         return True
    #     else:
    #         return player.participant.vars["failed_attention_check"]
    #
    # @staticmethod
    # def before_next_page(player: Player, timeout_happened):
    #     if player.attention_check_question_1 == C.ATTENTION_CHECK_CORRECT_ANSWER:
    #         player.participant.vars["failed_attention_check"] = False
    #     else:
    #         player.participant.vars["failed_attention_check"] = True


# class FailedAttentionCheck(Page):
#     @staticmethod
#     def is_displayed(player: Player):
#         return player.participant.vars["failed_attention_check"]


class SurveyEnd(Page):
    form_model = "player"
    form_fields = []

    # @staticmethod
    # def is_displayed(player: Player):
    #     return player.round_number >= C.NUM_ATTENTION_CHECK_TRIES

    @staticmethod
    def app_after_this_page(player: Player, timeout_happened):
        if player.version == 'binary_first':
            return 'binary_1'
        else:
            return 'bret'


# class TenSideDie(Page):
#     form_model = "player"
#     form_fields = []

page_sequence = [InformConsent, Introduction, SurveyQuestions1, SurveyQuestions2, SurveyEnd]
