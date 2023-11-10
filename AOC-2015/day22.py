# --- Day 22: Wizard Simulator 20XX ---

# Little Henry Case decides that defeating bosses with swords and stuff is
# boring. Now he's playing the game with a wizard. Of course, he gets stuck on
# another boss and needs your help again.

# In this version, combat still proceeds with the player and the boss taking
# alternating turns. The player still goes first. Now, however, you don't get
# any equipment; instead, you must choose one of your spells to cast. The first
# character at or below 0 hit points loses.

# Since you're a wizard, you don't get to wear armor, and you can't attack
# normally. However, since you do magic damage, your opponent's armor is
# ignored, and so the boss effectively has zero armor as well. As before, if
# armor (from a spell, in this case) would reduce damage below 1, it becomes 1
# instead - that is, the boss' attacks always deal at least 1 damage.

# On each of your turns, you must select one of your spells to cast. If you
# cannot afford to cast any spell, you lose. Spells cost mana; you start with
# 500 mana, but have no maximum limit. You must have enough mana to cast a
# spell, and its cost is immediately deducted when you cast it. Your spells are
# Magic Missile, Drain, Shield, Poison, and Recharge.

#     Magic Missile costs 53 mana. It instantly does 4 damage.

#     Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit
#     points.

#     Shield costs 113 mana. It starts an effect that lasts for 6 turns. While
#     it is active, your armor is increased by 7.

#     Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the
#     start of each turn while it is active, it deals the boss 3 damage.

#     Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At
#     the start of each turn while it is active, it gives you 101 new mana.

# Effects all work the same way. Effects apply at the start of both the player's
# turns and the boss' turns. Effects are created with a timer (the number of
# turns they last); at the start of each turn, after they apply any effect they
# have, their timer is decreased by one. If this decreases the timer to zero,
# the effect ends. You cannot cast a spell that would start an effect which is
# already active. However, effects can be started on the same turn they end.

# For example, suppose the player has 10 hit points and 250 mana, and that the
# boss has 13 hit points and 8 damage:

# -- Player turn --
# - Player has 10 hit points, 0 armor, 250 mana
# - Boss has 13 hit points
# Player casts Poison.

# -- Boss turn --
# - Player has 10 hit points, 0 armor, 77 mana
# - Boss has 13 hit points
# Poison deals 3 damage; its timer is now 5.
# Boss attacks for 8 damage.

# -- Player turn --
# - Player has 2 hit points, 0 armor, 77 mana
# - Boss has 10 hit points
# Poison deals 3 damage; its timer is now 4.
# Player casts Magic Missile, dealing 4 damage.

# -- Boss turn --
# - Player has 2 hit points, 0 armor, 24 mana
# - Boss has 3 hit points
# Poison deals 3 damage. This kills the boss, and the player wins.

# Now, suppose the same initial conditions, except that the boss has 14 hit
# points instead:

# -- Player turn --
# - Player has 10 hit points, 0 armor, 250 mana
# - Boss has 14 hit points
# Player casts Recharge.

# -- Boss turn --
# - Player has 10 hit points, 0 armor, 21 mana
# - Boss has 14 hit points
# Recharge provides 101 mana; its timer is now 4.
# Boss attacks for 8 damage!

# -- Player turn --
# - Player has 2 hit points, 0 armor, 122 mana
# - Boss has 14 hit points
# Recharge provides 101 mana; its timer is now 3.
# Player casts Shield, increasing armor by 7.

# -- Boss turn --
# - Player has 2 hit points, 7 armor, 110 mana
# - Boss has 14 hit points
# Shield's timer is now 5.
# Recharge provides 101 mana; its timer is now 2.
# Boss attacks for 8 - 7 = 1 damage!

# -- Player turn --
# - Player has 1 hit point, 7 armor, 211 mana
# - Boss has 14 hit points
# Shield's timer is now 4.
# Recharge provides 101 mana; its timer is now 1.
# Player casts Drain, dealing 2 damage, and healing 2 hit points.

