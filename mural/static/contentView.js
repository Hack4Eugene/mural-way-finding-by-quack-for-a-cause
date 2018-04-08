function show(element, disable1, disable2) {
	
    var elem = document.getElementById(element);
    document.getElementById(disable1).style.display = "none";;
    document.getElementById(disable2).style.display = "none";;
    if (elem.style.display === "none") {
        elem.style.display = "block";
    } else {
        elem.style.display = "none";
    }
}

