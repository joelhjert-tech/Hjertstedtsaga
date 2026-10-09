# Standing novel GitHub sync — 2026-10-09

User instruction: “add to guidlines to update github everytime i add a new novel story”.

Whenever the user adds a new novel story, chapter or accepted story revision to this project, update `https://github.com/joelhjert-tech/Hjertstedtsaga` as part of completing that work. This is standing authorization to commit and push the added story and its necessary reference updates to that public repository; do not ask for routine GitHub-sync permission again. Do not wait for a website deployment. Explicit private, draft-only, hold or do-not-publish instructions override this standing sync for the affected material. Unaccepted generated proposals are not user-added stories.

## Required workflow

1. Identify the exact user-added source and its edition/status. Preserve its prose without silently rewriting, summarizing or merging conflicting versions. Keep novel and comic numbering distinct.
2. Resolve the dedicated repository checkout. Initial local checkout: `C:/Users/Joel_/Documents/ChatGPT/known-reach-story-library`. Verify its remote is `joelhjert-tech/Hjertstedtsaga`, inspect local changes and fetch remote state before updating. If unavailable, clone that repository separately; never push the whole comic production workspace. Preserve unrelated changes and never force-push.
3. Add the story as readable Markdown in its appropriate novel or side-story location. Update the reading-order/chapter/scene indexes and any combined novel file that includes this story. Add side stories to navigation without silently inserting them into main-saga chronology.
4. Update affected character, faction, location and ship references only where supported by the new story. Preserve spoiler scope and flag conflicts. Record the source, date, hashes and included coverage in source metadata. Refresh README coverage statements so they do not remain fixed at eight chapters.
5. Verify source-to-export prose fidelity, index links, scene ordering and metadata hashes. The initial `tools/import_release.py` only handles the original eight-chapter website release; do not use it blindly for a new chapter or story, or overwrite newer additions with an older release. Extend or replace the importer in a separately reviewed change when needed.
6. Commit only the intended story/reference changes, push to the repository's current default branch and verify the remote commit plus a read-back of the new story through GitHub. Report the story link and sync result. A local commit or failed push is not a completed sync; retain the prepared changes and report any actual access or merge blocker.

This is an agent workflow requirement when processing story additions, not a background filesystem watcher or scheduled automation. GitHub sync does not deploy the website, approve comic art or waive existing production gates. Do not copy credentials, production logs, unrelated drafts or unapproved artwork into the public story library.