# -- Boss turn --
# - Player has 3 hit points, 7 armor, 239 mana
# - Boss has 12 hit points
# Shield's timer is now 3.
# Recharge provides 101 mana; its timer is now 0.
# Recharge wears off.
# Boss attacks for 8 - 7 = 1 damage!

# -- Player turn --
# - Player has 2 hit points, 7 armor, 340 mana
# - Boss has 12 hit points
# Shield's timer is now 2.
# Player casts Poison.

# -- Boss turn --
# - Player has 2 hit points, 7 armor, 167 mana
# - Boss has 12 hit points
# Shield's timer is now 1.
# Poison deals 3 damage; its timer is now 5.
# Boss attacks for 8 - 7 = 1 damage!

# -- Player turn --
# - Player has 1 hit point, 7 armor, 167 mana
# - Boss has 9 hit points
# Shield's timer is now 0.
# Shield wears off, decreasing armor by 7.
# Poison deals 3 damage; its timer is now 4.
# Player casts Magic Missile, dealing 4 damage.

# -- Boss turn --
# - Player has 1 hit point, 0 armor, 114 mana
# - Boss has 2 hit points
# Poison deals 3 damage. This kills the boss, and the player wins.

# You start with 50 hit points and 500 mana points. The boss's actual stats are
# in your puzzle input. What is the least amount of mana you can spend and still
# win the fight? (Do not include mana recharge effects as "spending" negative
# mana.)

# --- Part Two ---

# On the next run through the game, you increase the difficulty to hard.

# At the start of each player turn (before any other effects apply), you lose 1
# hit point. If this brings you to or below 0 hit points, you lose.

# With the same starting stats for you and the boss, what is the least amount of
# mana you can spend and still win the fight?


# If I wanted to remove the debug prints, this code could be greatly simplified


import sys
import queue
import copy

DEBUG = False

def main( argv ):

    player = Player( 50, 0, 0, 500 )
    boss = Boss( 51, 0, 9, 0 )

    ##
    # Part 1
    ##

    print( f"Part 1 answer: {playGame( player, boss )}" )

    ##
    # Part 2
    ##

    print( f"Part 2 answer: {playGame( player, boss, hard=True )}" )

def playGame( player, boss, hard=False ):
    q = queue.Queue()

    for spell in Player.SPELLS:
        q.put( copy.deepcopy( [ player, boss, spell ] ) )

    lowestManaSpent = 1000000

    while not q.empty():
        # Get the turn parameters
        p, b, s = q.get()

        # Run the turn
        if not runPlayerTurn( p, b, s, hard ) or not runBossTurn( p, b ):
            # Check for player win.  If they did, track the mana.  If they didn't discard this path.
            if b.isAlive():
                continue # We lost
            else:
                lowestManaSpent = min( lowestManaSpent, p.manaSpent )

        else:
            # Check if we've exceeded the best mana spent so far.  If we have, discard this path.
            if p.manaSpent >= lowestManaSpent:
                continue

            # Finally, queue up another turn
            for spell in Player.SPELLS:
                q.put( copy.deepcopy( [ p, b, spell ] ) )

    return lowestManaSpent

def debugPrint( str ):
    if DEBUG:
        print( str )

def runPlayerTurn( player, boss, spell, hard ):
    debugPrint( "-- Player turn --" )
    debugPrint( player )
    debugPrint( boss )
    
    # Hard mode / Part 2
    if hard:
        player.hp -= 1
        
        if not player.isAlive():
            return False

    player.runEffects()
    boss.runEffects()

    # Boss can be dead at this point
    if not boss.isAlive():
        debugPrint( "Boss has died.  Player wins" )
        return False

    if not player.castSpell( spell, boss ):
        debugPrint( "Player has run out of mana.  Player loses" )
        return False

    # Boss can be dead at this point
    if not boss.isAlive():
        debugPrint( "Boss has died.  Player wins" )
        return False
    
    debugPrint( "" )
    
    return True

