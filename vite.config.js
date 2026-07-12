import { resolve } from "node:path";
import { defineConfig } from "vite";

const pages = [
  "index",
  "research",
  "people",
  "projects",
  "facilities",
  "publications",
  "activities",
  "contact",
];

export default defineConfig({
  // Use relative asset paths so the built site works both at a custom domain root
  // and under a GitHub Pages project path such as /knuasml-site/.
  base: "./",
  build: {
    rollupOptions: {
      input: Object.fromEntries(pages.map((page) => [page, resolve(__dirname, `${page}.html`)])),
    },
  },
});
