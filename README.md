# Known Reach Story Library

A searchable writing reference for **Tales from the Known Reach / The Shattered Lane**.

## Start here

- [Novel chapter and scene index](novel/INDEX.md)
- [Complete novel, chapters 1–8](novel/complete-novel.md)
- [Characters, factions, locations, ships and other published lore](reference/INDEX.md)
- [Source edition and integrity manifest](sources/manifest.json)
- [Old-to-revised chapter/scene mapping](sources/novel-revision-map.json)

The first import is the text from website release `issue03-2026-10-08-v01`, copied on 9 October 2026. Chapter files preserve the published prose. Scene indexes are navigation aids, not generated plot summaries. Under the [standing sync guideline](guidelines/novel-github-sync-v01.md), agents must update this repository whenever the user adds a new novel story, chapter or accepted revision. This is a task completion requirement, not a background watcher.

## Use in a writing chat

Repository: https://github.com/joelhjert-tech/Hjertstedtsaga

This is the public repository selected by the owner. It contains already-published story and lore text. Connect GitHub in the ChatGPT/Codex surface you use and select this repository for reliable authenticated retrieval. Public links can also be read where web access supports them, but a link does not guarantee that every chat can retrieve its contents. If the chat cannot read it, upload `novel/complete-novel.md` or the relevant chapter instead.

Suggested prompt:

> Use https://github.com/joelhjert-tech/Hjertstedtsaga as my story reference. Read README.md and novel/INDEX.md. Before helping me write, retrieve the relevant novel scenes and reference dossiers. Recap what matters, cite chapter and scene, and distinguish established facts from suggestions. Do not invent missing continuity. My writing point is: [chapter/scene]. Avoid spoilers beyond that point.

For Codex on this computer, open this repository folder as a project. For Codex Cloud, select this GitHub repository when creating an environment; see the [official environment instructions](https://learn.chatgpt.com/docs/environments/cloud-environments).

## Authority and maintenance

The novel is the source for events in this edition. Website dossiers supplement it and may cover different points in the story; their stated scopes are preserved. Report conflicts rather than silently reconciling them. Comic issue numbering and historical four-chapter numbering are different from this revised eight-chapter novel.

This reference library does not supersede the production workspace's canon locks, approved visual assets, image gates or publication approvals. No unpublished drafts, production logs, artwork or credentials are included.

Sync new user-added stories directly from their exact source; a website release is not a prerequisite. Follow the standing guideline to update navigation, references and provenance, commit, push and verify. Explicit private, draft-only or hold instructions remain controlling. Changes here do not publish to the website.

For the original eight-chapter website snapshot only, `python tools/import_release.py PATH_TO_RELEASE_SITE --release RELEASE_NAME` imports an explicitly selected approved release and verifies prose fidelity. This importer is fixed to eight chapters: extend it before using it for additional chapters, and never let an older release overwrite newer story additions. Inspect removed/renamed entries; it does not delete old files.
