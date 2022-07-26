# $Id: qq.py 48 2008-05-27 17:31:15Z yardley $
# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .dpkt import Packet


# header_type
QQ_HEADER_BASIC_FAMILY = 0x02
QQ_HEADER_P2P_FAMILY = 0x00
QQ_HEADER_03_FAMILY = 0x03
QQ_HEADER_04_FAMILY = 0x04
QQ_HEADER_05_FAMILY = 0x05

header_type_str = [
    "QQ_HEADER_P2P_FAMILY",
    "Unknown Type",
    "QQ_HEADER_03_FAMILY",
    "QQ_HEADER_04_FAMILY",
    "QQ_HEADER_05_FAMILY",
]

# command
QQ_CMD_LOGOUT = 0x0001
QQ_CMD_KEEP_ALIVE = 0x0002
QQ_CMD_MODIFY_INFO = 0x0004
QQ_CMD_SEARCH_USER = 0x0005
QQ_CMD_GET_USER_INFO = 0x0006
QQ_CMD_ADD_FRIEND = 0x0009
QQ_CMD_DELETE_FRIEND = 0x000A
QQ_CMD_ADD_FRIEND_AUTH = 0x000B
QQ_CMD_CHANGE_STATUS = 0x000D
QQ_CMD_ACK_SYS_MSG = 0x0012
QQ_CMD_SEND_IM = 0x0016
QQ_CMD_RECV_IM = 0x0017
QQ_CMD_REMOVE_SELF = 0x001C
QQ_CMD_REQUEST_KEY = 0x001D
QQ_CMD_LOGIN = 0x0022
QQ_CMD_GET_FRIEND_LIST = 0x0026
QQ_CMD_GET_ONLINE_OP = 0x0027
QQ_CMD_SEND_SMS = 0x002D
QQ_CMD_CLUSTER_CMD = 0x0030
QQ_CMD_TEST = 0x0031
QQ_CMD_GROUP_DATA_OP = 0x003C
QQ_CMD_UPLOAD_GROUP_FRIEND = 0x003D
QQ_CMD_FRIEND_DATA_OP = 0x003E
QQ_CMD_DOWNLOAD_GROUP_FRIEND = 0x0058
QQ_CMD_FRIEND_LEVEL_OP = 0x005C
QQ_CMD_PRIVACY_DATA_OP = 0x005E
QQ_CMD_CLUSTER_DATA_OP = 0x005F
QQ_CMD_ADVANCED_SEARCH = 0x0061
QQ_CMD_REQUEST_LOGIN_TOKEN = 0x0062
QQ_CMD_USER_PROPERTY_OP = 0x0065
QQ_CMD_TEMP_SESSION_OP = 0x0066
QQ_CMD_SIGNATURE_OP = 0x0067
QQ_CMD_RECV_MSG_SYS = 0x0080
QQ_CMD_RECV_MSG_FRIEND_CHANGE_STATUS = 0x0081
QQ_CMD_WEATHER_OP = 0x00A6
QQ_CMD_ADD_FRIEND_EX = 0x00A7
QQ_CMD_AUTHORIZE = 0X00A8
QQ_CMD_UNKNOWN = 0xFFFF
QQ_SUB_CMD_SEARCH_ME_BY_QQ_ONLY = 0x03
QQ_SUB_CMD_SHARE_GEOGRAPHY = 0x04
QQ_SUB_CMD_GET_FRIEND_LEVEL = 0x02
QQ_SUB_CMD_GET_CLUSTER_ONLINE_MEMBER = 0x01
QQ_05_CMD_REQUEST_AGENT = 0x0021
QQ_05_CMD_REQUEST_FACE = 0x0022
QQ_05_CMD_TRANSFER = 0x0023
QQ_05_CMD_REQUEST_BEGIN = 0x0026
QQ_CLUSTER_CMD_CREATE_CLUSTER = 0x01
QQ_CLUSTER_CMD_MODIFY_MEMBER = 0x02
QQ_CLUSTER_CMD_MODIFY_CLUSTER_INFO = 0x03
QQ_CLUSTER_CMD_GET_CLUSTER_INFO = 0x04
QQ_CLUSTER_CMD_ACTIVATE_CLUSTER = 0x05
QQ_CLUSTER_CMD_SEARCH_CLUSTER = 0x06
QQ_CLUSTER_CMD_JOIN_CLUSTER = 0x07
QQ_CLUSTER_CMD_JOIN_CLUSTER_AUTH = 0x08
QQ_CLUSTER_CMD_EXIT_CLUSTER = 0x09
QQ_CLUSTER_CMD_SEND_IM = 0x0A
QQ_CLUSTER_CMD_GET_ONLINE_MEMBER = 0x0B
QQ_CLUSTER_CMD_GET_MEMBER_INFO = 0x0C
QQ_CLUSTER_CMD_MODIFY_CARD = 0x0E
QQ_CLUSTER_CMD_GET_CARD_BATCH = 0x0F
QQ_CLUSTER_CMD_GET_CARD = 0x10
QQ_CLUSTER_CMD_COMMIT_ORGANIZATION = 0x11
QQ_CLUSTER_CMD_UPDATE_ORGANIZATION = 0x12
QQ_CLUSTER_CMD_COMMIT_MEMBER_ORGANIZATION = 0x13
QQ_CLUSTER_CMD_GET_VERSION_ID = 0x19
QQ_CLUSTER_CMD_SEND_IM_EX = 0x1A
QQ_CLUSTER_CMD_SET_ROLE = 0x1B
QQ_CLUSTER_CMD_TRANSFER_ROLE = 0x1C
QQ_CLUSTER_CMD_CREATE_TEMP = 0x30
QQ_CLUSTER_CMD_MODIFY_TEMP_MEMBER = 0x31
QQ_CLUSTER_CMD_EXIT_TEMP = 0x32
QQ_CLUSTER_CMD_GET_TEMP_INFO = 0x33
QQ_CLUSTER_CMD_MODIFY_TEMP_INFO = 0x34
QQ_CLUSTER_CMD_SEND_TEMP_IM = 0x35
QQ_CLUSTER_CMD_SUB_CLUSTER_OP = 0x36
QQ_CLUSTER_CMD_ACTIVATE_TEMP = 0x37

