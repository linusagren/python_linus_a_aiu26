class OldCoinStash:
    def __init__(self, owner):
        self.owner = owner

        self._riksdaler = 0
        self._skilling = 0

    def deposit(self, riksdaler=0, skilling=0):
        if riksdaler < 0 or skilling < 0:
            raise ValueError(
                f"give positive riksdaler and positive skilling not {riksdaler} riksdaler, {skilling} skilling"
            )
            # more error handling

        self._riksdaler += riksdaler
        self._skilling += skilling

    def withdraw(self, riksdaler=0, skilling=0):
        if riksdaler > self._riksdaler or skilling > self._skilling:
            raise ValueError("Can't withdraw more than you have")
        self._riksdaler -= riksdaler
        self._skilling -= skilling

    def check_balance(self):
        print(
            f"Coins in stash: {self._riksdaler} riksdaler and {self._skilling} skillingar"
        )

    def __repr__(self):
        return f"OldCoinStash(owner='{self.owner}')"


stash1 = OldCoinStash("Ragnar")
stash1.check_balance()

try:
    stash1.deposit(riksdaler=5, skilling=-6)
except ValueError as err:
    print(err)

stash1.deposit(3,6)
stash1.check_balance()

stash1.withdraw(2,2)
stash1.check_balance()

stash1