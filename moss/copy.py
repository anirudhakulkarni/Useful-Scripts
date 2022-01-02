 "*** YOUR CODE HERE ***"
# strategy 1:
# if the ghost is scared, then we want to go to the ghost
# if the ghost is not scared, then we want to go to the closest food
# if the ghost is not scared, then we want to go to the closest ghost

ghost_score = 0
# score due to food
if successorGameState.isWin():
    return 1e11
if successorGameState.isLose():
    ghost_score-=1e11
maxscore = 0
minsofar = 1e10
maxsofar = -1e10
if len(newFood.asList()) == 0:
    minsofar = 0
    maxsofar = 0
for food in newFood.asList():
    minsofar = min(minsofar, manhattanDistance(newPos, food))
for food1 in newFood.asList():
    for food2 in newFood.asList():
        maxsofar = max(maxsofar, manhattanDistance(food1, food2))
food_score = -minsofar-10*len(newFood.asList())-maxsofar
# score due to ghost

if len(newGhostStates)==0:
    return 
for ghost in newGhostStates:
    if ghost.scaredTimer > 0:
        # scared ghost
        if manhattanDistance(newPos, ghost.getPosition()) < 2:
            return ghost_score+1e9
        else:
            ghost_score += q_param / \
                manhattanDistance(newPos, ghost.getPosition())

    else:
        if manhattanDistance(newPos, ghost.getPosition()) < 2:
            ghost_score -= 1e10
        else:
            ghost_score -= q_param / \
                manhattanDistance(newPos, ghost.getPosition())
# print(food_distance, ghost_score)
# score due to capsules

capsules = successorGameState.getCapsules()
capsuleScore = 0
capsule_minsofar = 1e10
if len(capsules) == 0:
    capsule_minsofar = 0
for capsule in capsules:
    capsule_minsofar = min(
        capsule_minsofar, manhattanDistance(newPos, capsule))
capsuleScore = -capsule_minsofar-10*len(capsules)
return food_score+ghost_score+capsuleScore
        print(successorGameState.getScore())

        # end strategy 1

        return successorGameState.getScore()

def minimax(curr_agentIndex, game_state, depth):
            val_action = None
            if (self.depth == depth) or game_state.isWin() or game_state.isLose() or (not game_state.getLegalActions(curr_agentIndex)):
                return self.evaluationFunction(game_state), 0

            if curr_agentIndex == game_state.getNumAgents()-1:
                depth += 1
                next_agentIndex = 0
            else:
                next_agentIndex = curr_agentIndex+1

            for action in game_state.getLegalActions(curr_agentIndex):
                next_value = minimax(next_agentIndex, game_state.generateSuccessor(
                    curr_agentIndex, action), depth)
                if not val_action:
                    val_action = (next_value[0], action)
                else:
                    prev_value = val_action[0]
                    if curr_agentIndex == 0:
                        if next_value[0] > prev_value:
                            val_action = (next_value[0], action)
                    else:
                        if next_value[0] < prev_value:
                            val_action = (next_value[0], action)
            return val_action
        final_val_action = minimax(0, gameState, 0)
        return final_val_action[1]
        # util.raiseNotDefined()

