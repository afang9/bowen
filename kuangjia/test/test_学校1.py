import unittest
from kuangjia.data.read_data import Read_Shuju
from kuangjia.config.s_school import School
class Tes_case(unittest.TestCase):
    tes_find=School().shool_search
    shuju=Read_Shuju.duqu_shuju()
    def test_1(self):
        html=self.tes_find(self.shuju[0][0])
        try:
            self.assertEqual(self.shuju['code'],int(self.shuju[0][1]))
        finally:
            self.assertEqual(len(self.shuju['data']),range(self.shuju[0][2]))
    def test_2(self):
        html=self.tes_find(self.shuju[1][0])
        try:
            self.assertEqual(self.shuju['code'],int(self.shuju[1][1]))
        finally:
            self.assertNotEqual(len(self.shuju['data']),range(self.shuju[0][2]))
    def test_3(self):
        html=self.tes_find(self.shuju[2][0])
        try:
            self.assertEqual(self.shuju['code'],int(self.shuju[2][1]))
        finally:
            self.assertNotEqual(len(self.shuju['data']),range(self.shuju[2][2]))
            self.assertTrue(self.shuju['code']==int(self.shuju[2][2]))
if __name__=='__main__':
    unittest.main()

