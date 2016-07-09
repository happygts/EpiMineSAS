function httpPost(url, data, callback)
{
    var request = new xmlhttprequest();
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
    var request = new xmlhttprequest();
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

//USAGE
httpGet('http://127.0.0.1:5000/list_group_doc?' + encodeQueryData({'token': 'test'}), handleResponse);
httpGet('http://127.0.0.1:5000/list_vm?' + encodeQueryData({'token': 'test'}), handleResponse);
httpPost('http://127.0.0.1:5000/connect', {'user': 'master', 'pwd': 'yolo'}, handleResponse);
httpPost('http://127.0.0.1:5000/create_vm', {'token': 'sdfsdf',
					     'os': 'Linux',
					     'ram': '1',
					     'proc': '1',
					     'hdd_size': '1'}, handleResponse);
httpGet('http://127.0.0.1:5000/list_accounts?' + encodeQueryData({'token': 'test'}), handleResponse);
httpGet('http://127.0.0.1:5000/get_auth?' + encodeQueryData({'token': 'test', 'user': 'test'}), handleResponse);
httpPost('http://127.0.0.1:5000/change_pwd', {'token': 'test', 'user': 'yolo', 'pwd': 'htd'}, handleResponse);
httpPost('http://127.0.0.1:5000/create_account', {'token': 'test', 'user': 'test', 'pwd': 'yolo'}, handleResponse);
httpPost('http://127.0.0.1:5000/change_auth', {'token': 'test', 'user': 'test', 'auth': 'retgy', 'group': 'auth'}, handleResponse);
httpPost('http://127.0.0.1:5000/change_vm', {'token': 'test', 'vm': 'BSD', 'status': 'down'}, handleResponse);