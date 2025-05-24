const newBtn = document.querySelector(".new");
const statementForm = document.querySelector(".form");
const closeBtn = document.querySelector(".closeBtn");
const modal = document.getElementById("modal");

newBtn.addEventListener("click", () => {
  statementForm.style.display = "block";
  modal.classList.add("active");
});

closeBtn.addEventListener("click", () => {
  statementForm.style.display = "none";
  modal.classList.remove("active");
});
