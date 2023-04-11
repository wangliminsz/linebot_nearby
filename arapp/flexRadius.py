# import os
# import time

import random

# ======LINE API=========
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
# =======================

def flex_Radius(thisUser):

    print("hello flex Radius-----------------------")

    message = TemplateSendMessage(
                        alt_text='Choose Radius',
                        template=CarouselTemplate(
                            columns=[
                                CarouselColumn(
                                    # thumbnail_image_url='https://example.com/item1.jpg',
                                    title='Menu',
                                    text='Choose Radius:',
                                    actions=[
                                        PostbackTemplateAction(
                                            label='Not Specified',
                                            text='Radius not specified',
                                            data='RRRRDDDD&' + thisUser + '&distance'
                                        ),
                                        PostbackTemplateAction(
                                            label='1km',
                                            text='Radius 1km',
                                            data='RRRRDDDD&' + thisUser + '&1km'
                                        ),
                                        PostbackTemplateAction(
                                            label='2km',
                                            text='Radius 2km',
                                            data='RRRRDDDD&' + thisUser + '&2km'
                                        ),

                                    ]
                                ),

                                CarouselColumn(
                                    # thumbnail_image_url='https://example.com/item1.jpg',
                                    title='Menu',
                                    text='Choose Radius:',
                                    actions=[
                                        PostbackTemplateAction(
                                            label='5km',
                                            text='Radius 5km',
                                            data='RRRRDDDD&' + thisUser + '&5km'
                                        ),
                                        PostbackTemplateAction(
                                            label='10km',
                                            text='Radius 10km',
                                            data='RRRRDDDD&' + thisUser + '&10km'
                                        ),
                                        PostbackTemplateAction(
                                            label='15km or Above',
                                            text='15km or Above',
                                            data='RRRRDDDD&' + thisUser + '&50km'
                                        ),
                                    ]
                                ),
                            ]
                        )
                    )

    return message



    # radiusFlex = {
    #     "type": "carousel",
    #     "contents": [
    #         {
    #         "type": "bubble",
    #         "size": "kilo",
    #         "header": {
    #             "type": "box",
    #             "layout": "vertical",
    #             "contents": [
    #             {
    #                 "type": "text",
    #                 "text": "Radius",
    #                 "color": "#ffffff",
    #                 "align": "start",
    #                 "size": "md",
    #                 "gravity": "center"
    #             }
    #             ],
    #             "backgroundColor": "#27ACB2",
    #             "paddingTop": "19px",
    #             "paddingAll": "12px",
    #             "paddingBottom": "16px"
    #         },
    #         "body": {
    #             "type": "box",
    #             "layout": "vertical",
    #             "contents": [
    #             {
    #                 "type": "button",
    #                 "action": {
    #                 "type": "postback",
    #                 "label": "action",
    #                 "data": "hello"
    #                 },
    #                 "height": "sm"
    #             },
    #                         {
    #                 "type": "button",
    #                 "action": {
    #                 "type": "postback",
    #                 "label": "action",
    #                 "data": "hello"
    #                 },
    #                 "height": "sm"
    #             },
    #                         {
    #                 "type": "button",
    #                 "action": {
    #                 "type": "postback",
    #                 "label": "action",
    #                 "data": "hello"
    #                 },
    #                 "height": "sm"
    #             },
    #                         {
    #                 "type": "button",
    #                 "action": {
    #                 "type": "postback",
    #                 "label": "action",
    #                 "data": "hello"
    #                 },
    #                 "height": "sm"
    #             },
    #                         {
    #                 "type": "button",
    #                 "action": {
    #                 "type": "postback",
    #                 "label": "action",
    #                 "data": "hello"
    #                 },
    #                 "height": "sm"
    #             },
    #                         {
    #                 "type": "button",
    #                 "action": {
    #                 "type": "postback",
    #                 "label": "action",
    #                 "data": "hello"
    #                 },
    #                 "height": "sm"
    #             }

    #             ],
    #             "spacing": "xs",
    #             "paddingAll": "12px"
    #         },
    #         "styles": {
    #             "footer": {
    #             "separator": False
    #             }
    #         }
    #         }
    #     ]
    # }


    # ####

    # fmessage = FlexSendMessage(
    #         alt_text='Please input your #keyword', contents=radiusFlex)
    # return fmessage