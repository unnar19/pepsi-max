import Employee
import Listing
import Real_estate
import Report
import Search
import Ticket
from Exceptions import *

# Logic_wrapper is a gateway between UI and Logic classes.
# All UI classes can use the Logic wrapper but only a few
# methods are exposed. Hence, the logic wrapper controls
# all communication between UI and Logic

class Logic_wrapper:
    def __init__(self) -> None:
        self.id = 'LW'
        

    def __authenticate_requester(self, requester_id, receiver):
        """
        Each Logic class only accepts requests from certain UI classes
        This function checks if requester_id is in receiver whitelist

        TAKES IN:
        Receiving_class, Requester_ID

        RETURNS:
        Bool
        """
        return receiver._whitelisted(requester_id)

    def _authenticate_user(self, requester_id, credentials):
        """Credentials are only for employees. If """
        authenticated = self.__authenticate_requester(requester_id, Employee)
        if authenticated:
            return Employee._authenticate_user(self.id, credentials)
        else:
            raise CouldNotAuthenticateUIException(f'Authentication returned: {authenticated}')
        