from git import Repo

def _create_head_master_from_origin(self):
        if not 'master' in self.repo.heads:
            self.logger.debug("Creating local master branch")
            self.repo.create_head('master', self.origin.refs.master)
        self.repo.heads.master.set_tracking_branch(self.origin.refs.master)
