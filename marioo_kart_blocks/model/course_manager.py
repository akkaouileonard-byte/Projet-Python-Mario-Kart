

class CourseManager:
    """Suit les checkpoints, les tours et le vainqueur de chaque joueur."""

    def __init__(self, total_laps=2, checkpoint_count=2):
        self.total_laps = total_laps
        self.checkpoint_count = checkpoint_count
        self.laps = {}
        self.checkpoints = {}
        self.last_checkpoint = {}
        self.winner = None

    def add_player(self, player_id, col, row):
        """Enregistre la position de départ d'un joueur."""
        self.laps[player_id] = 0
        self.checkpoints[player_id] = set()
        self.last_checkpoint[player_id] = (col, row)

    def reach_checkpoint(self, player_id, checkpoint_id, col, row):
        """Valide un checkpoint et conserve sa position."""
        self.checkpoints[player_id].add(checkpoint_id)
        self.last_checkpoint[player_id] = (col, row)

    def cross_finish(self, player_id):
        """Compte un tour seulement si tous les checkpoints ont été franchis."""
        if self.winner is not None:
            return False
        if len(self.checkpoints[player_id]) < self.checkpoint_count:
            return False

        self.laps[player_id] += 1
        self.checkpoints[player_id].clear()
        if self.laps[player_id] >= self.total_laps:
            self.winner = player_id
        return True

    def get_respawn_position(self, player_id):
        """Renvoie la position du dernier checkpoint ou du départ."""
        return self.last_checkpoint[player_id]
