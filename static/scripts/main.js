const statementsTable = document.querySelector("#myTable");

if (statementsTable) {
  new DataTable(statementsTable, {
    paging: true,
    searching: true,
    ordering: true,
    info: true,
    responsive: true,
    pageLength: 10,
    order: [[2, "desc"]],
    columnDefs: [
      {
        targets: 0, // First column (numbering)
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
