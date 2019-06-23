class IceCream(object):
    def __init__(self, flavor):
        self.flavor = flavor
    def change_flavor(self, new_flavor):
        print('아이스크림을 %s에서 %s로 변경해주세요.' %(self.flavor, new_flavor))
        self.flavor = new_flavor
        print('아이스크림 맛을 %s로 변경해드렸어요.' %self.flavor)

ice_cream = IceCream('레인보우 샤베트')
ice_cream.change_flavor('바람과 함께 사라지다')
