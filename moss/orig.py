def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.
        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.
        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.
        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        
        "*** YOUR CODE HERE ***"
        pellets = successorGameState.getCapsules()
        foodPosition = newFood.asList()
        foodCount = len(foodPosition)
        closestDistance = 1e6
        longestDistance = 0

        for i in range(foodCount):
            for j in range(i+1,foodCount,1):
                distance = manhattanDistance(foodPosition[i],foodPosition[j])
                if distance > longestDistance:
                    longestDistance = distance

        for i in range(foodCount):
            distance = manhattanDistance(foodPosition[i],newPos) + foodCount*100 + longestDistance
            if distance < closestDistance:
                closestDistance = distance

        if foodCount == 0:
            closestDistance = 0
        score = -closestDistance

        closestDistance = 1e6
        closestPos = (0,0)
        closestScareTime = 0
        flag = True
        for i in range(len(newGhostStates)):
            ghostPos = successorGameState.getGhostPosition(i+1)
            distance = manhattanDistance(newPos,ghostPos)
            if newScaredTimes[i] > 0:
                score += 1/float(distance)*100
            if distance < closestDistance:
                closestDistance = distance
                closestPos = ghostPos
                closestScareTime = newScaredTimes[i]
            if(newScaredTimes[i]>0):
                if manhattanDistance(ghostPos,newPos) <= 2:
                    return 1e8
                flag = False
            if manhattanDistance(newPos,ghostPos)<=1:
                score -= 1e6

        if manhattanDistance(newPos,closestPos)<=1 and closestScareTime==0:
            score -= 1e6

        if (newScaredTimes[0] - closestDistance) > 0:
            score+=1e6
        score -= 10000*len(pellets)

        for p in pellets:
            distance = manhattanDistance(newPos,p)
            score += 1/float(distance)*100
        return score

 def Max_Value(depth, gameState):
            if depth==self.depth or gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)
            return max(Min_Value(1,depth,gameState.generateSuccessor(0,action)) for action in gameState.getLegalActions(0))

        def Min_Value(agent, depth, gameState):
            if agent==0:
                return Max_Value(depth+1,gameState)
            if depth==self.depth or gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)
            return min(Min_Value((agent+1)%gameState.getNumAgents(),depth,gameState.generateSuccessor(agent,action)) for action in gameState.getLegalActions(agent))
            
        final_action = None
        value = None
        for action in gameState.getLegalActions(0):
            val = Min_Value(1,0,gameState.generateSuccessor(0,action))
            if value == None or val > value:
                value = val
                final_action = action
        return final_action

def Max_Value(depth, gameState, alpha, beta):
            if depth==self.depth or gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)
            value = float('-inf')
            for action in gameState.getLegalActions(0):
                val = Min_Value(1,depth,gameState.generateSuccessor(0,action), alpha,beta)
                value = max(value,val)
                if value > beta:
                    return value
                alpha = max(alpha,value)
            return value

        def Min_Value(agent, depth, gameState, alpha, beta):
            if agent==0:
                return Max_Value(depth+1,gameState, alpha, beta)
            if depth==self.depth or gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)
            value = float('inf')
            for action in gameState.getLegalActions(agent):
                val = Min_Value((agent+1)%gameState.getNumAgents(),depth,gameState.generateSuccessor(agent,action), alpha,beta)
                value = min(value,val)
                if value < alpha:
                    return value
                beta = min(beta,value)
            return value
            
        alpha = float('-inf')
        beta = float('inf')
        final_action = None
        value = float('-inf')
        for action in gameState.getLegalActions(0):
            val = Min_Value(1,0,gameState.generateSuccessor(0,action),alpha,beta)
            if value == float('-inf') or val > value:
                value = val
                final_action = action
            if value > beta:
                return value
            alpha = max(alpha, value)
        return final_action


def Max_Value(depth, gameState):
            if depth==self.depth or gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)
            return max(Exp_Value(1,depth,gameState.generateSuccessor(0,action)) for action in gameState.getLegalActions(0))

        def Exp_Value(agent, depth, gameState):
            if agent==0:
                return Max_Value(depth+1,gameState)
            if depth==self.depth or gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)
            v = 0
            length = float(len(gameState.getLegalActions(agent)))
            for action in gameState.getLegalActions(agent):
                p = 1.0/length
                v += p * Exp_Value((agent+1)%gameState.getNumAgents(),depth,gameState.generateSuccessor(agent,action))
            return v
            
        final_action = None
        value = None
        for action in gameState.getLegalActions(0):
            val = Exp_Value(1,0,gameState.generateSuccessor(0,action))
            if value == None or val > value:
                value = val
                final_action = action
        return final_action

        util.raiseNotDefined()

if currentGameState.isLose():
        return -1e6
    if currentGameState.isWin():
        return 1e6 

    ghosts = currentGameState.getGhostStates()
    pacman_pos = currentGameState.getPacmanPosition()
    food_pos = currentGameState.getFood().asList()
    pellets = currentGameState.getCapsules()

    score_from_ghost = 0
    for ghost in ghosts:
        distance = manhattanDistance(pacman_pos, ghost.getPosition())
        if ghost.scaredTimer > 0:
            score_from_ghost += max(8 - distance, 0)**2
        else:
            score_from_ghost -= max(7 - distance, 0)**2

    score_from_suicide = 0
    for ghost in ghosts:
        dist = manhattanDistance(pacman_pos, ghost.getPosition())
        if dist<=1:
            score_from_suicide = -1e6

    score_from_food = -1e6
    for food in food_pos:
        distance = 1.0 / float(manhattanDistance(pacman_pos, food))
        score_from_food = max(score_from_food,distance)
    if len(food_pos)==0:
        score_from_food = 0

    score_from_capsule = -1e6
    for pellet in pellets:
        distance = 1.0 / float(manhattanDistance(pacman_pos, pellet))
        score_from_capsule = max(score_from_capsule,distance)
    if len(pellets) == 0:
        score_from_capsule=0

    return currentGameState.getScore() + score_from_ghost + score_from_food + 100.0 * score_from_capsule + score_from_suicide
