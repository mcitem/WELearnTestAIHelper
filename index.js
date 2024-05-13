// ==UserScript==
// @name         WELearn Test AI Helper ; 使用讯飞语音听写配合AI获得welearn听力测试的答案
// @namespace    https://github.com/mcitem
// @version      1.1.1
// @description  使用讯飞语音听写配合AI获得welearn听力测试的答案; 这是一个用于获取题目数据的脚本，需要配合项目中的python使用，项目地址https://github.com/mcitem/WELearnTestAIHelper
// @author       MCitem
// @icon         https://www.google.com/s2/favicons?sz=64&domain=wetest.sflep.com
// @grant        none
// @match        https://wetest.sflep.com/test/*
// @license      AGPL-3.0
// ==/UserScript==

(async function() {
    'use strict';
    const textarea = document.createElement('textarea')
    textarea.style.backgroundColor = '#1e1e1e'
    textarea.style.position = 'fixed'
    textarea.style.top = '0'
    textarea.style.left = '0'
    textarea.style.zIndex = '9999'
    textarea.style.width = '5%'
    textarea.style.height = '5%'
    textarea.style.color = 'white'
    document.body.appendChild(textarea);

    function sleep(ms=1000){
        console.log('sleeping...', ms);
        return new Promise(resolve => setTimeout(resolve, ms))
    }

    function str(str){
        let match = str.match(/["']([^"']+.mp3)["']/);
        if (match) {
            return match[1];
        } else {
            return str
        }   
    }

    // inject
    document.oncopy = null;
    document.oncut = null;
    document.onpaste = null;
    document.oncontextmenu = null;
    document.onselectstart = null;
    window.saveLog = function(){}
    setInterval(function() {
        window.isLeave = false;
        window.leaveLogTime = null;
    }, 1000);

    // 等待
    await sleep(4000)

    function createData_itemDiv(link='',hov=[]) {
        return {
            'test_center_link':link,
            'test_hovs':hov
        } 
    }
    function createData_itemDiv_test_hov(hov_link='',choises=[]) {
        return {
            'test_hov_link':hov_link,
            'choices':choises
        }
    }
    console.log( window.location.hostname)

    if (window.location.hostname == 'wetest.sflep.com') {
        wetestMain()
    }
    if (window.location.hostname == 'welearn.sflep.com') {
        welearnMain()
    }

    function welearnMain(){
        const activePart  = document.querySelector('div.active')
        const itemDivs = activePart.querySelectorAll('.itemDiv')
        let data_itemDivs = []
        let all_links = []
        let count = 1; //题目序号
        for (let i = 0; i < itemDivs.length; i++) {
            let test_center = itemDivs[i].querySelector('.text-center')
            let test_center_link = str(test_center.querySelector('a').href)
            console.log(i+1,test_center_link);

            all_links.push(test_center_link)
            let data_itemDiv = createData_itemDiv(test_center_link)
    
            let test_hovs = itemDivs[i].getElementsByClassName('test_hov')
    
            for (let j = 0; j < test_hovs.length; j++) {
                let test_hov_link =  str(test_hovs[j].getElementsByTagName('a')[0].href)
                console.log('count',count,test_hov_link);
    
                var data_itemDiv_test_hov = createData_itemDiv_test_hov(test_hov_link)
                all_links.push(test_hov_link)
    
                let choicelist = test_hovs[j].getElementsByClassName('choiceList')[0]
      
    
                let choices = choicelist.getElementsByTagName('label')
    
                let choicount = 1; //选项序号（不太需要
                for (let k = 0; k < choices.length; k++) {
                    let choi = choices[k].innerText
                    console.log(count,choicount,choi);
                    choicount = choicount + 1;
                    data_itemDiv_test_hov.choices.push(choi)
                }
                count = count + 1;
                data_itemDiv.test_hovs.push(data_itemDiv_test_hov)
            }
            data_itemDivs.push(data_itemDiv)
            
        }
        console.log(data_itemDivs);
        
        let copy = {
            "all_links":all_links,
            "data":data_itemDivs
        }
        textarea.textContent = JSON.stringify(copy,null,2)
        navigator.clipboard.writeText(JSON.stringify(copy,null,2)).then(function() {
            console.log('Copying successful!');
        })

    }

    function wetestMain(){
    const part1 = document.getElementById('part1')
    const itemDivs = part1.getElementsByClassName('itemDiv')
    let data_itemDivs = []
    let all_links = []
    let count = 1; //题目序号
    for (let i = 0; i < itemDivs.length; i++) {
        let test_center = itemDivs[i].getElementsByClassName('text-center')
        let test_center_link = str(test_center[0].getElementsByTagName('a')[0].href)
        console.log(i+1,test_center_link);

        all_links.push(test_center_link)
        let data_itemDiv = createData_itemDiv(test_center_link)

        let test_hovs = itemDivs[i].getElementsByClassName('test_hov')

        for (let j = 0; j < test_hovs.length; j++) {
            let test_hov_link =  str(test_hovs[j].getElementsByTagName('a')[0].href)
            console.log('count',count,test_hov_link);

            var data_itemDiv_test_hov = createData_itemDiv_test_hov(test_hov_link)
            all_links.push(test_hov_link)

            let choicelist = test_hovs[j].getElementsByClassName('choiceList')[0]
  

            let choices = choicelist.getElementsByTagName('label')

            let choicount = 1; //选项序号（不太需要
            for (let k = 0; k < choices.length; k++) {
                let choi = choices[k].innerText
                console.log(count,choicount,choi);
                choicount = choicount + 1;
                data_itemDiv_test_hov.choices.push(choi)
            }
            count = count + 1;
            data_itemDiv.test_hovs.push(data_itemDiv_test_hov)
        }
        data_itemDivs.push(data_itemDiv)
        
    }
    console.log(data_itemDivs);
    
    let copy = {
        "all_links":all_links,
        "data":data_itemDivs
    }
    textarea.textContent = JSON.stringify(copy,null,2)
    navigator.clipboard.writeText(JSON.stringify(copy,null,2)).then(function() {
        console.log('Copying successful!');
    })
}
})();