QQ_CLUSTER_SUB_CMD_ADD_MEMBER = 0x01
QQ_CLUSTER_SUB_CMD_REMOVE_MEMBER = 0x02
QQ_CLUSTER_SUB_CMD_GET_SUBJECT_LIST = 0x02
QQ_CLUSTER_SUB_CMD_GET_DIALOG_LIST = 0x01

QQ_SUB_CMD_GET_ONLINE_FRIEND = 0x2
QQ_SUB_CMD_GET_ONLINE_SERVICE = 0x3
QQ_SUB_CMD_UPLOAD_GROUP_NAME = 0x2
QQ_SUB_CMD_DOWNLOAD_GROUP_NAME = 0x1
QQ_SUB_CMD_SEND_TEMP_SESSION_IM = 0x01
QQ_SUB_CMD_BATCH_DOWNLOAD_FRIEND_REMARK = 0x0
QQ_SUB_CMD_UPLOAD_FRIEND_REMARK = 0x1
QQ_SUB_CMD_REMOVE_FRIEND_FROM_LIST = 0x2
QQ_SUB_CMD_DOWNLOAD_FRIEND_REMARK = 0x3
QQ_SUB_CMD_MODIFY_SIGNATURE = 0x01
QQ_SUB_CMD_DELETE_SIGNATURE = 0x02
QQ_SUB_CMD_GET_SIGNATURE = 0x03
QQ_SUB_CMD_GET_USER_PROPERTY = 0x01
QQ_SUB_CMD_GET_WEATHER = 0x01

QQ_FILE_CMD_HEART_BEAT = 0x0001
QQ_FILE_CMD_HEART_BEAT_ACK = 0x0002
QQ_FILE_CMD_TRANSFER_FINISHED = 0x0003
QQ_FILE_CMD_FILE_OP = 0x0007
QQ_FILE_CMD_FILE_OP_ACK = 0x0008
QQ_FILE_CMD_SENDER_SAY_HELLO = 0x0031
QQ_FILE_CMD_SENDER_SAY_HELLO_ACK = 0x0032
QQ_FILE_CMD_RECEIVER_SAY_HELLO = 0x0033
QQ_FILE_CMD_RECEIVER_SAY_HELLO_ACK = 0x0034
QQ_FILE_CMD_NOTIFY_IP_ACK = 0x003C
QQ_FILE_CMD_PING = 0x003D
QQ_FILE_CMD_PONG = 0x003E
QQ_FILE_CMD_YES_I_AM_BEHIND_FIREWALL = 0x0040
QQ_FILE_CMD_REQUEST_AGENT = 0x0001
QQ_FILE_CMD_CHECK_IN = 0x0002
QQ_FILE_CMD_FORWARD = 0x0003
QQ_FILE_CMD_FORWARD_FINISHED = 0x0004
QQ_FILE_CMD_IT_IS_TIME = 0x0005
QQ_FILE_CMD_I_AM_READY = 0x0006

