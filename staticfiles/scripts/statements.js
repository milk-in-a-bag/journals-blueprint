const newBtn = document.querySelector(".new");
const delBtns = document.querySelectorAll(".del-btn");
const noBtn = document.querySelector(".no-btn");
const statementForm = document.querySelector(".newform");
const delForm = document.querySelector(".delform");
const deleteIdInput = document.getElementById("delete-id");
const modal = document.getElementById("modal");
const closeBtns = document.querySelectorAll(".closeBtn");

// Open "Add New" form
newBtn.addEventListener("click", () => {
  statementForm.style.display = "block";
  delForm.style.display = "none";
  modal.classList.add("active");
});

// Open Delete form with correct ID
delBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    delForm.style.display = "block";
    statementForm.style.display = "none";
    deleteIdInput.value = btn.getAttribute("data-id");
    modal.classList.add("active");
  });
});

// Close modal from "No" button
noBtn.addEventListener("click", () => {
  delForm.style.display = "none";
  modal.classList.remove("active");
});

// Close modal from either X button
closeBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    statementForm.style.display = "none";
    delForm.style.display = "none";
    modal.classList.remove("active");
  });
});
