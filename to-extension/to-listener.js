function navigateListener(details) {
    let url = String(details.url)

    let url_protocol_stripped = /^http[s]?:\/\/(.*)/g.exec(url)[1]

    if(url_protocol_stripped.startsWith('to/')) {
        let pathStart = url_protocol_stripped.indexOf('/')
        let path = url_protocol_stripped.substr(pathStart)
        browser.tabs.update(details.tabId, { url: `http://to.tmcd.me${path}` })
    }
}

browser.webNavigation.onBeforeNavigate.addListener(navigateListener)

console.log('Starting TO extension')