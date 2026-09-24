# Current source check / 本轮来源核验

Checked: **2026-09-24**. This record separates fresh checks from the source repository’s historical notes. The case titles and learning points below are editorial descriptions. Community model labels are the posters’ claims, not independently authenticated render records.

## Official material

The [official model page](https://seed.bytedance.com/en/seedance2_5) and [official launch article](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) were retrieved this round. The article is dated 2026-07-31. Ten video URLs were extracted from its HTML, including the opening film; all returned HTTP 200 and `video/mp4` to HEAD requests. [Nine teaching examples](official-examples.md) link directly to those official files. At the initial link-check stage no media was downloaded or end-to-end playback tested. A later still-extraction check is recorded below.

## X community material

Searches included `site:x.com "Seedance 2.5" "prompt"`, account-specific searches, and exact post IDs. Broad searches mostly returned X automated trend summaries; these are discovery aids, not reliable evidence of a particular post’s prompt, model, or popularity. An exact-ID search found a third-party repost of x11; that repost was not treated as native X verification.

Native X access was attempted for x01, x11, and x12. x01 returned HTTP 403; x11 and x12 failed retrieval. **No native X post or engagement count was verified this round.**

The twelve original-post candidates were located through the [FLAQ source repository](https://github.com/flaqai/awesome_seedance_2_5), then fetched afresh through the public FxTwitter metadata mirror. All twelve mirror requests returned HTTP 200 with a successful response, matching author handles, a Seedance 2.5 label, and prompt text. Links below lead to the original authors, not the mirror.

| Case | Original author and post | What readers can study |
|---|---|---|
| x01-galley-food-comedy | [@Goodmanprotocol](https://x.com/Goodmanprotocol/status/2099186117769822462) | Stage an action, a reaction, then a payoff. |
| x02-one-garment-fashion | [@Goodmanprotocol](https://x.com/Goodmanprotocol/status/2095216981624721691) | Keep the garment fixed while changing styling. |
| x03-rainy-pet-selfie | [@Strength04_X](https://x.com/Strength04_X/status/2098256490238755226) | Make the interruption visibly cause the reaction. |
| x04-live-action-doodle | [@Strength04_X](https://x.com/Strength04_X/status/2095748874942263601) | Define where live action and drawn elements interact. |
| x05-minidv-everyday | [@john_my07](https://x.com/john_my07/status/2090287853532266748) | Specify camera imperfections with restraint. |
| x06-two-person-vlog | [@Strength04_X](https://x.com/Strength04_X/status/2097968347430482177) | Track who holds the prop across cuts. |
| x07-talent-show-reversal | [@Strength04_X](https://x.com/Strength04_X/status/2090399966988550435) | Build a clear setup and reversal; retain the source credit to @techhalla. |
| x08-pressed-flower-tutorial | [@Strength04_X](https://x.com/Strength04_X/status/2084269139556761919) | Keep the craft steps readable and in order. |
| x09-energy-action-geography | [@Strength04_X](https://x.com/Strength04_X/status/2096147092188311749) | Preserve positions and action direction during escalation. |
| x10-day-trip-story-arc | [@Goodmanprotocol](https://x.com/Goodmanprotocol/status/2087165084397420849) | Give the day a beginning, change, and ending. |
| x11-visible-object-handover | [@AIwithkhan](https://x.com/AIwithkhan/status/2096424933366931946) | Show the object passing between hands. |
| x12-tropical-location-sound | [@RishuaVR](https://x.com/RishuaVR/status/2089204108175741157) | Give ambient sound a clear physical source. |

### Mirror-reported engagement snapshot

These numbers were returned by FxTwitter on 2026-09-24. They are approximate third-party snapshots, not audited native X counts. They can guide which examples to inspect first; they do not establish model quality, authentic views, or a popularity ranking. We describe these as community examples rather than independently verified viral examples.

| Case | Mirror views | Mirror likes | Mirror reposts | Metadata source |
|---|---:|---:|---:|---|
| x01-galley-food-comedy | 49,796 | 805 | 90 | [Mirror response](https://api.fxtwitter.com/Goodmanprotocol/status/2099186117769822462) |
| x02-one-garment-fashion | 24,513 | 402 | 36 | [Mirror response](https://api.fxtwitter.com/Goodmanprotocol/status/2095216981624721691) |
| x03-rainy-pet-selfie | 9,939 | 236 | 21 | [Mirror response](https://api.fxtwitter.com/Strength04_X/status/2098256490238755226) |
| x04-live-action-doodle | 22,730 | 398 | 44 | [Mirror response](https://api.fxtwitter.com/Strength04_X/status/2095748874942263601) |
| x05-minidv-everyday | 48,043 | 300 | 19 | [Mirror response](https://api.fxtwitter.com/john_my07/status/2090287853532266748) |
| x06-two-person-vlog | 2,921 | 52 | 1 | [Mirror response](https://api.fxtwitter.com/Strength04_X/status/2097968347430482177) |
| x07-talent-show-reversal | 16,660 | 362 | 23 | [Mirror response](https://api.fxtwitter.com/Strength04_X/status/2090399966988550435) |
| x08-pressed-flower-tutorial | 55,951 | 228 | 25 | [Mirror response](https://api.fxtwitter.com/Strength04_X/status/2084269139556761919) |
| x09-energy-action-geography | 14,382 | 186 | 20 | [Mirror response](https://api.fxtwitter.com/Strength04_X/status/2096147092188311749) |
| x10-day-trip-story-arc | 49,677 | 413 | 35 | [Mirror response](https://api.fxtwitter.com/Goodmanprotocol/status/2087165084397420849) |
| x11-visible-object-handover | 614,495 | 4,277 | 240 | [Mirror response](https://api.fxtwitter.com/AIwithkhan/status/2096424933366931946) |
| x12-tropical-location-sound | 3,655,618 | 4,742 | 416 | [Mirror response](https://api.fxtwitter.com/RishuaVR/status/2089204108175741157) |

## What remains historical or untested

- The inherited `x-showcase-sources.json` records video dimensions, durations, and media availability checked by the source project on 2026-09-20. Recorded dimensions and durations remain historical. This round rechecked URL availability and content types only, not dimensions, duration or playback.
- A requested aspect ratio or a phrase such as “4K” in a prompt is not evidence of the uploaded video’s actual format. Preserve the recorded differences between brief and published media.
- The repository’s adapted prompts are editorial drafts, not the exact prompts that produced the linked examples. No Seaimagine generation or reproduction test was performed for this source check.
- Official demonstrations do not establish that every third-party interface exposes every model feature. Current product controls, quotas, and supported inputs must be checked on the product itself.
- Original creators retain ownership of their community media. Linking an example does not imply endorsement, a Seaimagine customer relationship, or permission to relicense the source media.

## Fresh media reachability check

On 2026-09-24, all 12 community MP4 URLs and all 12 thumbnail URLs returned HTTP 200 with the expected `video/mp4` or `image/jpeg` content type. See the [machine-readable results](../data/media-link-check.json). This is a separate current check; the original 2026-09-20 source record remains unchanged. No end-to-end playback was tested. All 30 unique homepage brand URLs also responded successfully using a browser user agent; [results and request limitations](../data/brand-link-check.json).

## Official still extraction

On 2026-09-24, the three official videos selected for the homepage were downloaded temporarily for frame extraction. Six frames were extracted and visually inspected: backstage/stage at 3/24 seconds, concert hall/choir at 12/27 seconds, and the official breakfast camera comparison at 6/9 seconds. These timestamps refer to the hosted demonstration files, including introductory cards where present, not the prompt timelines.

Frames are proportionally resized to 800 pixels wide and exported as JPEG. No compositing, retouching, re-generation or removal of embedded labels was applied. The breakfast frames retain the official side-by-side comparison. Local assets and their original URLs are mapped in [the case manifest](official-homepage-cases.json).

This confirms the selected visible frames, not uninterrupted playback, sound synchronization or reproduction on SeaImagine. The homepage uses complete editorial prompt expansions for the same scenes, with added production choices, rather than verbatim official instructions. These expansions and the separate transfer exercises remain untested. ByteDance Seed retains rights in the excerpted official frames; these assets are excluded from the repository's MIT license.
