// ==UserScript==
// @name         修改网页标题为 Markdown 链接形式
// @version      2023.10.11
// @description  修改网页标题为 Markdown 链接形式
// @author       CYTMWIA
// @match        http*://*/*
// ==/UserScript==

(function() {
    'use strict';

    setInterval(function(){
        let re = /\[.*?\]\(.*?\)/
        let res = re.exec(document.title)
        if (!res) {
            document.title = `[${document.title}](${window.location})`
        }
    },500)

})();
