import re

def test(raw):
    regex = r'([A-Z]+-[0-9]+)'
    p = re.compile(regex)
    res = p.search(raw)
    if res:
        print(res.group(1))
    else:
        print(raw, '不匹配')

test('【拦截Case巡查】FLIGHT-47537')
test('FLIGHT-47537-dev')
test('FLIGHt-47537-dev')
test(' ')


