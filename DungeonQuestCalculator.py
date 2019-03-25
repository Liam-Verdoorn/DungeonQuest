weapons = {
    'Soulstealer Greatsword': {
        'base_damage': 3599,
        'max_upgrades': 338
    }
}

def getWeaponDamage(item: str, levels: int = 1):
    """ Calculate weapon damage at set specific level.
    """
    _baseDamage: int = weapons[item]['base_damage']
    _maxUpgrades: int = weapons[item]['max_upgrades']
    return round(_baseDamage+(10*levels))

def upgradeCost(levels: int = 1):
    """ Calculate the cost to upgrade an item per level.
    """
    return round(100*(1.0618*levels))

# no
# well 100 * 1.0618 = 106.18
# what section
# 100+(1,0618*levels)) did you just delete an entire section the upgradecost one what does the line mean?
#oh okay good
print(getWeaponDamage('Soulstealer Greatsword', 113))
print(upgradeCost(10))
