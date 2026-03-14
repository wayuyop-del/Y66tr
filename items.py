def use_coke(player):

    if player.coke>0:

        player.speed_timer = 75*60

        player.coke -=1


def use_shield(player):

    if player.shield>0:

        player.shield_timer = 5*60

        player.shield -=1
