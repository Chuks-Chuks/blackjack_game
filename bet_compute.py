class Stake:
    def __init__(self, total_amount, amount_staked):
        self.total_amount = total_amount
        self.amount_staked = amount_staked

    def stake_compute(self, boolean_return_for_score_value):
        if boolean_return_for_score_value:
            total = self.total_amount + self.amount_staked
        elif not boolean_return_for_score_value:
            total = self.total_amount - self.amount_staked
        else:
            total = self.total_amount
        return total
