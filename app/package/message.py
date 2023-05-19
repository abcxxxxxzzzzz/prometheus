
import json
from typing import List
import telebot
import smtplib
from email.mime.text import MIMEText
import requests
import logging
from package.schema import AlertType
from package.config import global_settings
from package.utils import get_today
from package.templates import tg_alertd, tg_resolved,email_altertd, email_resolved

logger = logging.getLogger(__name__)


class SendMessages():
    def __init__(self):
        self.content = "Hello World"

        self.TG_mode = "Markdown"

        self.EM_subtype = "html"

        self.DD_headers = {'Content-Type': 'application/json;charset=utf-8'}
        self.DD_message = { "msgtype": "text", "text": { "content": self.content }, "at": { "isAtAll": True }}


    async def get_tg_content(self, contents):
        alterd_content = get_today(hms=True)
        resolved_content = ""
        for _a in contents:
            if _a['status'] == "firing":
                alterd_content = alterd_content + tg_alertd(_a)
            elif _a['status'] == "resolved":
                resolved_content = resolved_content + tg_resolved(_a)

        content = alterd_content + resolved_content

        return content

    async def get_email_content(self, contents):
        resolved_content = ""
        for _a in contents:
            if _a['status'] == "firing":
                 alterd_content = alterd_content + email_altertd(_a)
            elif _a['status'] == "resolved":
                resolved_content = resolved_content + email_resolved(_a)

        content = alterd_content + resolved_content

        return content
    

    async def toTelegram(self, tg_id: int, tg_token: str):
        bot = telebot.TeleBot(tg_token) 
        bot.send_message(tg_id, self.content, parse_mode=self.TG_mode)


    async def toEmail(self, host: str, username: str, password: str, from_email, title: str,  accept_email: List):
        msg            = MIMEText(self.content, _subtype=self.EM_subtype)
        msg['Subject'] = title
        msg['From']    = from_email
        msg['To']      = ','.join(accept_email)

        # server = smtplib.SMTP_SSL()  # 163 -> 465 TSL端口
        server = smtplib.SMTP()
        server.connect(host)
        server.login(username, password)
        server.sendmail(from_email, accept_email, msg.as_string())
        server.close()


    async def toDingding(self,  webhook: str):
        message_json = json.dumps(self.DD_message)
        requests.post(url=webhook, data=message_json, headers=self.DD_headers)
        # return info.text


    async def switch(self, contents: any, _type: str):
        # self.content = content

        try:
            if _type == AlertType.email.value:
                self.content = await self.get_email_content(contents)
                await self.toEmail(
                    host     = global_settings.smtp_host,
                    username = global_settings.smtp_user,
                    password = global_settings.smtp_pass,
                    from_email = global_settings.smtp_from,
                    title = global_settings.accept_title,
                    accept_email = global_settings.accept_email
                )
                return True
                
            elif _type == AlertType.dingding.value:
                await self.toDingding(global_settings.dingding_webhook)
                return True

            elif _type == AlertType.telegram.value:
                self.content = await self.get_tg_content(contents)
                await self.toTelegram(global_settings.tg_id, global_settings.tg_token)
                return True
            else:
                return False
        except Exception as e:
            from datetime import datetime
            logger.error(f'ERROR: {datetime.now()} : {str(e)}')
            return False
