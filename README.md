# Repeated Play Prisoner's Dillema
Lab #1 for CS 670: Repeated Play Prisoner's Dillema


## Purposes:
The purposes of this lab are:
- To let you play with ideas from game theory.
- To teach you about how repeated play games differ from the normal game theory context.
- To let you think about developing a utility-based strategic agent for a competitive environment.

## What you should learn:
When you complete this lab, you should understand the following:
- Why the tit-for-tat strategy is such a good idea.
- Where game theoretic assumptions fail in repeated games.
- The issues involved in designing a competitive agent (such as inter-agent modeling, anticipation, forgiveness, commitment, etc.).
You should also gain practice writing technical documents.  Check out the grading guidelines at the bottom of the description.

##  Description:
You will conduct a tournament that tests how different strategies perform in repeated-play prisoner's dilemma game.  You will create your own strategy, and play against the following agents:

- [x] **1.** An agent who employs the one-shot equilibrium solution (always defect)
- [x] **2.** An agent who chooses randomly
- [x] **3.** An agent who always cooperates with you (and never confesses)
- [x] **4.** An agent who employs the tit-for-tat strategy (reviewed below), and
- [ ] **5.** An agent who employs the tit-for-two-tats strategy (also reviewed below).
- [x] **6.** An agent who uses the Pavlov strategy (reviewed below).
- [ ] **7.** An agent who uses the Win-Stay/Lose-Shift strategy (reviewed below).
- [ ] **8.** An agent who uses the Never Forgive strategy (reviewed below).

You should try out how well each strategy works when there are 5 trials, 100 trials, and 200 trials.  You should also play a variant where, after each interaction, you flip a biased coin to decide if you continue to another round; the coin turns up heads p percent of the time, and whenever the coin turns up heads you continue.  Conduct the experiment for p = 0.75, 0.99, and 0.9. Each agent will compete against all other agents, and the total scores will be recorded.  You should use the prisoner's dilemma payoff matrix in ordinal form with 5 the most preferred outcome and 1 the least preferred.

| P1/P2           | Cooperate 2 | Defect 2 |
| --------------- | ----------- | -------- |
| **Cooperate 1** | (3,3)       | (1,5)    |
| **Defect 1**    | (5,1)       | (2,2)    |

> In the payoff matrix, cooperate means cooperating with the other prisoner by remaining silent, and defect means defecting from the team strategy by confessing to the police.  If you play the game 100 trials, your score is the sum of all of the payoffs you received so, for example,  if you and your opponent each cooperated, then your score would be 3*100.  High scores win.

## Strategies Review:
### Tit-for-Tat
In the **_tit-for-tat strategy_**, the agent begins by cooperating, and then plays whatever strategy the other agent played.  For example, let P1 be an arbitrary agent and let P2 be the tit-for-tat agent.  Then a sequence of choices might be something like:

|   | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
|P1 | D | C | C | D | D |
|TfT| C | D | C | C | D |

> Notice how P2 started off cooperating, and then just copies the previous choice by P1.

### Tit-for-Two-Tats
The **_tit-for-two-tats_** strategy is similar, except that P2 only defects if the other agent defects twice in a row, but cooperates immediately after the other agent cooperates.  So, if I let the sequence (A1,A2) represent the past two choices from the other agent, then Tf2T plays the following strategy:

| Their Sequence | My Response |
| --- | --- |
| (C,C) | C |
| (C,D) | C |
| (D,C) | C |
| (D,D) | D |

Thus, the following example represents a proper response for a Tf2T agent:

| |  0 |  1 |  2 |  3 |  4 |  5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| P1 | D | C | C |  D | D | C | C | C | 
| Tf2T | C | C | C |  C | C |  D | C | C |  


### Pavlov
The **_Pavlov_** strategy begins by cooperating.  On subsequent turns, whenever the two agents didn't agree on the previous last play then the Pavlov agent defects; otherwise, the Pavlov agent cooperates.   So, if I let the pair <A,B> represent the choices that the two players made on the last round, then Pavlov plays the following strategy:

| <Your last choice,My last choice> | My Response |
| --- | --- |
| <C,C> | C |
| <C,D> | D |
| <D,C> | D |
| <D,D> | C |

> This says that if we cooperated last time then I'll cooperate this time.  If we both defected, I'll take a chance that you might want to cooperate this time.  If you defected and I cooperated, I'll defect next time.  And if you cooperated and I defected, I'll try to get away with defecting again this time. 

An example sequence of how Pavlov would play against a made-up agent is shown below:

|   | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
|P1 | D | D | C | D | D | D |
|Pav| C | D | C | C | D | C |

### WSLS
The **_WinStay/LoseShift (WSLS)_** strategy begins by cooperating, but then changes its behavior (C goes to D or D goes to C) whenever the agent doesn't win.  Winning occurs whenever the agent gets either its most preferred or next most preferred result.  For example, let P1 be an arbitrary agent and let P2 be the WSLS agent.  Then a sequence of choices might be something like:

|    | 0 | 1 | 2 | 3 | 4 | 5 |
|--- |---|---|---|---|---|---|
|P1  | D | D | C | C | D | D |
|WSLS| C | D | C | C | C | D |

> Whenever WSLS wins (CC or CD --- where P1's choice is listed first and P2's choice is listed second), the WSLS agent replays its choice (C or D, respectively); i.e., it stays with the choice.  Whenever WSLS loses (DC or DD), the WSLS agent changes its choice (D or C, respectively); i.e., it shifts its choice.

## What you should turn in:
When you are done, you should turn in:
- One page describing and justifying your strategy.
- A description of the results for each number of trials listed above (5, 100, and 200); since this is a data intensive lab, take some time to present the information in an intelligible format.
- A description of the results for each of the probabilities above (0.75, 0.9, and 0.99); since this is a data intensive lab, take some time to present the information in an intelligible format.
- One page explaining why the winner won, and discussing how their strategy performed and why.
 

# Grading Rubric
Your report will be graded on four criteria: style, grammar, analysis, content.

**Style:** Is there an adequate introduction? Does the conclusions section make conclusions justified by the data? Is there a logical flow to the organization of the paper?

**Grammar:** Is the language adequate?

**Analysis:** Does the report present not only what is found but why? Have you made conclusions that are not justified? Do you include multiple trials to account for uncertainty? Have you reported both means and variances of data?

**Content:** Have you completed what was assigned? Is there some originality in the work?
