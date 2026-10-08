const input = document.querySelector("#query");
const status = document.querySelector("#search-status");
const results = document.querySelector("#results");
fetch(input.dataset.index)
  .then((r) => {
    if (!r.ok) throw new Error();
    return r.json();
  })
  .then((pages) => {
    const search = () => {
      const terms = input.value
        .toLowerCase()
        .trim()
        .split(/\s+/)
        .filter(Boolean);
      results.replaceChildren();
      if (!terms.length) {
        status.textContent = "Search across all posts and pages.";
        return;
      }
      const matches = pages.filter((p) =>
        terms.every((t) => `${p.title} ${p.content}`.toLowerCase().includes(t)),
      );
      status.textContent = `${matches.length} ${matches.length === 1 ? "result" : "results"}`;
      for (const page of matches) {
        const li = document.createElement("li");
        const a = document.createElement("a");
        a.href = page.permalink;
        a.textContent = page.title;
        li.append(a);
        results.append(li);
      }
    };
    input.addEventListener("input", search);
    search();
  })
  .catch(() => {
    status.textContent =
      "Search could not load. Please try again or browse the archive.";
  });
