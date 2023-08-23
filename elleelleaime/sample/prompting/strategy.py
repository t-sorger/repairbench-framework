from abc import ABC, abstractmethod
from elleelleaime.core.benchmarks.bug import Bug

from typing import Tuple, Optional


class PromptingStrategy(ABC):
    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def prompt(self, bug: Bug) -> Tuple[Optional[str], Optional[str], Optional[str]]:
        """
        Returns the prompt for the given bug.

        :param bug: The bug to generate the prompt for.
        :return: A tuple of the form (buggy_code, fixed_code, prompt) or None if the prompt cannot be generated.
        """
        pass