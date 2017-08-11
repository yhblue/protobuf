# -*- coding: utf-8 -*-

import 


hero = .Hero_msg()
hero.name = "zhaozilong"
hero.point_x =  20
hero.point_y = 40
send_msg = .SerializeToString()
print send_msg

hero2 = .Hero_msg()
hero2.ParseFromString(send_msg)
print hero2.name
print hero2.point_x
print hero2.point_y




