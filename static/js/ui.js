const refreshLucideIcons = () => {
  if (window.lucide) {
    window.lucide.createIcons();
  }
};

const autoDismissMessages = (root = document) => {
  root.querySelectorAll("[data-auto-dismiss]").forEach((el) => {
    if (el.dataset.dismissTimer) return;
    const timeoutMs = Number(el.dataset.autoDismiss) || 4000;
    el.dataset.dismissTimer = "1";
    setTimeout(() => {
      el.style.transition = "opacity 300ms";
      el.style.opacity = "0";
      setTimeout(() => el.remove(), 300);
    }, timeoutMs);
  });
};

const applyUiEnhancements = (root = document) => {
  refreshLucideIcons();
  autoDismissMessages(root);
};

document.addEventListener("DOMContentLoaded", () => applyUiEnhancements());
document.addEventListener("htmx:afterSwap", (e) => applyUiEnhancements(e.target || document));
