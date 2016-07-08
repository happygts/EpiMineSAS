function httpPost(url, data, callback)
{
    var xmlHttp = new XMLHttpRequest();

    xmlHttp.open("POST", url, true);
    xmlHttp.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
    xmlHttp.send(JSON.stringify(data));
    xmlHttp.onload = callback;
}


function httpGet(url, callback)
{
    var xmlHttp = new XMLHttpRequest();

    xmlHttp.open("GET", url, true);
    xmlHttp.send();
    xmlHttp.onload = callback;
}

function encodeQueryData(data)
{
    var ret = [];

    for (var d in data)
	ret.push(encodeURIComponent(d) + "=" + encodeURIComponent(data[d]));
    return ret.join("&");
}

function handleResponse()
{
    var data = JSON.parse(this.responseText);
    console.log(data);
}
