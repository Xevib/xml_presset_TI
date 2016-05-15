import unittest
from lxml import etree

class TestXML(unittest.TestCase):

    def setUp(self):
        pass

    def test_xsd(self):
        filename = 'put your file name here.xml'
        f_preset = open(filename)
        f_xsd = open('test/tagging-preset.xsd')
        xmlschema_doc = etree.parse(f_xsd)
        xmlschema = etree.XMLSchema(xmlschema_doc)
        doc = etree.parse(f_preset)
        xmlschema.assertValid(doc)

if __name__ == '__main__':
    unittest.main()
