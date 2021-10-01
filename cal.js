var table = document.getElementById('myTable')
var myDate = new Date();
myDate.setDate(myDate.getDate() - 1)

function ISO8601_week_no(dt) {
    var tdt = new Date(dt.valueOf());
    var dayn = (dt.getDay() + 6) % 7;
    tdt.setDate(tdt.getDate() - dayn + 3);
    var firstThursday = tdt.valueOf();
    tdt.setMonth(0, 1);
    if (tdt.getDay() !== 4) {
        tdt.setMonth(0, 1 + ((4 - tdt.getDay()) + 7) % 7);
    }
    return 1 + Math.ceil((firstThursday - tdt) / 604800000);
}

for (var i = 0; i < 16; i++) {
    var row = document.createElement('TR');
    var cell1 = document.createElement('TD');
    var cell2 = document.createElement('TD');
    var cell3 = document.createElement('TD');
    var isoDate = myDate.toISOString().substring(0, 10)
    var weekDate = myDate.getFullYear() + "-W" + ISO8601_week_no(myDate) + "-" + (myDate.getDay() + 1)
    cell1.innerHTML = isoDate + "<br>" + weekDate;
    cell3.innerHTML = isoDate + "<br>" + weekDate;
    cell2.innerHTML = "<hr>";
    cell1.setAttribute("class", "cell");
    cell3.setAttribute("class", "cell");
    cell2.setAttribute("class", "cell");
    cell2.setAttribute("width", "79%");
    row.appendChild(cell1);
    row.appendChild(cell2);
    row.appendChild(cell3);
    table.tBodies[0].appendChild(row);
    myDate.setDate(myDate.getDate() + 1);
}
console.log()