command_str = {
    0x0001: "QQ_CMD_LOGOUT",
    0x0002: "QQ_CMD_KEEP_ALIVE",
    0x0004: "QQ_CMD_MODIFY_INFO",
    0x0005: "QQ_CMD_SEARCH_USER",
    0x0006: "QQ_CMD_GET_USER_INFO",
    0x0009: "QQ_CMD_ADD_FRIEND",
    0x000A: "QQ_CMD_DELETE_FRIEND",
    0x000B: "QQ_CMD_ADD_FRIEND_AUTH",
    0x000D: "QQ_CMD_CHANGE_STATUS",
    0x0012: "QQ_CMD_ACK_SYS_MSG",
    0x0016: "QQ_CMD_SEND_IM",
    0x0017: "QQ_CMD_RECV_IM",
    0x001C: "QQ_CMD_REMOVE_SELF",
    0x001D: "QQ_CMD_REQUEST_KEY",
    0x0022: "QQ_CMD_LOGIN",
    0x0026: "QQ_CMD_GET_FRIEND_LIST",
    0x0027: "QQ_CMD_GET_ONLINE_OP",
    0x002D: "QQ_CMD_SEND_SMS",
    0x0030: "QQ_CMD_CLUSTER_CMD",
    0x0031: "QQ_CMD_TEST",
    0x003C: "QQ_CMD_GROUP_DATA_OP",
    0x003D: "QQ_CMD_UPLOAD_GROUP_FRIEND",
    0x003E: "QQ_CMD_FRIEND_DATA_OP",
    0x0058: "QQ_CMD_DOWNLOAD_GROUP_FRIEND",
    0x005C: "QQ_CMD_FRIEND_LEVEL_OP",
    0x005E: "QQ_CMD_PRIVACY_DATA_OP",
    0x005F: "QQ_CMD_CLUSTER_DATA_OP",
    0x0061: "QQ_CMD_ADVANCED_SEARCH",
    0x0062: "QQ_CMD_REQUEST_LOGIN_TOKEN",
    0x0065: "QQ_CMD_USER_PROPERTY_OP",
    0x0066: "QQ_CMD_TEMP_SESSION_OP",
    0x0067: "QQ_CMD_SIGNATURE_OP",
    0x0080: "QQ_CMD_RECV_MSG_SYS",
    0x0081: "QQ_CMD_RECV_MSG_FRIEND_CHANGE_STATUS",
    0x00A6: "QQ_CMD_WEATHER_OP",
    0x00A7: "QQ_CMD_ADD_FRIEND_EX",
    0x00A8: "QQ_CMD_AUTHORIZE",
    0xFFFF: "QQ_CMD_UNKNOWN",
    0x0021: "_CMD_REQUEST_AGENT",
    # 0x0022: "_CMD_REQUEST_FACE",   # FIXME - dup dict key
    0x0023: "_CMD_TRANSFER",
    # 0x0026: "_CMD_REQUEST_BEGIN",  # FIXME - dup dict key
}


class QQBasicPacket(Packet):
    __hdr__ = (
        ('header_type', 'B', 2),
        ('source', 'H', 0),
        ('command', 'H', 0),
        ('sequence', 'H', 0),
        ('qqNum', 'L', 0),
    )


class QQ3Packet(Packet):
    __hdr__ = (
        ('header_type', 'B', 3),
        ('command', 'B', 0),
        ('sequence', 'H', 0),
        ('unknown1', 'L', 0),
        ('unknown2', 'L', 0),
        ('unknown3', 'L', 0),
        ('unknown4', 'L', 0),
        ('unknown5', 'L', 0),
        ('unknown6', 'L', 0),
        ('unknown7', 'L', 0),
        ('unknown8', 'L', 0),
        ('unknown9', 'L', 0),
        ('unknown10', 'B', 1),
        ('unknown11', 'B', 0),
        ('unknown12', 'B', 0),
        ('source', 'H', 0),
        ('unknown13', 'B', 0),
    )


class QQ5Packet(Packet):
    __hdr__ = (
        ('header_type', 'B', 5),
        ('source', 'H', 0),
        ('unknown', 'H', 0),
        ('command', 'H', 0),
        ('sequence', 'H', 0),
        ('qqNum', 'L', 0),
    )
