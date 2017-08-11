# -*- coding: utf-8 -*-

import message_pb2

hero1 = message_pb2.Hero_msg()
hero1.name = "zhaozilong"
hero1.point_x =  20
hero1.point_y = 40
send_msg = hero1.SerializeToString()
print send_msg

hero2 = message_pb2.Hero_msg()
hero2.ParseFromString(send_msg)
print hero2.name
print hero2.point_x
print hero2.point_y




