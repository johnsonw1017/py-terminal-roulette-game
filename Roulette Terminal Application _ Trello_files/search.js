// depends on shared.js

var fileCache = null;
var fileCacheTime = Date.now();
var pendingSearch = null;

function doSearch(token) {
  if (pendingSearch != null) return pendingSearch;
  if (fileCache != null && Date.now() - fileCacheTime < 60000) {
    return new Promise(function(resolve, reject) {
      resolve(fileCache);
    });
  }

  pendingSearch = makeReq('GET', '/api/user/trello/files', token)
  .then(function(resp) {
    fileCache = resp.meta;
    fileCacheTime = Date.now();
    pendingSearch = null;
    return fileCache;
  });

  return pendingSearch;
}

function attachFile(url, t, options) {
  t.attach({ url });
  return t.closePopup();
}

function popupSearch(token, mode, t, options) {
  t.popup({
    title: 'Figma',
    items: [{
      text: 'Loading files...',
    }]
  });

  return doSearch(token)
  .then(function(files) {
    var allFiles = [];
    files.forEach(function(file) {
      var url = file.url;
      url = url.replace('/file/', '/' + mode + '/');

      allFiles.push({
        text: file.name,
        callback: attachFile.bind(this, url),
        url
      });
    });

    return t.popup({
      title: 'Figma Files',
      items: allFiles,
      search: {
        count: 10,
        placeholder: 'Search files',
        empty: 'No files found'
      }
    });
  })
  .catch(function () {
    return t.popup({
      title: 'Error',
      items: [{
        text: 'Could not retrieve files',
        callback: nullCallback
      }]
    });
  });
}

function showMenu(token, t, options) {
  doSearch(token);
  return t.popup({
    title: 'Figma',
    items: [{
      text: 'Attach a file',
      callback: popupSearch.bind(this, token, 'file')
    }, {
      text: 'Attach a prototype',
      callback: popupSearch.bind(this, token, 'proto')
    }]
  });
}
