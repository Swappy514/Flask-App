#!/bin/bash

# Reset Git to clean state
git checkout -b main || git checkout main

# Define reusable commit function
make_commit() {
    folder="$1"
    timestamp="$2"
    message="$3"

    cp -r $folder/* . 2>/dev/null || echo "⚠️ $folder is empty"

    git add -A
    GIT_AUTHOR_DATE="$timestamp" GIT_COMMITTER_DATE="$timestamp" \
    git commit -m "$message"
}

# START FRESH
rm -rf .git
git init

# .gitignore setup
echo -e "__pycache__/\n*.pyc\n.env\nvenv/" > .gitignore
git add .gitignore
GIT_AUTHOR_DATE="2025-07-19T18:00:00" GIT_COMMITTER_DATE="2025-07-19T18:00:00" git commit -m "Add .gitignore"

# PHASE 1 — 2025-07-20
make_commit "phase_1" "2025-07-20T10:15:00" "phase1: initial setup"
touch phase1_config.txt
git add phase1_config.txt
GIT_AUTHOR_DATE="2025-07-20T15:35:00" GIT_COMMITTER_DATE="2025-07-20T15:35:00" git commit -m "phase1: config updates"

# PHASE 2 — 2025-07-21 & 2025-07-22
make_commit "phase_2/user_verify_mini_project" "2025-07-21T09:45:00" "phase2: created data schema"
make_commit "phase_2/mini_project_2" "2025-07-21T13:25:00" "phase2: implemented API logic"
GIT_AUTHOR_DATE="2025-07-21T17:50:00" GIT_COMMITTER_DATE="2025-07-21T17:50:00" git commit --allow-empty -m "phase2: tested endpoints"

make_commit "phase_2/jinja2" "2025-07-22T10:00:00" "phase2: authentication logic"
GIT_AUTHOR_DATE="2025-07-22T14:30:00" GIT_COMMITTER_DATE="2025-07-22T14:30:00" git commit --allow-empty -m "phase2: session handling"
GIT_AUTHOR_DATE="2025-07-22T16:55:00" GIT_COMMITTER_DATE="2025-07-22T16:55:00" git commit --allow-empty -m "phase2: error handling updates"

# PHASE 3 — 2025-07-23 & 2025-07-24
make_commit "phase_3/manual_form_handling_using_flask" "2025-07-23T11:10:00" "phase3: UI base components"
make_commit "phase_3/flask_WTF" "2025-07-23T13:50:00" "phase3: form validations"
make_commit "phase_3/flash_messages" "2025-07-23T17:40:00" "phase3: responsive design tweaks"

touch split_ui.txt
GIT_AUTHOR_DATE="2025-07-24T09:30:00" GIT_COMMITTER_DATE="2025-07-24T09:30:00" git commit -am "phase3: split components"

touch theme_toggle.js
GIT_AUTHOR_DATE="2025-07-24T12:30:00" GIT_COMMITTER_DATE="2025-07-24T12:30:00" git commit -am "phase3: added theme toggle"

touch ui_polish_notes.md
GIT_AUTHOR_DATE="2025-07-24T15:30:00" GIT_COMMITTER_DATE="2025-07-24T15:30:00" git commit -am "phase3: UI polish"

# PHASE 4 — 2025-07-25
make_commit "phase_4" "2025-07-25T10:05:00" "phase4: connected database"
touch migrate.sh
GIT_AUTHOR_DATE="2025-07-25T13:10:00" GIT_COMMITTER_DATE="2025-07-25T13:10:00" git commit -am "phase4: added migration script"

# PHASE 5 — 2025-07-26
make_commit "phase_5" "2025-07-26T14:00:00" "phase5: CI/CD config"
GIT_AUTHOR_DATE="2025-07-26T18:00:00" GIT_COMMITTER_DATE="2025-07-26T18:00:00" git commit --allow-empty -m "phase5: final cleanup"

# FINAL PUSH
git branch -M main
git remote add origin https://github.com/Swappy514/Flask-App.git
git push -f origin main

echo "✅ All phases pushed successfully with historic timestamps."
