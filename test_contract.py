import copy
import unittest
import xml_namespace_contract as m

P={'namespaces':['urn:feed',''], 'rules':[{'path':['{urn:feed}catalog','{urn:feed}item'],'min':1,'max':2,'required_attributes':['id'],'unique_attribute':'id'}]}


class Tests(unittest.TestCase):
    def run_xml(self,s,p=None):return m.audit(s.encode(),p or P)
    def test_prefix_invariance(self):
        a=self.run_xml('<a:catalog xmlns:a="urn:feed"><a:item id="1"/></a:catalog>')
        b=self.run_xml('<b:catalog xmlns:b="urn:feed"><b:item id="1"/></b:catalog>')
        self.assertEqual(a,b);self.assertFalse(a['findings'])
    def test_default_namespace(self):self.assertFalse(self.run_xml('<catalog xmlns="urn:feed"><item id="1"/></catalog>')['findings'])
    def test_uri_drift(self):self.assertTrue(self.run_xml('<catalog xmlns="urn:other"><item id="1"/></catalog>')['findings'])
    def test_missing_path(self):self.assertEqual(self.run_xml('<catalog xmlns="urn:feed"/>')['findings'][0]['code'],'count')
    def test_duplicate_ids(self):self.assertEqual(self.run_xml('<catalog xmlns="urn:feed"><item id="1"/><item id="1"/></catalog>')['findings'][0]['code'],'duplicate_attribute')
    def test_missing_attr(self):self.assertEqual(self.run_xml('<catalog xmlns="urn:feed"><item/></catalog>')['findings'][0]['code'],'missing_attribute')
    def test_namespaced_attr(self):self.assertEqual(self.run_xml('<catalog xmlns="urn:feed" xmlns:z="urn:bad"><item id="1" z:x="v"/></catalog>')['findings'][0]['code'],'namespace')
    def test_doctype(self):
        with self.assertRaises(ValueError):self.run_xml('<!DOCTYPE x [<!ENTITY a "x">]><x>&a;</x>')
    def test_encoding(self):
        with self.assertRaises(ValueError):self.run_xml('<?xml version="1.0" encoding="latin-1"?><x/>')
    def test_malformed(self):
        with self.assertRaises(ValueError):self.run_xml('<x>')
    def test_depth(self):
        with self.assertRaises(ValueError):self.run_xml('<x>'*65+'</x>'*65)
    def test_policy(self):
        p=copy.deepcopy(P);p['rules'][0]['min']=True
        with self.assertRaises(ValueError):m.contract(p)
    def test_duplicate_path(self):
        p=copy.deepcopy(P);p['rules']*=2
        with self.assertRaises(ValueError):m.contract(p)


if __name__=='__main__':unittest.main()
