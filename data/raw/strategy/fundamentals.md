# Magic: The Gathering Strategy Fundamentals

This document teaches the reasoning frameworks and strategic concepts needed to analyze Magic: The Gathering gameplay. It covers *how to think* about the game, not specific card interactions or current metagame facts.

---

## 1. Resources

Magic revolves around four core resources. Understanding their baseline values and how they interact is fundamental to all strategic decisions.

### 1.1 Cards (Hand Size)

**Baseline value**: Positive. More cards in hand means more options.

Each card represents a potential action. A player with five cards has more choices than a player with two. Drawing cards or forcing opponents to discard creates *card advantage* - having more resources than your opponent.

**Value inversion**: Effects that punish card count (damage per card, discard costs) can make a smaller hand preferable. In these situations, the normal "more cards = good" rule flips.

### 1.2 Mana

**Baseline value**: Positive. More available mana means more possible plays per turn.

Mana enables action. A player with five lands can deploy more threats or hold up more responses than a player with two. Mana advantage comes from:
- Playing more lands
- Mana-producing creatures or artifacts
- Cost reduction effects

**Mana efficiency**: Spending mana effectively each turn is often more important than raw mana count. An unspent mana is a wasted resource.

**Mana screw**: Drawing too few lands, leaving you unable to cast spells in your hand. A player with three-cost spells stuck on two lands is "mana screwed." This cripples your ability to execute any game plan.

**Mana flood**: Drawing too many lands, leaving you with mana but nothing to spend it on. A player with seven lands but only one spell in hand is "flooded." Excess mana without cards to cast provides no advantage.

**Mana sinks**: Cards or abilities that let you spend excess mana productively. Examples include activated abilities (pay 3: draw a card) or X-cost spells. Mana sinks help convert flood into value.

**Value inversion**: Late-game land draws are often less valuable than spell draws. A deck that minimizes flood/screw variance through card selection or mana sinks gains consistency.

### 1.3 Life Total

**Baseline value**: Positive, but contextual. Life is a resource to spend, not just a score to protect.

The only life point that truly matters is your last one. Going from 20 to 17 rarely affects the game. Going from 3 to 0 ends it.

**Life as currency**: Paying life for cards, mana, or other effects is often correct. Cards like Necropotence and Ad Nauseam are powerful because they trade a weaker resource (life) for a stronger one (cards).

**Burn**: A strategy (or deck archetype) focused on dealing direct damage to the opponent through spells like Lightning Bolt. Burn decks aim to reduce the opponent from 20 to 0 using mostly non-creature damage sources.

**Reach** (strategic term): The ability to deal damage directly to the opponent, bypassing blockers. "The opponent has reach" means they can finish you with burn spells or direct damage even if you stabilize the board. (Note: This differs from the keyword "reach" which lets creatures block flyers.)

**Damage race**: A game state where both players are trying to kill each other as fast as possible, ignoring defense. In a race, every point of life matters because whoever deals 20 first wins.

**Value thresholds**: Certain life totals become dangerous based on opponent's deck:
- Against burn: staying above 3 avoids Lightning Bolt kills
- Against aggro with haste: staying above 5-6 provides buffer
- In damage races: every point matters earlier

**Value inversion**: When your opponent has effects that punish high life totals, or when you need to enable your own "low life matters" cards.

### 1.4 Board State (Permanents)

**Baseline value**: Positive. More permanents generally means more options and more power.

Creatures can attack and block. Artifacts and enchantments provide ongoing effects. Planeswalkers generate value over time. A developed board represents accumulated investment.

**Board presence vs hand size**: These resources trade off. Deploying cards builds your board but shrinks your hand. Holding cards preserves options but leaves mana unspent.

**Board sweeper** (also called "wrath effect" or "mass removal"): A spell that destroys all creatures at once, like Wrath of God. Sweepers punish players who overcommit to the board.

