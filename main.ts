// Entry point for the news-image-20261124 bounty submission.
//
// The poster itself is a pre-rendered PNG that lives next to this file.
// All this program does is place a copy of it where the harness expects
// the output to be, so the run stays fully deterministic: the same input
// file always produces the same output bytes.

import { copyFileSync, existsSync, mkdirSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const source = resolve(here, "entry.png");

if (!existsSync(source)) {
  throw new Error(`entry.png not found next to main.ts: ${source}`);
}

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
const target = join(outDir, "entry.png");

copyFileSync(source, target);
console.log(`Wrote ${target}`);
