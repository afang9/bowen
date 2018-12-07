import unittest
import HTMLTestRunnertest
from kuangjia.config.查_学校 import School_查询
from kuangjia.data.read_数据 import duqu_shuju
class G2(unittest.TestCase):
    tes_查询=School_查询().school_快查
    shuju =duqu_shuju()
    def test_1(self):
        html = self.tes_查询(self.shuju[0][0])
        try:
            self.assertEqual(html['code'], int(self.shuju[0][1]))
        except:
            self.assertIn(len(html['data']), range(int(self.shuju[0][2])))
    def test_2(self):
        # shuju = self.tes_shuju()
        html = self.tes_查询(self.shuju[1][0])
        self.assertEqual(html['code'], int(self.shuju[1][1]))
        # self.assertIn(len(html['data']), range(int(self.shuju[1][2])))
    def test_3(self):
        # shuju = self.tes_shuju()
        html = self.tes_查询(self.shuju[2][0])
        self.assertEqual(html['code'], int(self.shuju[2][1]))
if __name__=='__main__':
    unittest.main()