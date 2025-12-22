function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
}

document.addEventListener("htmx:configRequest", (e) => {
  const token = getCookie("csrftoken");
  if (token) e.detail.headers["X-CSRFToken"] = token;
});
