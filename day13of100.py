def buy_health(self, health, coins):
    if coins >= 5 and health < 100:
        buy_more = input(f'{self.name}, you have been wounded in battle. Would you like to purchase a healing potion? ')
        if buy_more == 'no':
            print(f'You have decided to continue with {self.health}.')
        elif buy_more == 'yes':
            how_many = input(f'Enter the number of potions? ')
            if self.money / int(how_many) < 0:
                print(f'AH! {self.name}, you do not have enough coins!')
            else:
                potions = int(how_many) * self.money
                self.money = coins - potions
                self.health = potions + health
                print(f'Power up to restore health...\n')
                print(f'{self.name}, your health is restored to {self.health}.\n You have {self.money} remaining.')


