def can_cancel(status, owner, actor):
    """Return whether this synthetic request may be cancelled."""
    return status == "pending" and bool(owner)