**Value inversion**: Against board sweepers, overcommitting to the board is risky. Sometimes holding back resources is correct - deploy just enough threats to pressure, keeping reserves in hand.

---

## 2. Resource Valuation Framework

Before evaluating synergies or making strategic decisions, you must understand what is generally "good" and "bad" for each player.

### 2.1 What Is Good For You

- Cards in hand (options)
- Creatures on your battlefield (can attack, block, use abilities)
- Life total above dangerous thresholds
- Mana available to cast spells
- Opponent's resources diminishing

### 2.2 What Is Bad For You

- Empty hand ("topdeck mode" - your entire game depends on whatever you draw next, with no backup options)
- Empty or weak board (can't pressure opponent, vulnerable to attacks)
- Low life total (limits your plays, enables opponent's reach)
- Mana screw (too few lands to cast your spells)
- Mana flood (too many lands, not enough spells to cast)
- Opponent accumulating resources faster than you

### 2.3 Tradeoff Evaluation

Most cards involve trading one resource for another. Evaluate by asking:
- What am I giving up?
- What am I getting?
- In the current game state, which resource matters more?

**Example**: A 4/4 creature that deals 1 damage to you each turn. The body (board presence, 4 damage per attack) outweighs the cost (1 life per turn). This is a favorable tradeoff in most situations.

**Example**: An effect that deals 2 damage to you per card in hand. Normally more cards = good, but now optimal hand size might be 2-3 cards. Context inverts the baseline value.

### 2.4 Resource Conversion

Strong plays often convert weaker resources into stronger ones:
- Life into cards (generally favorable)
- Cards into tempo/board presence (context-dependent)
- Mana into cards (card draw spells)
- Board presence into cards (sacrifice effects with draw)

---

## 3. Card Advantage

Card advantage is the concept that whoever has more resources - cards in hand plus meaningful permanents in play - has the advantage.

### 3.1 Basic Card Advantage

**One-for-one**: Trading one card for one card. Neither player gains advantage.
- Example: Using Murder to kill opponent's creature.

**Two-for-one**: Using one card to deal with two of opponent's cards. You gain advantage.
- Example: Wrath of God killing three creatures costs you one card, costs opponent three cards.
- Example: Divination draws two cards for one card spent.

### 3.2 Virtual Card Advantage

Virtual card advantage occurs when you make opponent's cards irrelevant without destroying them.

**Example**: Playing Teferi's Moat against a green creature deck. Their creatures can't attack. You haven't destroyed them, but you've neutralized them with one card. Those creatures are now "virtually" gone.

**Dead cards**: Cards in hand that cannot be usefully cast in the current game state. A creature removal spell against a creatureless deck is a dead card - it occupies space in your hand but provides no value.

**Example**: Playing a creature with protection from red against a mono-red deck. Their burn spells targeting creatures become dead cards.

### 3.3 Card Quality vs Card Quantity

Not all cards are equal in every situation. A card that's perfect for the current board state is worth more than two cards that don't help.

Early game: lands are valuable (enable plays)
Late game: spells are valuable (lands often don't help)

Well-constructed decks manage this through mana curves and card selection.

---

## 4. Tempo

Tempo represents speed and mana efficiency - accomplishing your strategy faster than your opponent.

### 4.1 Tempo vs Card Advantage

These concepts often oppose each other:

**Stabilize**: The moment a defensive player stops the bleeding - they've answered the immediate threats, their life total is no longer dropping, and they can begin executing their own game plan. Control decks aim to stabilize before deploying their win conditions.

**Tempo-focused play**: Deploy threats quickly, pressure opponent, win before they stabilize. May sacrifice card advantage for speed.

**Card advantage-focused play**: Accumulate resources, answer threats efficiently, win through superior options. May sacrifice tempo for value.

**The fundamental tension**: "It is difficult to make a deck that wins both via card and time advantage."

### 4.2 Tempo Gains and Losses

**Bounce**: Returning a permanent to its owner's hand. Bounce spells don't destroy the threat permanently, but they cost the opponent tempo - they must spend mana to replay it.

**Gaining tempo**:
- Removing a threat while developing your own (two-for-one in mana terms)
- Bouncing an opponent's creature they spent mana on (they lose the mana invested)
- Playing efficient threats (high power for low mana cost)

**Losing tempo**:
- Spending mana on cards that don't affect the board
- Having your threat removed after investing mana
- Missing land drops

### 4.3 The Fundamental Turn

The "Fundamental Turn" is the turn when a deck's strategy becomes dominant - when it "wins" if uninterrupted.

**For aggro**: The turn it can deal lethal damage
**For control**: The turn it stabilizes and begins generating insurmountable advantage
**For combo**: The turn it assembles its winning combination

**Strategic implication**: Your deck's fundamental turn must be competitive with the format's average. If most decks win by turn 4-5, a deck that can't interact until turn 6 is poorly positioned.

### 4.4 Mana Economy in Trades

When your cheap card deals with their expensive card, you gain tempo advantage equal to the mana difference. A 2-mana Murder killing a 5-mana creature nets you 3 mana of tempo - you spent less and can redeploy faster than they can.

**Trading up**: A creature that kills something more expensive than itself creates mana advantage. A 1-mana 1/1 deathtouch trading with a 5-mana 5/5 is card-neutral (one-for-one) but a massive tempo swing - you're up 4 mana worth of resources.

**Trading down**: Conversely, using expensive removal on cheap threats loses tempo. Spending a 4-mana sweeper to kill one 2-mana creature is inefficient - you'd rather answer cheap threats cheaply and save expensive answers for expensive problems.

**Forced inefficiency**: Some threats demand answers regardless of mana efficiency. A 2-mana creature that must be killed or you lose the game is worth spending 4 mana on. Recognize when efficiency matters and when survival matters more.

---

## 5. Archetypes

Decks cluster into strategic archetypes based on their game plan.

### 5.1 Aggro

**Combat tricks**: Instant-speed spells that modify creatures during combat, such as +3/+3 effects or granting abilities. Combat tricks create surprise advantages in combat - your 2/2 suddenly beats their 3/3.

**Goal**: Kill the opponent as quickly as possible.
**Resource priority**: Tempo over card advantage.
**Typical cards**: Efficient creatures, burn spells, combat tricks.
**Wins by**: Overwhelming opponent before they can stabilize.
**Loses to**: Falling behind on board, opponent stabilizing with lifegain or sweepers.

### 5.2 Control

**Goal**: Survive the early game, then win through card advantage.
**Resource priority**: Card advantage over tempo.
**Typical cards**: Removal, counterspells, card draw, few but powerful win conditions.
**Wins by**: Answering all threats, then deploying an unanswerable threat.
**Loses to**: Being overwhelmed before stabilizing, running out of answers.

### 5.3 Midrange

**Goal**: Play versatile threats and answers, adapting to the opponent.
**Resource priority**: Balances tempo and card advantage.
**Typical cards**: Efficient creatures with abilities, versatile removal, some card advantage.
**Wins by**: Out-valuing aggro, out-tempoing control.
**Loses to**: Being too slow against aggro, too fair against combo.

### 5.4 Combo

**Tutors**: Cards that search your library for specific cards. Named after Demonic Tutor, these effects increase consistency by letting you find exactly what you need. Combo decks use tutors to assemble their pieces faster.

**Goal**: Assemble a specific combination of cards that wins the game.
**Resource priority**: Speed to combo, protection for combo pieces.
**Typical cards**: Combo pieces, tutors, card draw, sometimes protection.
**Wins by**: Executing the combo before opponent can disrupt it.
**Loses to**: Disruption (discard, counterspells), being killed before combo assembles.

### 5.5 Tempo (as archetype)

**Goal**: Establish an early threat, then protect it while disrupting opponent.
**Resource priority**: Efficient mana usage, converting tempo into damage.
**Typical cards**: Cheap threats, counterspells, bounce spells.
**Wins by**: Landing a threat, then countering/bouncing everything opponent does.
**Loses to**: Resolved threats it can't answer, running out of disruption.

---

## 6. Role Assignment: Who's the Beatdown?

"The most common (yet subtle, yet disastrous) mistake I see in tournament Magic is the misassignment of who is the beatdown deck and who is the control deck in a similar deck vs. similar deck matchup."
— Mike Flores

### 6.1 The Core Principle

In any matchup, one player should be the **beatdown** (aggressor) and one should be the **control** (defender). Misidentifying your role often leads to losing.

**Beatdown's job**: Kill the opponent faster than they can kill you.
**Control's job**: Survive, establish card advantage, then win at leisure.

### 6.2 Determining Your Role

**Permission**: A control strategy built around counterspells - you give the opponent "permission" to resolve their spells (by not countering) or deny permission (by countering). Permission decks control what enters the battlefield.

Three factors determine who should be beatdown:

1. **Damage capacity**: More damage-oriented cards = beatdown role
2. **Removal quantity**: More answers = control role
3. **Card advantage/permission**: More counterspells and draw = control role

### 6.3 Role Fluidity

Your deck's "natural" archetype doesn't always determine your role.

**Example**: An aggro deck facing a faster aggro deck may need to play control - blocking, trading, surviving until the opponent runs out of gas.

**Inevitability**: The concept of who wins if the game goes very long with no decisive action. A deck with inevitability has an endgame advantage - perhaps an unbeatable threat, a combo, or simply better card quality. The player without inevitability must act as beatdown before this advantage materializes.

**Gas**: Slang for threats, action cards, or resources that advance your game plan. "Running out of gas" means you've depleted your hand of useful cards and are now in topdeck mode, hoping to draw something relevant.

**Example**: A control deck facing a slower control deck may need to be the beatdown - applying pressure before the opponent establishes inevitability.

### 6.4 Misassignment = Game Loss

If you're the beatdown but play defensively, you give the opponent time to establish advantage.

If you're the control but play aggressively, you walk into the opponent's game plan and waste resources.

**Sideboard**: A set of 15 cards kept separate from your main deck. Between games in a match, you may swap cards between your main deck and sideboard. Sideboards contain specialized answers for specific matchups - cards too narrow for the main deck but powerful against certain strategies.

**Sideboarding**: The process of modifying your deck between games using your sideboard. Good sideboarding means knowing which cards underperform in each matchup and which sideboard cards address your opponent's strategy.

**Key insight**: Determine your role before sideboarding. Remove cards that don't serve your assigned role; add cards that reinforce it.

---

## 7. Combat Fundamentals

Combat is where games are won and lost. Mastering attacking and blocking decisions is essential.

### 7.1 Use Your Creatures

A creature that neither attacks nor blocks provides no value that turn. Passivity is often as bad as recklessness.

**Default heuristic**: If it's safe to attack and you don't intend to block, attack. If you can block without disaster, block.

### 7.2 Trading

When similar creatures face off:
- Usually attack if you can
- Usually block if you can

**Why attack**: The opponent might not block (free damage). If they do block, the trade happens on your terms. Waiting gives opponent time for things to go wrong for you.

**Why block**: You make an even trade while saving life. Not blocking lets them attack back, possibly with a combat trick.

**Be willing to trade creatures.** Trying to avoid trades often leads to taking extra damage or letting opponent leverage their creatures better.

### 7.3 Exceptions to Trading

Don't trade when:
- Setting up for a big turn (Overrun effects)
- Building critical mass (devotion, tribal synergies, convoke)
- The creature has a job outside combat

But achieve your goals quickly - avoiding trades for too long lets opponent pressure you.

### 7.4 Managing Life Total

**Early game**: Life matters less. Taking 3 damage to save a creature is often correct.

**Late game**: Life matters more. Your last points are precious.

**Think ahead**: If opponent has Lightning Bolt, avoid going to 3. If opponent has haste creatures, avoid going to 5-6. Identify when you'll need to start blocking conservatively.

### 7.5 Chump Blocking

Throwing away a creature to save life (chump blocking) is a last resort.

**Don't chump**: Going from 20 to 17.
**Must chump**: Going from 3 to 0.

**The middle ground**: Once you identify you'll have to chump eventually, do it while you can - before opponent removes your option with removal spells.

---

## 8. The Danger of Cool Things

"We can get so wrapped up in the cool things our deck can do that we lose objectivity."
— Chad Ellis

### 8.1 The Problem

Players often lose games because they pursue impressive plays instead of winning plays.

### 8.2 Winning Over Style

Before "improving" your line of play with something flashy:
- Verify the original plan still works
- Consider what opponent can do to disrupt you
- Evaluate whether the alternative offers better win percentage

**Don't get greedy.** If you can win the game, win the game. Don't delay victory for a more spectacular finish.

### 8.3 Card Attachment

Beware of keeping cards in your deck because they won "that one game." Evaluate cards based on their overall performance, not memorable exceptions.

---

## 9. Mana Base Construction

A functional mana base is the foundation of any deck.

### 9.1 Land Count by Strategy

| Strategy | Land Count |
|----------|------------|
| Aggressive (low curve) | 18-22 |
| Midrange | 23-25 |
| Control (high curve) | 25-27 |
| Land-focused | 28+ |

**Baseline**: 24 lands for an unknown or average deck.

### 9.2 Non-Land Mana Sources

For every two non-land mana sources (mana creatures, artifacts), reduce land count by one. But remember you need mana to cast these sources initially.

### 9.3 Color Ratios

Match your land mix to your spell requirements. If your deck has twice as many red spells as black spells, use approximately a 2:1 ratio of red sources to black sources.

### 9.4 Double-Cost Considerations

Spells requiring multiple colored mana (like 1UU or 2BB) need extra dedicated sources. Count these as 1.5 spells when calculating color ratios.

In multicolor decks, minimize double-cost spells to reduce mana problems.

---

## 10. Linear Strategies

A linear strategy focuses entirely on one goal, with every card contributing to that plan.

### 10.1 Characteristics

- Single-minded focus
- Little interest in interacting with opponent
- Cards that are weak individually but powerful together
- "Not interested in playing a fair game of Magic"

**Critical mass**: The threshold at which a synergy-based strategy becomes powerful. A deck with 5 artifacts might have weak artifact synergies, but a deck with 20 artifacts reaches "critical mass" where artifact payoffs become devastating. Linear strategies need to reach critical mass to function.

### 10.2 Advantages

- Explosive potential
- Can overwhelm unprepared opponents
- Critical mass makes individual cards exponentially more powerful

### 10.3 Disadvantages

- Lack of flexibility
- Vulnerable to targeted disruption
- Individual cards weak in isolation
- Sideboard hate can be devastating

**Sideboard hate**: Narrow but powerful cards designed to shut down specific strategies. Examples: graveyard hate (cards that exile graveyards) against graveyard decks, artifact destruction against artifact decks. Linear strategies are especially vulnerable because one hate card can invalidate their entire game plan.

### 10.4 Playing Against Linear Strategies

Prevent them from reaching critical mass. Disruption and removal are key. You often don't need to "win" - just stop their plan long enough to execute yours.

---

## Sources

This document synthesizes concepts from foundational Magic strategy articles including:
- "Who's the Beatdown?" by Mike Flores
- "Tempo and Card Advantage" by Eric Taylor
- "The Danger of Cool Things" by Chad Ellis
- "Clear the Land and the Fundamental Turn" by Zvi Mowshowitz
- "Mmmmmmmmmana" by Jay Moldenhauer-Salazar
- "Level One" series by Reid Duke
- "The Ins and Outs of Combat" by Reid Duke
