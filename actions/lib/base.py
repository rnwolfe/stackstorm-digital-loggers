from dlipower import PowerSwitch

from st2common.runners.base_action import Action


class DLBaseAction(Action):
    """ Base Digital Logger class for all actions
    """

    def __init__(self, config):
        """ init method, run at class creation
        """
        super(DLBaseAction, self).__init__(config)
        self.logger.debug('Instantiating DLBaseAction()')
        self.switch = self._init_client()

    def _init_client(self):
        """ init_client method, run at class creation
        """
        self.logger.debug('Initializing dlipower client')
        switch = PowerSwitch(
            hostname=self.config['hostname'], userid=self.config['username'], password=self.config['password'])

        if switch.verify():
            return switch
        else:
            self.logger.error(f"Failed to connect to switch {self.config.['hostname']}")
            exit(1)
