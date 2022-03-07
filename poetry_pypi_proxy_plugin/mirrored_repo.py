from typing import List

from poetry.core.packages.package import Package
from poetry.core.packages.utils.link import Link
from poetry.repositories.pypi_repository import PyPiRepository
from poetry.repositories.legacy_repository import LegacyRepository


class MirroredPyPi(PyPiRepository):
    def find_links_for_package(self, package: Package) -> List[Link]:
        result = super().find_links_for_package(package)
        # result[0].url
        return result
