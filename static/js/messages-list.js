let observer = null;

function syncEmptyState() {
  const ul = document.getElementById("messages-ul");
  const empty = document.getElementById("messages-empty");
  if (!ul || !empty) return;

  const hasItems = ul.querySelectorAll(":scope > li").length > 0;
  empty.hidden = hasItems;
}

function initMessagesListObserver() {
  syncEmptyState();

  const ul = document.getElementById("messages-ul");
  if (!ul) return;

  if (observer) observer.disconnect();

  observer = new MutationObserver(() => syncEmptyState());
  observer.observe(ul, { childList: true });
}

document.addEventListener("DOMContentLoaded", initMessagesListObserver);

document.body.addEventListener("htmx:afterSwap", (e) => {
  if (
    e.target?.id === "messages-container" ||
    e.target?.id === "messages-list" ||
    e.target?.querySelector?.("#messages-ul")
  ) {
    initMessagesListObserver();
  }
});

document.body.addEventListener("htmx:afterSettle", syncEmptyState);
