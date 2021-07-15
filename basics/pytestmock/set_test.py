"""
==============================
    @author: bmz
    @contact: bomz@dianzhong.com
    @software: PyCharm
    @file: Public.py
    @time: 2021/5/21 20:15
    @desc:
    @Site : 
    @Version:  2.0
==============================
"""
import pytest
from basics.pytestmock.mock import Mock


class Test():

    def test_01(self, mocker):
        # 实例化
        p = Mock()
        mock_value = {'result': "雪", 'status': '下雪了！'}
        # 通过object的方式进行查找需要mock的对象
        p.weather = mocker.patch.object(Mock, "weather", return_value=mock_value)
        result = p.weather_result()
        print(result)
        assert result == '下雪了！'

    def test_02(self, mocker):
        # 实例化
        product = Mock()
        # Mock的返回值
        mock_value = {'result': "雨", 'status': '下雨了！'}
        # 第一个参数必须是模拟mock对象的完整路径
        product.weather = mocker.patch("mock.Mock.weather", return_value=mock_value)
        result = product.weather_result()
        print(result)
        assert result == '下雨了！'


if __name__ == '__main__':
    pytest.main(['-v', '-s'])