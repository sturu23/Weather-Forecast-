function displayTime(){
    let dateTime = new Date();
    let hrs = dateTime.getHours();
    let mins = dateTime.getMinutes();
    let secs = dateTime.getSeconds();


    document.getElementById('hrs').innerHTML = hrs;
    document.getElementById('mins').innerHTML = mins;
    document.getElementById('secs').innerHTML = secs;


}
setInterval(displayTime,10)