from package.utils import change_dateime




# Telegram 报警模板
def tg_alertd(c):
    alert_content = '''
    ```python
    告警类型: %(TYPE)s
    告警任务: %(JOB)s
    告警级别: %(STATUS)s
    告警主机: %(INSTANCE)s
    主机用途：%(ENV)s
    告警主题: %(SUMMARY)s
    告警详情: %(DESCRIPTION)s
    触发时间: %(STARTAT)s
    详情图表: %(GENERATORURL)s
    ```
    ''' % dict(
            TYPE         = c['labels']['alertname'],
            JOB          = c['labels']['job'],
            STATUS       = c['labels']['severity'],
            INSTANCE     = c['labels']['instance'],
            ENV          = c['labels']['env'],
            SUMMARY      = c['annotations']['summary'],
            DESCRIPTION  = c['annotations']['description'],
            STARTAT      = change_dateime(c['startsAt']),
            GENERATORURL = c['generatorURL'],
        )
    return alert_content

# Telegram 恢复模板
def tg_resolved(c):
    resolved_content = '''
    ```python
    恢复类型: %(TYPE)s
    恢复主机: %(INSTANCE)s
    恢复主题: %(SUMMARY)s
    触发时间: %(STARTAT)s
    恢复时间: %(ENDSAT)s
    ```
    ''' % dict(
                TYPE        = c['labels']['alertname'],
                INSTANCE    = c['labels']['instance'],
                SUMMARY     = c['annotations']['summary'],
                STARTAT     = change_dateime(c['startsAt']),
                ENDSAT      = change_dateime(c['endsAt']),
            )
    return resolved_content



# Email 报警模板
def email_altertd(c):
    alert_content = '''
    ===================<br>
    告警类型: %(TYPE)s<br>
    告警任务: %(JOB)s<br>
    告警级别: %(STATUS)s<br>
    告警主机: %(INSTANCE)s<br>
    主机用途：%(ENV)s<br>
    告警主题: %(SUMMARY)s<br>
    告警详情: %(DESCRIPTION)s<br>
    触发时间: %(STARTAT)s<br>
    详情图表: %(GENERATORURL)s<br>
    ===================<br>
    '''% dict(
            TYPE         = c['labels']['alertname'],
            JOB          = c['labels']['job'],
            STATUS       = c['labels']['severity'],
            INSTANCE     = c['labels']['instance'],
            ENV          = c['labels']['env'],
            SUMMARY      = c['annotations']['summary'].replace(" ",""),
            DESCRIPTION  = c['annotations']['description'].replace(" ",""),
            STARTAT      = change_dateime(c['startsAt']),
            GENERATORURL = c['generatorURL'],
        )
    return alert_content


# Email 报警模板
def email_resolved(c):
    resolved_content = '''
    ===================<br>
    恢复类型: %(TYPE)s<br>
    恢复主机: %(INSTANCE)s<br>
    恢复主题: %(SUMMARY)s<br>
    触发时间: %(STARTAT)s<br>
    恢复时间: %(ENDSAT)s<br>
    ===================<br>
    ''' % dict(
                TYPE        = c['labels']['alertname'],
                INSTANCE    = c['labels']['instance'],
                SUMMARY     = c['annotations']['summary'].replace(" ",""),
                STARTAT     = change_dateime(c['startsAt']),
                ENDSAT      = change_dateime(c['endsAt']),
            )
    return resolved_content

