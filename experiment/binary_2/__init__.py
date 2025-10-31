from otree.api import *
import random

doc = """
Your app description
"""




class C(BaseConstants):
    NAME_IN_URL = 'binary_2'
    PLAYERS_PER_GROUP = None
    NUM_ATTENTION_CHECK_TRIES = 2
    NUM_GAME_ROUNDS = 1
    NUM_ROUNDS = NUM_GAME_ROUNDS + NUM_ATTENTION_CHECK_TRIES - 1
    ATTENTION_CHECK_1_CORRECT_ANSWER = 'Option A'
    ATTENTION_CHECK_2_CORRECT_ANSWER = 'Option B'
    ATTENTION_CHECK_3_CORRECT_ANSWER = 'Option A'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    round_result = models.CurrencyField()
    payoff_current = models.CurrencyField()
    dice2 = models.IntegerField()
    bq1 = models.StringField(
        label="",
        # choices=[
        #     ('option a','A.$5 if throw of die is 1, $4 if throw of die is 2-10'),
        #     ('option b','B.$9.63 if throw of die is 1, $0.25 if throw of die is 2-10')
        #     ],
        choices = ['Option A','Option B'],
        widget=widgets.RadioSelectHorizontal
    )
    bq2 = models.StringField(
        label="",
        # choices=[
        #     ('option a','A.$5 if throw of die is 1-2, $4 if throw of die is 3-10'),
        #     ('option b','B.$9.63 if throw of die is 1-2, $0.25 if throw of die is 3-10')
        #     ],
        choices=['Option A', 'Option B'],
        widget=widgets.RadioSelectHorizontal
    )
    bq3 = models.StringField(
        label="",
        # choices=[
        #     ('option a','A.$5 if throw of die is 1-3, $4 if throw of die is 4-10'),
        #     ('option b','B.$9.63 if throw of die is 1-3, $0.25 if throw of die is 4-10')
        #     ],
        choices=['Option A', 'Option B'],
        widget=widgets.RadioSelectHorizontal
    )
    bq4 = models.StringField(
        label="",
        # choices=[
        #     ('option a','A.$5 if throw of die is 1-4, $4 if throw of die is 5-10'),
        #     ('option b','B.$9.63 if throw of die is 1-4, $0.25 if throw of die is 5-10')
        #     ],
        choices=['Option A', 'Option B'],
        widget = widgets.RadioSelectHorizontal
    )
    bq5 = models.StringField(
        label="",
        # choices=[
        #     ('option a','A.$5 if throw of die is 1-5, $4 if throw of die is 6-10'),
        #     ('option b','B.$9.63 if throw of die is 1-5, $0.25 if throw of die is 6-10')
        #     ],
        choices=['Option A', 'Option B'],
        widget=widgets.RadioSelectHorizontal
    )
    bq6 = models.StringField(
        label="",
        # choices=[
        #     ('option a','A.$5 if throw of die is 1-6, $4 if throw of die is 7-10'),
        #     ('option b','B.$9.63 if throw of die is 1-6, $0.25 if throw of die is 7-10')
        #     ],
        choices=['Option A', 'Option B'],
        widget=widgets.RadioSelectHorizontal
    )
    bq7 = models.StringField(
        label="",
        # choices=[
        #     ('option a','A.$5 if throw of die is 1-7, $4 if throw of die is 8-10'),
        #     ('option b','B.$9.63 if throw of die is 1-7, $0.25 if throw of die is 8-10')
        #     ],
        choices=['Option A', 'Option B'],
        widget=widgets.RadioSelectHorizontal
    )
    bq8= models.StringField(
        label="",
        # choices=[
        #     ('option a','A.$5 if throw of die is 1-8, $4 if throw of die is 9-10'),
        #     ('option b','B.$9.63 if throw of die is 1-8, $0.25 if throw of die is 9-10')
        #     ],
        choices=['Option A', 'Option B'],
        widget=widgets.RadioSelectHorizontal
    )
    bq9 = models.StringField(
        label="",
        # choices=[
        #     ('option a','A.$5 if throw of die is 1-9, $4 if throw of die is 10'),
        #     ('option b','B.$9.63 if throw of die is 1-9, $0.25 if throw of die is 10')
        #     ],
        choices=['Option A', 'Option B'],
        widget=widgets.RadioSelectHorizontal
    )
    bq10 = models.StringField(
        label="",
        # choices=[
        #     ('option a',"$5 if throw of die is 1-10"),
        #     ('option b',"$9.63 if throw of die is 1-10")
        #     ],
        choices=['Option A', 'Option B'],
        widget=widgets.RadioSelectHorizontal
    )
    ac1 = models.StringField(
        label="",
        # choices=['A.$5 if throw of die is 1, $4 if throw of die is 2-10','B.$9.63 if throw of die is 1, $0.25 if throw of die is 2-10'],
        choices=['Option A', 'Option B'],
        widget=widgets.RadioSelectHorizontal
    )
    ac2 = models.StringField(
        label="",
        # choices=['A.$5 if throw of die is 1-4, $4 if throw of die is 5-10','B.$9.63 if throw of die is 1-4, $0.25 if throw of die is 5-10'],
        choices=['Option A', 'Option B'],
        widget=widgets.RadioSelectHorizontal
    )
    ac3 = models.StringField(
        label="",
        # choices=['A.$5 if throw of die is 1-6, $4 if throw of die is 7-10', 'B.$9.63 if throw of die is 1-6, $0.25 if throw of die is 7-10'],
        choices = ['Option A', 'Option B'],
        widget=widgets.RadioSelectHorizontal
    )




