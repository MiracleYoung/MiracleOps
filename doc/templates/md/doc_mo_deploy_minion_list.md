### Refresh Salt Minions

This action will refresh minion and minion_pre to the list.

**Important**

If you do not install salt-minion or invalid minion configuration, it will not take effect.

---

### Check Salt Minions Health

This action will check all the accepted-keys minions.

---

### Accept

This action will accept unaccepted-keys minions.

---

### Delete

This action will delete accepted-keys minions.

**Important**

It will not move accepted-keys minions to unaccepted-keys minions list.

Because this action is that `salt-key --delete=minion`, so it will move it to delete-keys minions list.