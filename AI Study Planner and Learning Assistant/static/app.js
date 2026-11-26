const form = document.querySelector("#task-form");
const list = document.querySelector("#task-list");
const message = document.querySelector("#form-message");

function showMessage(text, isError = false) {
  message.textContent = text;
  message.style.color = isError ? "#b54735" : "#147d78";
}

form?.addEventListener("submit", async (event) => {
  event.preventDefault();
  const data = Object.fromEntries(new FormData(form).entries());
  data.estimated_minutes = Number(data.estimated_minutes);
  try {
    const response = await fetch("/api/tasks", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(data)
    });
    const result = await response.json();
    if (!response.ok) throw new Error(result.error || "Could not save task.");
    window.location.reload();
  } catch (error) {
    showMessage(error.message, true);
  }
});

list?.addEventListener("click", async (event) => {
  const button = event.target.closest("button[data-action]");
  if (!button) return;
  const card = button.closest(".task");
  const id = card?.dataset.id;
  if (!id) return;
  try {
    let response;
    if (button.dataset.action === "toggle") {
      response = await fetch("/api/tasks/" + id, {
        method: "PATCH",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({completed: !card.classList.contains("is-complete")})
      });
    } else if (button.dataset.action === "delete") {
      if (!window.confirm("Delete this study task?")) return;
      response = await fetch("/api/tasks/" + id, {method: "DELETE"});
    }
    if (!response || !response.ok) {
      const result = await response.json();
      throw new Error(result.error || "The action could not be completed.");
    }
    window.location.reload();
  } catch (error) {
    window.alert(error.message);
  }
});
