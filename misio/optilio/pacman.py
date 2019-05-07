from ..pacman.agents import Agent
from ..pacman.pacman import ClassicRules, GameState
from ..pacman.layout import Layout, get_layout
from ..pacman.textDisplay import NullGraphics

END_GAME_WORD="END"
class OptilioPacmanGameRunner(object):
    def __init__(self,
                 layout_dir,
                 random_ghosts=False,
                 ):
        layout = get_layout(layout_dir)
        if layout is None:
            raise Exception("The layout " + layout_dir + " cannot be found")
        self.layout = layout
        if random_ghosts:
            from ..pacman.ghostAgents import RandomGhost
            GhostClass = RandomGhost
        else:
            from ..pacman.ghostAgents import DirectionalGhost
            GhostClass = DirectionalGhost
        self.ghosts = [GhostClass(i + 1) for i in range(layout.getNumGhosts())]
        self.display = NullGraphics()
        self.agent = StdIOAgent()

        print(layout.height)
        print(layout)

    def run_game(self, ):

        rules = ClassicRules()
        game = rules.newGame(
            self.layout,
            self.agent,
            self.ghosts,
            self.display,
            quiet=True)
        game.run(print_ghost_moves=True)
        print(END_GAME_WORD)
        return game


class StdIOPacmanRunner(object):
    def __init__(self):
        self.layout = StdIOPacmanRunner.load_layout_from_stdin()

    @staticmethod
    def load_layout_from_stdin():
        lines_num = int(input())
        layout_text = []
        for _ in range(lines_num):
            layout_text.append(input().strip())
        return Layout(layout_text)

    def run_game(self, agent):
        # create initial state
        state = GameState()
        state.initialize(self.layout, self.layout.getNumGhosts())
        while not state.isFinished():
            action = agent.getAction(state)
            state = state.generatePacmanSuccessor(action)
            print(action, flush=True)
            raw_input = input()
            if raw_input != END_GAME_WORD:
                ghost_actions = raw_input.strip().split()
                for ai, action in enumerate(ghost_actions, start=1):
                    state = state.generateSuccessor(ai, action)
            else:
                break

class StdIOAgent(Agent):
    def getAction(self, state):
        return input().strip()
