const newBtn = document.querySelector(".new");
const delBtn = document.querySelectorAll(".del-btn");
const noBtn = document.querySelector(".no-btn");
const statementForm = document.querySelector(".newform");
const delForm = document.querySelector(".delform");
const closeBtn = document.querySelector(".closeBtn");
const deleteIdInput = document.getElementById("delete-id");
const modal = document.getElementById("modal");

newBtn.addEventListener("click", () => {
  statementForm.style.display = "block";
  modal.classList.add("active");
});

closeBtn.addEventListener("click", () => {
  statementForm.style.display = "none";
  modal.classList.remove("active");
});

delBtn.forEach((btn) => {
  btn.addEventListener("click", () => {
    delForm.style.display = "block";
    const id = btn.getAttribute("data-id");
    deleteIdInput.value = id;
    modal.classList.add("active");
  });
});

noBtn.addEventListener("click", () => {
  delForm.style.display = "none";
  modal.classList.remove("active");
});