def alpha_beta(curr_agentIndex, game_state, depth, min_val, max_val):
            val_action = None
            if (self.depth == depth) or game_state.isWin() or game_state.isLose() or (not game_state.getLegalActions(curr_agentIndex)):
                return self.evaluationFunction(game_state), 0

            if curr_agentIndex == game_state.getNumAgents()-1:
                depth += 1
                next_agentIndex = 0
            else:
                next_agentIndex = curr_agentIndex+1

            for action in game_state.getLegalActions(curr_agentIndex):
                if not val_action:
                    next_value = alpha_beta(next_agentIndex, game_state.generateSuccessor(
                        curr_agentIndex, action), depth, min_val, max_val)
                    val_action = (next_value[0], action)
                    # next_min_val = val_action[0]
                    # next_max_val = val_action[0]
                    if curr_agentIndex == 0:
                        max_val = max(max_val, val_action[0])
                    else:
                        min_val = min(min_val, val_action[0])
                else:
                    if curr_agentIndex == 0 and val_action[0] > min_val:
                        return val_action
                    # if curr_agentIndex != 0:
                    #    if curr_agentIndex == game_state.getNumAgents()-1 and val_action[0] < max_val:
                    #        return val_action
                    if curr_agentIndex != 0 and val_action[0] < max_val:
                        return val_action
                    next_value = alpha_beta(next_agentIndex, game_state.generateSuccessor(
                        curr_agentIndex, action), depth, min_val, max_val)
                    prev_value = val_action[0]
                    if curr_agentIndex == 0:
                        if next_value[0] > prev_value:
                            val_action = (next_value[0], action)
                        max_val = max(max_val, val_action[0])
                    else:
                        if next_value[0] < prev_value:
                            val_action = (next_value[0], action)
                        min_val = min(min_val, val_action[0])
            return val_action

        final_val_action = alpha_beta(
            0, gameState, 0, float('inf'), float('-inf'))
        # print(final_val_action[0])
        return final_val_action[1]
        # util.raiseNotDefined()
def exptmax(curr_agentIndex, game_state, depth):
            val_action = None
            if (self.depth == depth) or game_state.isWin() or game_state.isLose() or (not game_state.getLegalActions(curr_agentIndex)):
                return self.evaluationFunction(game_state), 0

            if curr_agentIndex == game_state.getNumAgents()-1:
                depth += 1
                next_agentIndex = 0
            else:
                next_agentIndex = curr_agentIndex+1

            p = 1.0/len(game_state.getLegalActions(curr_agentIndex))
            for action in game_state.getLegalActions(curr_agentIndex):
                next_value = exptmax(next_agentIndex, game_state.generateSuccessor(
                    curr_agentIndex, action), depth)
                if not val_action:
                    if curr_agentIndex == 0:
                        val_action = (next_value[0], action)
                    else:
                        val_action = (p*next_value[0], action)
                else:
                    prev_value = val_action[0]
                    if curr_agentIndex == 0:
                        if next_value[0] > prev_value:
                            val_action = (next_value[0], action)
                    else:
                        val_action = (p*next_value[0]+prev_value, action)
            return val_action
        final_val_action = exptmax(0, gameState, 0)
        return final_val_action[1]
        # util.raiseNotDefined()

ghosts = currentGameState.getGhostStates()
    pacman_position = currentGameState.getPacmanPosition()
    foods = currentGameState.getFood().asList()
    capsules = currentGameState.getCapsules()
    final_eval_score = currentGameState.getScore()

    final_eval_score += -20*(len(capsules))
    final_eval_score += -10*(len(foods))

    for food in foods:
        food_distance = manhattanDistance(pacman_position, food)
        if food_distance < 2:
            final_eval_score += -1*food_distance
        elif food_distance < 6:
            final_eval_score += -0.5*food_distance
        else:
            final_eval_score += -0.25*food_distance

    for ghost in ghosts:
        ghost_distance = manhattanDistance(
            pacman_position, ghost.getPosition())
        if ghost.scaredTimer:
            if ghost_distance < 2:
                final_eval_score += -20*ghost_distance
            else:
                final_eval_score += -8*ghost_distance
        else:
            if ghost_distance < 2:
                final_eval_score += 4*ghost_distance
            elif ghost_distance < 6:
                final_eval_score += 2*ghost_distance
            else:
                final_eval_score += 0.5*ghost_distance

    for capsule in capsules:
        capsule_distance = manhattanDistance(pacman_position, capsule)
        if capsule_distance < 2:
            final_eval_score += -15*capsule_distance
        else:
            final_eval_score += -8*capsule_distance

    return final_eval_score
    # util.raiseNotDefined()

