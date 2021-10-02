let table = document.getElementById('myTable');
const leftDate = new Date(document.getElementById("leftDate").value);
const rightDate = new Date(document.getElementById("rightDate").value);

function ISO8601_week_no(dt) {
    let tdt = new Date(dt.valueOf());
    let dayn = (dt.getDay() + 7) % 7;
    tdt.setDate(tdt.getDate() - dayn + 3);
    let firstThursday = tdt.valueOf();
    tdt.setMonth(0, 1);
    if (tdt.getDay() !== 4) {
        tdt.setMonth(0, 1 + ((4 - tdt.getDay()) + 7) % 7);
    }
    return 1 + Math.ceil((firstThursday - tdt) / 604800000);
}

function formatDates(dt) {
    const isoDate = dt.toISOString().substring(0, 10);
    const weekDate = `${
        dt.getFullYear()
    }-W${
        ISO8601_week_no(dt)
    }-${
        (dt.getDay() + 1)
    }`;
    return isoDate + "<br>" + weekDate;
}

for (let i = 0; i < 16; i++) {
    let row = document.createElement('TR');
    let cell1 = document.createElement('TD');
    let cell2 = document.createElement('TD');
    let cell3 = document.createElement('TD');
    let cell4 = document.createElement('TD');
    cell1.innerHTML = formatDates(leftDate);
    cell2.innerHTML = "<hr>";
    cell3.innerHTML = "<hr>";
    cell4.innerHTML = formatDates(rightDate);
    cell1.setAttribute("class", "cell");
    cell2.setAttribute("class", "cell");
    cell2.setAttribute("width", "39%");
    cell3.setAttribute("width", "39%");
    cell3.setAttribute("class", "cell");
    cell4.setAttribute("class", "cell");
    row.appendChild(cell1);
    row.appendChild(cell2);
    row.appendChild(cell3);
    row.appendChild(cell4);
    table.tBodies[0].appendChild(row);
    leftDate.setDate(leftDate.getDate() + 1);
    rightDate.setDate(rightDate.getDate() + 1);
}
console.log()