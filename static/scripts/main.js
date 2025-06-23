const statementsTable = document.querySelector("#myTable");
const wrapper = document.querySelector(".profile-wrapper");
const menu = document.querySelector(".menu");

// Profile menu (desktop-only now)
if (wrapper && menu) {
  // Toggle menu visibility on profile wrapper click
  wrapper.addEventListener("click", function (event) {
    event.stopPropagation(); // Prevent the document click listener from immediately closing it
    menu.style.display = menu.style.display === "block" ? "none" : "block";
  });

  // Close the menu if clicked outside
  document.addEventListener("click", function (event) {
    // Check if the click is outside profileToggle and profileMenu
    const isClickInsideProfile =
      wrapper.contains(event.target) || menu.contains(event.target);
    if (!isClickInsideProfile) {
      menu.style.display = "none";
    }
  });
}

// DataTables initialization
if (statementsTable) {
  new DataTable(statementsTable, {
    paging: true,
    searching: true,
    ordering: true,
    info: true,
    responsive: true,
    pageLength: 10,
    order: [[3, "desc"]],
    columnDefs: [
      {
        targets: [0], // First column (numbering)
        searchable: false,
        orderable: false,
      },
    ],
    drawCallback: function (settings) {
      const api = this.api();
      const pageInfo = api.page.info();

      api
        .column(0, { page: "current" }) // target column 0 on current page
        .nodes()
        .each(function (cell, i) {
          cell.innerHTML = pageInfo.start + i + 1;
        });
    },
  });
}

document.addEventListener("DOMContentLoaded", () => {
  // Tab functionality
  const tabLinks = document.querySelectorAll(".tab-link");
  const tabContents = document.querySelectorAll(".tab-content");

  tabLinks.forEach((btn) => {
    btn.addEventListener("click", () => {
      const target = btn.dataset.tab;

      tabLinks.forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");

      tabContents.forEach((content) => {
        content.classList.remove("active");
        if (content.id === target) content.classList.add("active");
      });
    });
  });

  // Mobile navigation (hamburger menu)
  const hamburger = document.querySelector(".hamburger");
  const navbarLinks = document.querySelector(".navbar-links");

  if (hamburger && navbarLinks) {
    hamburger.addEventListener("click", () => {
      navbarLinks.classList.toggle("active"); // Toggle visibility of nav links and profile links
    });
  }

  // Close mobile menu if clicked outside hamburger and the menu itself
  document.addEventListener("click", (e) => {
    if (hamburger && navbarLinks) {
      // Ensure elements exist before checking
      const isClickInsideHamburger = hamburger.contains(e.target);
      const isClickInsideNavbarLinks = navbarLinks.contains(e.target);

      if (
        !isClickInsideHamburger &&
        !isClickInsideNavbarLinks &&
        navbarLinks.classList.contains("active")
      ) {
        navbarLinks.classList.remove("active");
      }
    }
  });
});
