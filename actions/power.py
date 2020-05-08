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
            return (True, self.switch.statuslist())

        # For the purposes of this action, the outlet is the 
        # physical outlet number, and the relay is the index 
        # of the outlet in a pythonic list.
        if outlet and (int(outlet) or outlet.isnumeric()):
            # Adjust outlet number for starting at index 0
            outlet = int(outlet)
            relay = outlet - 1
        else:
            # If no outlet provided, turn all on.
            outlet = 'all'
            relay = 'all;'

        if state == 'on':  # POWER ON
            self.logger.debug(f'Powering on outlet {outlet}')
            if isinstance(relay, int):
                return (True, self.switch[relay].on())
            else:
                return (True, [outlet.on() for outlet in self.switch])
        if state == 'off':  # POWER OFF
            self.logger.debug(f'Powering off outlet {outlet}')
            if isinstance(relay, int):
                return (True, self.switch[relay].off())
            else:
                return (True, [outlet.off() for outlet in self.switch])
