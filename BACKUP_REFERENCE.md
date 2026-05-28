# 🔒 PERMANENT BACKUP REFERENCE

## ⚠️ IMPORTANT — READ THIS BEFORE MAKING CHANGES

This project has a **permanent stable backup branch** that should NEVER be deleted.

---

## Backup Branch Details

| Key | Value |
|---|---|
| **Branch Name** | `stable-backup-may28` |
| **Created On** | May 28, 2026 |
| **Status** | ✅ Fully Working — All features verified |
| **Commit** | Latest commit on `main` as of May 28, 2026 1:18 PM IST |

---

## What This Backup Contains (All Working)

1. **9 Subject Cards** — Philosophy of Education, Philosophy of AI, English for BA, Literary Malayalam, History of Keralam, Sociology, Fundamentals of Ethics, Micro Economics, Development Issues
2. **Academic Progress Dashboard** — 9-row table with English + Malayalam upload counts
3. **Real-Time Presence System** — Shows online user count + username cards (presence_v2 node)
4. **Active Website Users** — Community section showing ALL registered usernames from Firebase `users` node, sorted A-Z, with dynamic count
5. **Real-Time Chat** — Full chat system with admin moderation
6. **Theme System** — 14 themes with persistence
7. **Username Lock** — Subjects locked until user sets a name
8. **Issue Report Form** — Web3Forms integration

---

## How to Restore From This Backup

If the `main` branch gets broken, run:

```bash
# Option 1: Reset main to the backup
git checkout main
git reset --hard stable-backup-may28
git push origin main --force

# Option 2: Restore only index.html
git checkout stable-backup-may28 -- index.html
git commit -m "Restored index.html from stable backup"
git push origin main
```

---

## Firebase Configuration

| Key | Value |
|---|---|
| **Database URL** | `https://academic-portal-135fd-default-rtdb.firebaseio.com/` |
| **Project ID** | `academic-portal-135fd` |
| **Key Nodes** | `users`, `active_users`, `presence_v2`, `chat_messages` |
| **Community Data Source** | `users` node (primary), `active_users` (legacy) |
| **Online Tracking** | `presence_v2` node with 10s heartbeat, 35s stale check |

### Firebase Rules (Required)

```json
{
  "rules": {
    ".read": true,
    "presence_v2": { ".write": true },
    "users": { ".write": true },
    "active_users": { ".write": true },
    "chat_messages": { ".write": true }
  }
}
```

---

## 🤖 NOTE FOR AI ASSISTANTS

If you are an AI assistant working on this project:

1. **DO NOT** modify the layout, structure, or styling without explicit user permission
2. **DO NOT** delete or overwrite Firebase data nodes
3. **ALWAYS** check this backup branch exists before making destructive changes
4. **IF SOMETHING BREAKS** — restore from `stable-backup-may28` branch
5. The `Active Website Users` section pulls ALL usernames from Firebase `users` node — do not add static/placeholder members
6. The `Online Now` section uses `presence_v2` with `onDisconnect().remove()` pattern
7. **Deployment** is via Cloudflare Pages (auto-deploys from `main` branch)

---

## Project Owner

- **Admin**: Hashim (ameenulhashim)
- **Portal**: BA Calicut University Unofficial Notes
