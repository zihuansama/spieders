from lxml import etree

import requests

# __VIEWSTATE: Ic/bHsyV2HWLnVOXeX5bNxddYEQhOiMrS0oGRaOhYkrbyyiXaiww0aLW485vaxBr0j4WVAdMaUvnh7sq8oDuEIazS+rX8kFD+yt+6FVrxrDx3Ud4FytdzizpL7/vczaXwSfnMMz6T80/xy73wi18c4/v43s=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 15377001677
# pwd: w526079.11]
# code: gvy4
# denglu:
# __VIEWSTATE: JaWPETW77psBrJE4NHcwUoqIk/OPo21UZErRmMPDoIE4QDnTsVSB/kVWg1OGJhqkg8mAAimumNHRkkk+qvnARj37EZGcAgyBgtSZwSaSOPSfBlgMoRRhnloJw6fTe0WKNRqf3mdSabqnykn0mfI+RztHHeM=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 15377001677
# pwd: 1234561
# code: o2kq
# denglu: 登录

url = 'http://so.gushiwen.cn/user/collect.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
response = requests.get(url=url,headers=headers)
content =response.text

tree = etree.HTML(content)
tree_list = tree.xpath('//div/input[@id="__VIEWSTATEGENERATOR"]/@value')
