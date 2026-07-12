import { defineConfig } from "vite";

export default defineConfig({
  // Use relative asset paths so the built site works both at a custom domain root
  // and under a GitHub Pages project path such as /knuasml-site/.
  base: "./",
});
