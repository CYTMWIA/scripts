// ==UserScript==
// @name         修改网页标题为 Markdown 链接形式
// @version      2023.10.11
// @description  修改网页标题为 Markdown 链接形式
// @author       CYTMWIA
// @match        http*://*/*
// ==/UserScript==

(function() {
    'use strict';

    let title = document.title
    setInterval(function(){
        let re = /\[(.*?)\]\((.*?)\)/
        let res = re.exec(document.title)
        if (res) {
            if (window.location!==res[2]) {
                document.title = `[${title}](${window.location})`
            }
        } else {
            title = document.title
            document.title = `[${title}](${window.location})`
        }
    },500)

})();
