const statementsTable = document.querySelector("#myTable");
const wrapper = document.querySelector(".profile-wrapper");
const menu = document.querySelector(".menu");

if (wrapper && menu) {
  // Toggle menu visibility on profile wrapper click
  wrapper.addEventListener("click", function (event) {
    event.stopPropagation(); // Prevent the document click listener from immediately closing it
    menu.style.display = menu.style.display === "block" ? "none" : "block";
  });

  // Close the menu if clicked outside
  document.addEventListener("click", function (event) {
    if (!wrapper.contains(event.target)) {
      menu.style.display = "none";
    }
  });
}

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
        targets: [0, 4], // First column (numbering)
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
