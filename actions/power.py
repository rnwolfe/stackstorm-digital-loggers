from lib.base import DLBaseAction

""" This action handles changing power state of outlets.
"""


class DLAction(DLBaseAction):

    """ Digital Loggers run action
    """

    def run(self, outlet=None, state=None, **kwargs):
        """ Run action and call appropriate method
        """

        if not outlet and not state:
            # If no parameters given, return status of outlets
            return (True, self.dl.switch.statuslist())

        if outlet and (int(outlet) or outlet.isnumeric()):
            # Adjust outlet number for starting at index 0
            relay = int(outlet) - 1
        else:
            # If no outlet provided, turn all on.
            relay = 'all;'

        if state == 'on':  # POWER ON
            self.logger.debug(f'Powering on {relay}')
            if int(relay):
                return (True, self.dl.switch[relay].on())
            else:
                return (True, [outlet.on() for outlet in self.dl.switch])
        if state == 'off':  # POWER ON
            self.logger.debug(f'Powering off {relay}')
            if int(relay):
                return (True, self.dl.switch[relay].off())
            else:
                return (True, [outlet.off() for outlet in self.dl.switch])