def runBossTurn( player, boss ):
    debugPrint( "-- Boss turn -- " )
    debugPrint( player )
    debugPrint( boss )
    player.runEffects()
    boss.runEffects()

    # Boss can be dead at this point
    if not boss.isAlive():
        debugPrint( "Boss has died.  Player wins" )
        return False
    
    #print( f"Boss attacks for {boss.dmg} damage." )
    player.attack( boss.dmg )

    # Player can be dead at this point
    if not player.isAlive():
        debugPrint( "Player has died.  Boss wins" )
        return False
    
    debugPrint( "" )
    
    return True


class Character:
    SPELLS = { "Magic Missile": 53, "Drain": 73, "Shield": 113, "Poison": 173, "Recharge": 229 }

    def __init__( self, hp, armor, dmg, mana ):
        self.hp = hp
        self.armor = armor
        self.dmg = dmg
        self.mana = mana

        self.activeEffects = []
        self.manaSpent = 0

    def isAlive( self ):
        return self.hp > 0
    
    def attack( self, dmg ):
        self.hp -= max( (dmg - self.armor), 1 )
        debugPrint( f"Boss attacks for {dmg} - {self.armor} = {max( (dmg - self.armor), 1 )} damage!" )

    # Returns True if we got the spell off, False if we were out of mana
    def castSpell( self, spell, tgt ):
        if self.mana - Player.SPELLS[ spell ] < 0:
            return False
        elif spell == "Magic Missile":
            tgt.hp -= 4
            debugPrint( "Player casts Magic Missle, dealing 4 damage" )
        elif spell == "Drain":
            tgt.hp -= 2
            self.hp += 2
            debugPrint( "Player casts Drain, dealing 2 damage, and healing for 2 hit points" )
        elif spell == "Shield":
            self.addEffect( spell, 6 )
        elif spell == "Poison":
            tgt.addEffect( spell, 6 )
            debugPrint( "Player casts Poison" )
        elif spell == "Recharge":
            self.addEffect( spell, 5 )
            debugPrint( "Player casts Recharge" )

        self.mana -= Player.SPELLS[ spell ]
        self.manaSpent += Player.SPELLS[ spell ]

        return True

    def addEffect( self, effect, duration ):
        # Don't allow multiples of same effect
        for e in self.activeEffects:
            if e[ 1 ] == effect:
                return
            
        self.activeEffects.append( [ duration, effect ] )

        # Sheild takes effect at apply time and drops off when timer reaches 0
        if effect == "Shield":
            self.armor += 7
            debugPrint( "Player casts Shield, increasing armor by 7." )

    def runEffects( self ):
        for effect in self.activeEffects:
            effect[ 0 ] -= 1  # Decrease timer

            if effect[ 1 ] == "Shield":
                debugPrint( f"Shield's timer is now {effect[ 0 ]}" )

                if not effect[ 0 ]:
                    self.armor -= 7  # Shield drops off when timer expires
                    debugPrint( "Shield wears off, decreasing armor by 7" )

            elif effect[ 1 ] == "Poison":
                self.hp -= 3
                debugPrint( f"Poison deals 3 damage; its timer is now {effect[ 0 ]}" )

            elif effect[ 1 ] == "Recharge":
                self.mana += 101
                debugPrint( f"Recharge provides 101 mana; its timer is now {effect[ 0 ]}" )

                if not effect[ 0 ]:
                    debugPrint( "Recharge wears off" )

        # Prune expired effects
        self.activeEffects = [ effect for effect in self.activeEffects if effect[ 0 ] ] 


class Player( Character ):
    def __str__( self ):
        return f"- Player has {self.hp} hit points, {self.armor} armor, {self.mana} mana"
     

class Boss( Character ):
    def __str__( self ):
        return f"- Boss has {self.hp} hit points"

if __name__ == "__main__":
    main( argv=sys.argv )
