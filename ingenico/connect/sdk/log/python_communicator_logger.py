from ingenico.connect.sdk.log.communicator_logger import \
    CommunicatorLogger


class PythonCommunicatorLogger(CommunicatorLogger):
    """
    A communicator logger that is backed by the log library.
    """

    def __init__(self, logger, log_level, error_log_level=False):
        """
        Logs messages to the argument logger using the argument log_level.
        If absent, the error_log_level will be equal to the log_level.
        Note that if the CommunicatorLogger's log level is lower than the
        argument logger's log level (e.g. the CommunicatorLogger is given
        log.INFO as level and the argument logger has a level of
        log.WARNING), then nothing will be logged to the logger.

        :param logger: the logger to log to
        :param log_level: the log level that will be used for non-error
         messages logged via the CommunicatorLogger
        :param error_log_level: the log level that will be used for error
         messages logged via the CommunicatorLogger.
        """
        CommunicatorLogger.__init__(self)
        if not error_log_level:
            error_log_level = log_level
        if logger is None:
            raise ValueError("logger is required")
        if log_level is None:
            raise ValueError("log_level is required")
        if error_log_level is None:
            raise ValueError("error_log_level is required")
        self.__logger = logger
        self.__log_level = log_level
        self.__error_log_level = error_log_level

    def log(self, message, thrown=None):
        """
        Log a message to the underlying logger.
        If thrown is absent, the message will be logged with the
        CommunicatorLogger's log_level, if a thrown object is provided,
        the message and exception will be logged with the CommunicatorLogger's
        error_log_level.

        :param message: the message to be logged
        :param thrown: an optional throwable object
        """
        if not thrown:
            self.__logger.log(self.__log_level, message)
        else:
            self.__logger.log(self.__error_log_level, message, thrown)
