from abc import ABC, abstractmethod


class ObfuscationCapable(ABC):
    """
    Classes that extend this class support obfuscating bodies and headers.
    """

    @abstractmethod
    def set_body_obfuscator(self, body_obfuscator):
        """
        Sets the current body obfuscator to use.
        """
        raise NotImplementedError

    @abstractmethod
    def set_header_obfuscator(self, header_obfuscator):
        """
        Sets the current header obfuscator to use.
        """
        raise NotImplementedError
