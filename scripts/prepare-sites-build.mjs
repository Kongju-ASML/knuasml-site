import { copyFile, mkdir, readFile, writeFile } from "node:fs/promises";

await mkdir("dist/server", { recursive: true });
await mkdir("dist/.openai", { recursive: true });
await copyFile(".openai/hosting.json", "dist/.openai/hosting.json");

const htmlSource = await readFile("index.html", "utf8");
const css = await readFile("styles.css", "utf8");
const js = await readFile("script.js", "utf8");
const svg = await readFile("assets/microstructure.svg", "utf8");
const svgData = `data:image/svg+xml;base64,${Buffer.from(svg).toString("base64")}`;

const html = htmlSource
  .replace('<link rel="stylesheet" href="styles.css" />', `<style>${css}</style>`)
  .replace('src="assets/microstructure.svg"', `src="${svgData}"`)
  .replace('<script type="module" src="script.js"></script>', `<script type="module">${js}</script>`);

const server = `const html = ${JSON.stringify(html)};

export default {
  async fetch(request) {
    return new Response(html, {
      headers: {
        "content-type": "text/html; charset=utf-8",
        "cache-control": "public, max-age=300"
      }
    });
  }
};
`;

await writeFile("dist/server/index.js", server);
