function httpPost(url, data, callback)
{
    var request = new XMLHttpRequest();
    request.onreadystatechange = function()
    {
        if (request.readyState == 4 && request.status == 200)
        {
            callback(request.responseText); // Another callback here
        }
    }; 
    request.open("POST", url, true);
    request.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
    request.send(JSON.stringify(data));
}


function httpGet(url, callback)
{
    var request = new XMLHttpRequest();
    request.onreadystatechange = function()
    {
        if (request.readyState == 4 && request.status == 200)
        {
            callback(request.responseText); // Another callback here
        }
    }; 
    request.open('GET', url);
    request.send();
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

function logout() {
    sessionStorage.removeItem("email");
    sessionStorage.removeItem("admin");
    window.location.href = 'login';
}