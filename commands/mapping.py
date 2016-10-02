class Mapping:
    add_undo_mappings = {
        '.': 'git reset HEAD .'
    }

    commit_undo_mappings = {
        '-m': 'git reset HEAD~1 --soft',
        '-am': 'git reset HEAD~1',
    }

    @staticmethod
    def get_add_undo_mappings():
        return Mapping.add_undo_mappings

    @staticmethod
    def get_commit_undo_mappings():
        return Mapping.commit_undo_mappings
