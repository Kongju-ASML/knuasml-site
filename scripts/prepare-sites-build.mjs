import { copyFile, mkdir, writeFile } from "node:fs/promises";

await mkdir("dist/server", { recursive: true });
await mkdir("dist/.openai", { recursive: true });
await copyFile(".openai/hosting.json", "dist/.openai/hosting.json");

const server = `import { readFile } from "node:fs/promises";
import { extname, join, normalize } from "node:path";

const root = new URL("../", import.meta.url);
const types = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".svg": "image/svg+xml; charset=utf-8",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".webp": "image/webp",
  ".ico": "image/x-icon"
};

export default {
  async fetch(request) {
    const url = new URL(request.url);
    const pathname = decodeURIComponent(url.pathname);
    const cleanPath = normalize(pathname).replace(/^([.][.][\\\\/])+/, "");
    const filePath = cleanPath === "/" ? "index.html" : cleanPath.replace(/^\\\\|^\\//, "");
    const target = join(root.pathname, filePath);

    try {
      const body = await readFile(target);
      return new Response(body, {
        headers: {
          "content-type": types[extname(target)] || "application/octet-stream",
          "cache-control": "public, max-age=300"
        }
      });
    } catch {
      const body = await readFile(join(root.pathname, "index.html"));
      return new Response(body, {
        headers: { "content-type": "text/html; charset=utf-8" }
      });
    }
  }
};
`;

await writeFile("dist/server/index.js", server);
