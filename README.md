# Known Reach Story Library

## New revised standalone story — 27 October 2026

[The House That Would Not Kneel](side-stories/the-house-that-would-not-kneel.md) follows a Directorate analyst through the Cairn’s Wake campaign. Owner-supplied revised prose is retained exactly for audiobook and illustration review. Its campaign remains **proposed standalone continuity**, separate from the committed main novel. No website or comic publication follows from this sync. [Source record](sources/house-would-not-kneel-2026-10-27.json).

A searchable writing reference for **Tales from the Known Reach / The Shattered Lane**.

## Start here

- [Novel chapter and scene index](novel/INDEX.md)
- [Complete novel, chapters 1–8](novel/complete-novel.md)
- [Standalone side stories](side-stories/INDEX.md)
- [Characters, factions, locations, ships and other published lore](reference/INDEX.md)
- [Vharok Brood — new faction README and slender ship study](reference/factions/vharok-brood/README.md)
- [Standing novel-writing guidelines](guidelines/novel-writing-guidelines.md)
- [Source edition and integrity manifest](sources/manifest.json)
- [Old-to-revised chapter/scene mapping](sources/novel-revision-map.json)

The first import is the text from website release `issue03-2026-10-08-v01`, copied on 9 October 2026. The current repository edition includes the owner-directed revision below; it is no longer an exact copy of that website edition. Scene indexes are navigation aids, not generated plot summaries. Under the [standing sync guideline](guidelines/novel-github-sync-v01.md), agents must update this repository whenever the user adds a new novel story, chapter or accepted revision. This is a task completion requirement, not a background watcher.

## New side story — 26 October 2026

[The Kharad Trial: The Things Beneath the Ash](side-stories/the-kharad-trial.md) follows five Talyrn candidates through a containment failure on Vaerith. The owner authorized the reviewed fixes: credible rescue decisions, independent authentication, clear injuries and escape geography, institutional accountability and a truthful survivor count. The eight-chapter main novel remains unchanged. [Source record](sources/kharad-trial-2026-10-26.json).

## New faction reference — 24 October 2026

The owner added [the Vharok Brood](reference/factions/vharok-brood/README.md), an intelligent predatory alien civilization whose vessels are deliberately **advanced, narrow and sleek** compared with regular faction hulls. The faction dossier includes an embedded [Splitfang frigate silhouette](reference/factions/vharok-brood/splitfang-silhouette.svg) and a separate [ship-class sheet](reference/fleet-classes/vharok-splitfang.md). The user-provided creature reference image was not republished. The SVG is a design-reference diagram, **not approved production artwork**.

This is wider-setting lore for the proposed forgotten-gate/Directorate mystery; it does not alter or confirm events within the currently committed eight-chapter novel. The drafted Chapter 9 continuation remains uncommitted.

## Latest novel revision

On 19 October 2026, the **House Rivalry, Banter and Victory Traditions** revision strengthened Chapters 02–08: distinct family voices, veteran competition, running bottle debts, disciplined teamwork, a Kestrel victory feast and remembrance. **Chapter 01 is unchanged**, as explicitly requested. All eight chapter titles, 116 scene identities, established mission outcomes and major continuity remain. The character, House and Winter Reserve dossiers retain their original website text and add clearly labeled writing supplements. See the [revision coverage and source record](sources/house-rivalry-2026-10-19.json).

The [standing writing guidelines](guidelines/novel-writing-guidelines.md) make this culture part of future writing while preserving the Charter, military orders, small servings and guest protections. This repository update does not deploy the website or revise comic pages.

## Previous reference update

On 10 October 2026, fourteen published ship dossiers and the independent-operator grouping were added from website release `new-ships-2026-10-10-v01`. This includes **The Unanswered Crown**, **Last Covenant**, **Silent Meridian** and **Patient Thunder**. Twelve ship dossiers link to published artwork; Bulwark and Threshold remain lore-only while their artwork findings are unresolved. Novel chapters and scene order are unchanged. See the [ship update source record](sources/new-ships-2026-10-10.json).

## Use in a writing chat

Repository: https://github.com/joelhjert-tech/Hjertstedtsaga

This is the public repository selected by the owner. It contains already-published story and lore text. Connect GitHub in the ChatGPT/Codex surface you use and select this repository for reliable authenticated retrieval. Public links can also be read where web access supports them, but a link does not guarantee that every chat can retrieve its contents. If the chat cannot read it, upload `novel/complete-novel.md` or the relevant chapter instead.

Suggested prompt:

> Use https://github.com/joelhjert-tech/Hjertstedtsaga as my story reference. Read README.md and novel/INDEX.md. Before helping me write, retrieve the relevant novel scenes and reference dossiers. Recap what matters, cite chapter and scene, and distinguish established facts from suggestions. Do not invent missing continuity. My writing point is: [chapter/scene]. Avoid spoilers beyond that point.

For Codex on this computer, open this repository folder as a project. For Codex Cloud, select this GitHub repository when creating an environment; see the [official environment instructions](https://learn.chatgpt.com/docs/environments/cloud-environments).

## Authority and maintenance

The novel is the source for events in this edition. Website dossiers supplement it and may cover different points in the story; their stated scopes are preserved. Report conflicts rather than silently reconciling them. Comic issue numbering and historical four-chapter numbering are different from this revised eight-chapter novel.

This reference library does not supersede the production workspace's canon locks, approved visual assets, image gates or publication approvals. No unpublished novel drafts, production logs, approved production artwork or credentials are included. The new Vharok SVG is a reference-only technical silhouette, not a finalized comic or production asset.

Sync new user-added stories directly from their exact source; a website release is not a prerequisite. Follow the standing guideline to update navigation, references and provenance, commit, push and verify. Explicit private, draft-only or hold instructions remain controlling. Changes here do not publish to the website.

For the original eight-chapter website snapshot only, `python tools/import_release.py PATH_TO_RELEASE_SITE --release RELEASE_NAME` imports an explicitly selected approved release and verifies prose fidelity. This importer is fixed to eight chapters: extend it before using it for additional chapters, and never let an older release overwrite newer story additions. Inspect removed/renamed entries; it does not delete old files.