# FUNCTIONS
def set_payoff_binary(player: Player):
    participant = player.participant
    round_number = player.round_number
    # 模拟掷骰子
    dice = random.randint(1, 10)
    player.dice2 = dice

    if player.bq2 == 'Option A':
        if dice == 1 or dice == 2:
            player.round_result = cu(5)
        else:
            player.round_result = cu(4)
    else:  # option b
        if dice == 1 or dice == 2:
            player.round_result = cu(9.63)
        else:
            player.round_result = cu(0.25)

    player.payoff_current = player.round_result

# def set_payoff_binary(player: Player):
#     participant = player.participant
#     round_number = player.round_number
#
#     # determine round_result as (potential) payoff per round
#     if player.bq2 == 'option a':
#         player.round_result = cu(4)
#     else:
#         player.round_result = cu(0.25)
#
#     player.payoff_current = player.round_result

def save_payoff_binary(player: Player):
    player.participant.payoff_binary = player.payoff_current

def save_choices(player: Player):
    player.participant.bq1 = player.bq1
    player.participant.bq2 = player.bq2
    player.participant.bq3 = player.bq3
    player.participant.bq4 = player.bq4
    player.participant.bq5 = player.bq5
    player.participant.bq6 = player.bq6
    player.participant.bq7 = player.bq7
    player.participant.bq8 = player.bq8
    player.participant.bq9 = player.bq9
    player.participant.bq10 = player.bq10
    player.participant.dice2 = player.dice2


# PAGES
class Introduction1(Page):
    form_model = 'player'
    form_fields = []
    @staticmethod
    def is_displayed(player: Player):
        if player.round_number == 1:
            player.participant.vars["failed_attention_check"] = False
            return True
        else:
            return player.participant.vars["failed_attention_check"]


class TenSideDie(Page):
    form_model = 'player'
    form_fields = []
    @staticmethod
    def is_displayed(player: Player):
        if player.round_number == 1:
            return True
        else:
            return player.participant.vars["failed_attention_check"]


class Introduction2(Page):
    form_model = 'player'
    form_fields = []
    @staticmethod
    def is_displayed(player: Player):
        if player.round_number == 1:
            return True
        else:
            return player.participant.vars["failed_attention_check"]


class Questions(Page):
    form_model = 'player'
    form_fields = ["bq1","bq2","bq3","bq4","bq5","bq6","bq7","bq8","bq9","bq10"]
    @staticmethod
    def is_displayed(player: Player):
        if player.round_number == 1:
            return True
        else:
            return player.participant.vars["failed_attention_check"]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_payoff_binary(player)
        save_payoff_binary(player)
        save_choices(player)


class AttentionCheck(Page):
    form_model = 'player'
    form_fields = ["ac1","ac2","ac3"]
    @staticmethod
    def is_displayed(player: Player):
        if player.round_number == 1:
            return True
        else:
            return player.participant.vars["failed_attention_check"]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.ac1 == C.ATTENTION_CHECK_1_CORRECT_ANSWER and player.ac2 == C.ATTENTION_CHECK_2_CORRECT_ANSWER and player.ac3 == C.ATTENTION_CHECK_3_CORRECT_ANSWER:
            player.participant.vars["failed_attention_check"] = False
        else:
            player.participant.vars["failed_attention_check"] = True


class FailedAttentionCheck(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.vars["failed_attention_check"]


class Results(Page):
    form_model = "player"
    form_fields = []
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number >= C.NUM_ATTENTION_CHECK_TRIES

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        return dict(
            payoff=player.participant.payoff_binary,
            player_choice= player.participant.bq2,
            player_dice2= player.participant.dice2
        )


page_sequence = [Introduction1, TenSideDie, Introduction2, Questions, AttentionCheck, FailedAttentionCheck, Results]
