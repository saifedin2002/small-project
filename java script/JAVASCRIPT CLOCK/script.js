function showTime() {
    let date = new Date();
    let h = date.getHours(); // from 0 to 23
    let m = date.getMinutes(); // from 0 to 59
    let s = date.getSeconds();// from 0 to 59
    if (h == 0) {
        h = 12
    }

    if (h > 12) {
        h = h - 12;
        session = "PM";
    }

    
    h = (h < 10) ? "0" + h : h;
    m = (m < 10) ? "0" + m : m;
    s = (s < 10) ? "0" + s : s;
    
    let time = h + ":" + m + ":" + s + " " + session;
    document.getElementById("MyClockDisplay").innerHTML = time;
    document.getElementById("MyClockDisplay").textContent = time;

    setTimeout(showTime, 1000);    
}


showTime();