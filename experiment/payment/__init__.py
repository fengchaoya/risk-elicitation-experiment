from otree.api import *
import random

doc = """
Generate the total payment of the participants.
"""


class C(BaseConstants):
    NAME_IN_URL = 'payment'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    selected_part = models.StringField()# 记录被选中的部分
    bonus = models.CurrencyField()  # 最终支付金额
    payoff_pay = models.CurrencyField()


def set_payoff_final(player: Player):
    # 直接从participant获取数据
    payoff_binary = player.participant.payoff_binary
    payoff_bret = player.participant.payoff_bret

    # 随机选择支付部分
    if random.random() < 0.5:
        player.selected_part = 'binary'
        player.bonus = payoff_binary
    else:
        player.selected_part = 'multi'
        player.bonus = payoff_bret

    # 设置最终支付
    player.payoff_pay = player.bonus + cu(2)

def save_payoff_final(player: Player):
    player.participant.payoff = player.payoff_pay
    player.participant.payoff_total = player.payoff_pay


# PAGES
class Finished(Page):
    form_model = "player"
    form_fields = []
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_payoff_final(player)
        save_payoff_final(player)

class PaymentPage(Page):
    form_model = "player"
    form_fields = []

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            payoff_binary=player.participant.payoff_binary,
            payoff_bret=player.participant.payoff_bret,
            selected_part=player.selected_part,
            bonus=player.bonus,
            total_payoff=player.participant.payoff_total,
        )




page_sequence = [Finished, PaymentPage]
