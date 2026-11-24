# Leaderboard — One Sentence for a Traveler from 1800

Slug: `u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb`
Checked: 2026-11-24 ~13:05 WIB (06:05 UTC). Raw copy: `leaderboard.json` (this folder).

## Board state: BLIND

- `scores_visible: false`, `placements_held: true`, blind rounds 3x.
  Round 1 cut 2026-11-24 17:03 WIB (passed), round 2 cut 21:44 WIB tonight,
  final = deadline 2026-11-25 02:25 WIB (19:25 UTC).
- `entries: []` — no scores, no ranks visible to anyone. Nothing to copy from a top 10.
- Submissions: 481 at watcher discovery (~12:54 WIB) → 552 at this check (~13:05 WIB).
  Field is growing ~6/min; final heat takes the top 500 on the dev board, so with
  552+ entries the cut may actually bind — but every entry that passes the gate and
  is unrated also goes on, and the heat re-judges afresh (Swiss + top-12 playoff).
- `rank_key`: `judge` (pairwise win rate, Bradley-Terry). `tie_break`: `bytes`
  (smaller text wins ties, then earlier receipt). `submission_rule`: Force_Last.
- Prize: $2 total, top 10 (1st $0.63 … 10th $0.02). Free entry.

## What the field is doing (from public submission titles, GET /api/competitions/<slug>)

Word frequency across all 552 titles: road 143, library 133, post office 116,
letter 71, "every" 145, "joining" 40. The modal entry is some variant of
"a road joining every library / post office on earth, letters arrive in a blink".
Representative titles: "Every Library and Post Office, One Road", "A Road of Light",
"One road joining every library on earth", "A library and a post office in every
house at once", "Letters on Thin Wires", "A Letter Read Before the Ink Dries".

Implication: the library + post-office + road angle is saturated. An entry that
only repeats it can at best tie the modal entry and loses on the bytes tie-break
to shorter ones. To win pairwise it must do MORE explanatory work in the same
image: cover knowledge AND two-way communication, with a fresh speed image
(not "in a blink" / "before your tea cools", both already in play), and no
literally-false totality claim ("every house", "every book", "any page" all overclaim).

## Judge brief (RULES.txt, criteria in order)

1. Explains the modern internet to an 1800 traveler — what it is AND what it does.
2. Builds from what 1800 knows (road, post office, library), no post-1800 words.
3. Literally true — no claim that misleads a literal reader.
4. Every word earns its place in 200 chars; no filler, no crammed feature list.
5. One memorable image/phrase.
Plus: a single comparison may carry the whole sentence if true; cleverness alone
does not count; no ties — first differing criterion decides.

## Targets (from rank-recovery §2e + this bouty's RULES.txt)

- Dev rank ≤ #50 mid-phase is the usual judge-based target, but THIS bounty's heat
  is top **500** (not 80) and the field is ~552 and growing — the realistic target is
  simply: be clearly better than the modal library/road entry in pairwise judging,
  so the dev rate lands in the top 500 and the entry reaches the final heat, where
  Swiss + playoff decide the top 10.
- Tie-break: keep the sentence short among equals (ours: 168 bytes, ASCII-only).
- Do NOT chase a 15-minute submit: blind/judge-based, quality decides. But finish
  well before the round-2 cut (21:44 WIB) so the entry is judged in round 2.
- No secrets allowed in this bounty (provider keys only, unused); everything the
  entry runs must be in the repo. Size is the ENTRY TEXT's bytes, not repo size.
