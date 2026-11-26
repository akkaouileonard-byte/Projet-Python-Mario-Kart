class Block:
    """Classe représentant un bloc du circuit."""
    def __init__(self):
        pass


class StartBlock(Block):
    """Bloc indiquant la position de départ d'un joueur."""
    def __init__(self, player_id):
        super().__init__()
        self.player_id = player_id


class CheckpointBlock(Block):
    """Point de passage obligatoire du circuit."""
    def __init__(self, checkpoint_id):
        super().__init__()
        self.checkpoint_id = checkpoint_id


class FinishBlock(Block):
    """Bloc correspondant à la ligne d'arrivée."""
    def __init__(self):
        super().__init__()


class BoostBlock(Block):
    """Bloc donnant une accélération supplémentaire."""
    def __init__(self, boost_value=1.0):
        super().__init__()
        self.boost_value = boost_value
