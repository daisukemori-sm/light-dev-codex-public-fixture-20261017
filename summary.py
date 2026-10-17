def status_label(status):
    return {
        "pending": "申請中",
        "approved": "承認済み",
        "cancelled": "取り消し済み",
    }.get(status, status)
