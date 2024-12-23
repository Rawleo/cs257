function updateDate(the_json) {
    json = the_json;
    abbr = json['abbr']
    startdate = json['startdate'];
    enddate = json['enddate'];
    datetoupdate = document.getElementById("daterange");
    newdaterange = "Data at " + abbr + " is available from " + startdate + " through " + enddate;
    daterange.innerHTML=newdaterange;
}

function fetchDate() {
    my_airport = document.getElementById("airports").value;
    lookupURL = "/lookup/" + my_airport;
    fetch(lookupURL).then(response => response.json()).then(the_json => updateDate(the_json));
}

function updateDescription(the_json) {
    json = the_json;
    column = json['column'];
    description = column + ": " + json['description']
    toUpdate = document.getElementById("columnDescription");
    toUpdate.innerHTML=description;
}

function hoverDescription(column) {
    // alert(column);
    lookupURL = "/columndescription/" + column;
    fetch(lookupURL).then(response => response.json()).then(the_json => updateDescription(the_json))


    // will acquire id of column that is hovered by mouse
    // url for the acquisition of description matching the column name from flask link in python
        // requires the creation of sql script to match column to correct description
    // fetch() will need to fetch the colmun description from the server via a json 
    // display change in html for the hover over description! 
}