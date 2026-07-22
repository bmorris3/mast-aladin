from abc import ABC, abstractmethod
from mast_aladin.aida import AIDA_aspects


class ViewerSyncAdapter(ABC):
    def sync_to(self, sync_adapter, aspects):

        # TODO (2026-07-22): the jdaviz glue viewer attribute `aid`
        # will be removed in a PR coming soon, the line below will
        # need to be updated.
        viewer = sync_adapter.viewer
        if hasattr(sync_adapter, 'aid'):
            # temporarily, the jdaviz sync adapter has an `aid attribute`
            viewer = sync_adapter.aid

        source_viewport = viewer.get_viewport(sky_or_pixel="sky")

        new_viewport = viewer.get_viewport(sky_or_pixel="sky").copy()
        for aspect in set(aspects) & {*AIDA_aspects}:
            new_viewport[aspect] = source_viewport[aspect]

        viewer.set_viewport(**new_viewport)

    @abstractmethod
    def add_callback(self, func):
        raise NotImplementedError

    @abstractmethod
    def remove_callback(self, func):
        raise NotImplementedError

    @abstractmethod
    def show(self):
        raise NotImplementedError
