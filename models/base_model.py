from abc import ABC, abstractmethod


class BaseAIModel(ABC):
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def run(self, messages):
        pass

    @abstractmethod
    def name(self):
        pass
