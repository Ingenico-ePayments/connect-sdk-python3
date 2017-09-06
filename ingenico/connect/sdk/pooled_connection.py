from .connection import Connection


# noinspection PyAbstractClass
class PooledConnection(Connection):
    """
    Represents a pooled connection to the Ingenico ePayments platform server.
    Instead of setting up a new HTTP connection for each request, this
    connection uses a pool of HTTP connections.
    """

    def close_idle_connections(self, idle_time):
        """
        Closes all HTTP connections that have been idle for the specified time.
        This should also include all expired HTTP connections.

        :param idle_time: a datetime.timedelta object indicating the idle time
        """
        raise NotImplementedError

    def close_expired_connections(self):
        """
        Closes all expired HTTP connections.
        """
        raise NotImplementedError
