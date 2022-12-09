var GRAY_ICON = './figma_999.svg';
var URL_REGEX = /^https?:\/\/[a-zA-Z\-]+\.figma\.com(:[0-9]+)?\/(file|proto)\/([0-9a-zA-Z]{22,128})(?:\/.*)?$/;
var CLIENT_ID = 'Z0aNrmUOqzVfEpj3ZinQ5n';
var Promise = window.TrelloPowerUp.Promise;

var makeReq = function(method, url, token) {
  return new Promise(function(resolve, reject) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
      if (xmlhttp.readyState != XMLHttpRequest.DONE) return;
      if (xmlhttp.status == 200) {
        resolve(JSON.parse(xmlhttp.response));
      } else {
        reject();
      }
    };

    xmlhttp.open(method, url);
    if (token != null) {
      xmlhttp.setRequestHeader('Authorization', 'Bearer ' + token);
    }

    xmlhttp.send();
  });
};
