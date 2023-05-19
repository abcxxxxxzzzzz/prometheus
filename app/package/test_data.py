result = {
    "receiver": "telegram", 
    "status": "firing", 
    "alerts": [
        {
            "status": "resolved", 
            "labels": {
                "alertname": "ping主机", 
                "env": "web_url", 
                "instance": "http://98.net", 
                "job": "check-web-status", 
                "status": "严重告警"
            }, 
            "annotations": {
                "description": " 非要逼我报警么0%)", 
                "summary": " 主机ping不通了！"
            }, 
            "startsAt": "2023-05-06T10:02:33.742Z", 
            "endsAt": "2023-05-06T10:12:33.742Z", 
            "generatorURL": "http://es1:9090/graph?g0.expr=probe_success+%3D%3D+0&g0.tab=1", 
            "fingerprint": "8d9dc7e58f689ff1"
        }, 
        {
            "status": "firing", 
            "labels": {
                "alertname": "ping主机", 
                "env": "web_url", 
                "instance": "http://abc123129as.asdfasdl.com", 
                "job": "check-web-status", 
                "status": "严重告警"
            }, 
            "annotations": {
                "description": " 非要逼我报警么0%)", 
                "summary": " 主机ping不通了！"
            }, 
            "startsAt": "2023-05-06T10:02:33.742Z", 
            "endsAt": "0001-01-01T00:00:00Z", 
            "generatorURL": "http://es1:9090/graph?g0.expr=probe_success+%3D%3D+0&g0.tab=1", 
            "fingerprint": "8d6b898fd281c554"
        }, 
        {
            "status": "resolved", 
            "labels": {
                "alertname": "ping主机", 
                "group": "机房 正式 网络监控", 
                "instance": "192.168.26.235", 
                "job": "icmp_ping", 
                "ping": "192.168.26.235", 
                "status": "严重告警"
            }, 
            "annotations": {
                "description": " 非要逼我报警么0%)", 
                "summary": " 主机ping不通了！"
            }, 
            "startsAt": "2023-05-06T10:02:48.742Z", 
            "endsAt": "2023-05-06T10:09:33.742Z", 
            "generatorURL": "http://es1:9090/graph?g0.expr=probe_success+%3D%3D+0&g0.tab=1", 
            "fingerprint": "76eed1e08d409abb"
        }, 
        {
            "status": "firing", 
            "labels": {
                "alertname": "ping主机", 
                "group": "机房 正式 网络监控", 
                "instance": "192.168.31.206", 
                "job": "icmp_ping", 
                "ping": "192.168.31.206", 
                "status": "严重告警"
            }, 
            "annotations": {
                "description": " 非要逼我报警么0%)", 
                "summary": " 主机ping不通了！"
            }, 
            "startsAt": "2023-05-06T10:02:48.742Z", 
            "endsAt": "0001-01-01T00:00:00Z", 
            "generatorURL": "http://es1:9090/graph?g0.expr=probe_success+%3D%3D+0&g0.tab=1", 
            "fingerprint": "8f913bb2fdafaaa3"
        }, 
        {
            "status": "resolved", 
            "labels": {
                "alertname": "ping主机", 
                "group": "机房 正式 网络监控", 
                "instance": "192.168.4.37", 
                "job": "icmp_ping", 
                "ping": "192.168.4.37", 
                "status": "严重告警"
            }, 
            "annotations": {
                "description": " 非要逼我报警么0%)", 
                "summary": " 主机ping不通了！"
            }, 
            "startsAt": "2023-05-06T10:02:48.742Z", 
            "endsAt": "2023-05-06T10:09:33.742Z", 
            "generatorURL": "http://es1:9090/graph?g0.expr=probe_success+%3D%3D+0&g0.tab=1", 
            "fingerprint": "6677ecb4247ec97b"
        }
    ], 
    "groupLabels": {
        "alertname": "ping主机"
    }, 
    "commonLabels": {
        "alertname": "ping主机", 
        "status": "严重告警"
    }, 
    "commonAnnotations": {
        "description": " 非要逼我报警么0%)", 
        "summary": " 主机ping不通了！"
    }, 
    "externalURL": "http://es1:9093", 
    "version": "4", 
    "groupKey": "{}:{alertname=\"ping主机\"}", 
    "truncatedAlerts": 0
}