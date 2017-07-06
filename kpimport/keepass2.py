"""Importer for keepass2"""
import os
import lxml.etree
import kickpass
from .importer import KickpassImporter


class Keepass2Importer(KickpassImporter):
    """Import password from a keepass2 xml file"""
    def __init__(self, inputdata):
        super().__init__(inputdata)
        self._tree = lxml.etree.parse(self._inputdata)

    @staticmethod
    def getkeyvalue(entry, key):
        (value, ) = entry.xpath("./String/Key/text()[normalize-space()='"+key+"']/../following-sibling::Value/text()[normalize-space()]")
        return value

    def getsafes(self):
        safes = []
        entries = self._tree.getroot().findall('./Root//Group/Entry')
        for entry in entries:
            path = self.getkeyvalue(entry, 'Title')
            for parent in entry.iterancestors():
                if parent.tag == 'Group':
                    (name,) = parent.xpath("./Name/text()[normalize-space()]")
                    # Avoid getting first group called 'Root'
                    if parent.getparent().tag == 'Group':
                        path = os.path.join(name, path)
            safes.append((path, entry))

        return safes

    def importsafe(self, ctx, safe, elem):
        safe.password = b"test"
        safe.metadata = b"test"

    @staticmethod
    def magic(inputdata):
        try:
            tree = lxml.etree.parse(inputdata)
            if tree.getroot().tag == 'KeePassFile':
                return 1
            return 0
        except ET.ParseError as _:
            return 0
