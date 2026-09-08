# Duan 2026 Volume I authority and retrieval protocol

## Source identity `[E]`

- Guang-Ren Duan, *Fully Actuated System Approach: Volume I. Global Fully Actuated Systems*.
- Springer Nature Singapore, 2026.
- DOI: `10.1007/978-981-96-8395-6`.
- Zotero PDF: `/home/yzk/Zotero/storage/688CMT53/978-981-96-8395-6.pdf`.
- PDF pages: 513; file size: 8,540,455 bytes; tagged and unencrypted.
- SHA-256: `3ac437c2a236bbfe902a22401c535cb6787bae0a5b385cbb22efca609e223a78`.
- The book states a Creative Commons Attribution 4.0 International license.

This is the consolidated primary authority for the global-FAS branch. It is not the primary theorem source for SUB-FAS, substability, substabilization, or ROEA.

## Three-layer use

1. **Immutable source:** the Zotero PDF decides disputes.
2. **Search index:** a local SQLite FTS5 index locates candidate pages. Extracted text is a discovery aid, not formula authority.
3. **Curated references:** definitions, theorem cards, symbol rules, and proof templates enter the skill only after checking the PDF page.

Never place the full extracted book text in `SKILL.md` or a reference file.

## Build, search, and extract

Build or refresh the index:

```bash
python3 /home/yzk/.codex/skills/duan-hofas/scripts/build_volume1_index.py
```

Search by concepts:

```bash
python3 /home/yzk/.codex/skills/duan-hofas/scripts/search_volume1.py \
  --query 'arbitrary assignment closed-loop dynamics' --top 6
```

Search an exact phrase or extracted glyph sequence:

```bash
python3 /home/yzk/.codex/skills/duan-hofas/scripts/search_volume1.py \
  --literal 'minimum singular value' --top 10
```

Find an exact numbered result:

```bash
python3 /home/yzk/.codex/skills/duan-hofas/scripts/search_volume1.py \
  --label 'Theorem 5.1'
```

Search only theorem openings:

```bash
python3 /home/yzk/.codex/skills/duan-hofas/scripts/search_volume1.py \
  --query 'closed-loop system' --kind Theorem --top 8
```

Extract a narrow PDF-page range to the terminal:

```bash
python3 /home/yzk/.codex/skills/duan-hofas/scripts/extract_volume1_pages.py \
  --pdf-pages 120:124
```

The default index is `/home/yzk/.cache/duan-hofas/volume1.sqlite`. Rebuild it when the source checksum changes.

## Chapter router `[E]`

| Printed pages | Destination |
|---:|---|
| 1–48 | Ch. 1: introduction, framework overview, notation, eigenstructure preliminaries |
| 49–90 | Ch. 2: physical, single-order, multi-order, LTI/LTV, and feedback-linearizable global FAS models |
| 91–126 | Ch. 3: closed-loop assignment, nonlinear-to-linear conversion, feedback linearization, parameterization, examples |
| 127–160 | Ch. 4: disturbance attenuation and decoupling |
| 161–196 | Ch. 5: robust, adaptive, and robust-adaptive control |
| 197–226 | Ch. 6: strict-feedback systems with uniform dimensions |
| 227–258 | Ch. 7: strict-feedback systems with increasing dimensions |
| 259–302 | Ch. 8: nonaffine strict-feedback systems |
| 303–326 | Ch. 9: high-order backstepping for robust control |
| 327–346 | Ch. 10: high-order backstepping for adaptive control |
| 347–376 | Ch. 11: observer-based control |
| 377–404 | Ch. 12: robust stabilization of Type I systems |
| 405–420 | Appendix A: controller-parameterization solutions |
| 421–476 | Appendix B: proofs of selected theorems |
| 477–500 | bibliography |
| 501–503 | index and end matter |

## Evidence workflow

For a definition, theorem, formula, or writing pattern:

1. search with two or more discriminating terms;
2. record the returned PDF page, inferred printed page, and chapter;
3. extract no more than the necessary page range;
4. inspect the PDF rendering for matrices, accents, inequalities, Greek letters, and equation numbers;
5. verify dimensions and direct substitutions where applicable;
6. preserve the claim with `[E]` and a locator;
7. mark inference `[D]` and unresolved transcription `[U]`.

Use locators such as:

```text
[E, Duan 2026, Ch. 3, §3.1.1, printed p. 92, PDF p. 124, Eq. (...)]
```

Do not guess a section or printed page when the index cannot establish it. When a proof is in Appendix B, inspect both the theorem statement and the appendix proof.

## Formula warning

`pdftotext` may flatten matrices or confuse $\Delta$, $\Phi$, decorated symbols, superscripts, and subscripts. A hit establishes where to look; it does not authorize mathematical transcription.
