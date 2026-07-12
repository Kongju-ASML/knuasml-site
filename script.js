const navLinks = Array.from(document.querySelectorAll(".site-nav a"));
const currentPage = window.location.pathname.split("/").pop() || "index.html";

navLinks.forEach((link) => {
  const linkPage = link.getAttribute("href")?.split("#")[0] || "index.html";
  link.classList.toggle("is-active", linkPage === currentPage);
});

const sections = Array.from(document.querySelectorAll("main section[id]"));

if (sections.length > 0) {
  const observer = new IntersectionObserver(
    (entries) => {
      const visible = entries
        .filter((entry) => entry.isIntersecting)
        .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];

      if (!visible) return;

      navLinks.forEach((link) => {
        if (!link.hash) return;
        link.classList.toggle("is-active", link.hash === `#${visible.target.id}`);
      });
    },
    { rootMargin: "-35% 0px -55% 0px", threshold: [0.1, 0.3, 0.6] },
  );

  sections.forEach((section) => observer.observe(section));
}
