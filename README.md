<h1 align="center">WELearn Test AI Helper</h1>

<p align="center">
使用讯飞语音听写配合AI获得welearn听力测试的答案
</p>


## 声明

- 本项目基于AGPL-3.0开放源代码，仅供技术学习和交流，开发者团队并未授权任何组织、机构以及个人将其用于商业或者盈利性质的活动。也从未使用本项目进行任何盈利性活动。个人或者组织，机构如果使用本项目产生的各类纠纷，法律问题，均由其本人承担。
- 如果您开始使用本项目，即视为同意项目免责声明中的一切条款，条款更新不再另行通知。
- 本脚本仅供学习交流使用，对于使用本脚本造成的任何后果，均由使用者本人承担。

## 兼容性
- 答案正确率受语音听写识别和AI阅读理解能力影响，输出题目文本可能存在错误，建议自行阅读输出的题目文本，斟酌作答

用户脚本`index.js`目前只为`wetest.sflep.com/test`这个新版考试界面做了适配，且只去获取`PartA`的听力题选择题的的题目数据

而，还有一个考试域名`welearn.sflep.com/test/` 的html类名不太相同，因为用不上所以没有去适配（

## FFmpeg
如果在用户脚本能够方便、兼容地将 MP3 转为 16k pcm数据，且提交讯飞语音听写能够正常得到内容的话，那么就不在需要python了 
<br/><br/><br/>
比如在用户脚本中运行ffmpeg.wasm（ 这好像并不现实，也无法cdn引入和生成web worker

期待大佬提供支持（



## 依赖
Windows需要安装ffmpeg才能正常使用

[下载](https://github.com/BtbN/FFmpeg-Builds/releases) `ffmpeg-master-latest-win64-gpl.zip`
手动配置系统环境变量安装（推荐）

科学上网安装法
```sh
winget install --id Gyan.FFmpeg
```

主要依赖
```sh
pip install wget
pip install ffmpeg-python
pip install websockets
```

使用 Moonshot AI API的 依赖 (推荐) 

这个免费api给了比较多，不用实名注册就有
```
pip install openai
```

使用 讯飞星火API 的 依赖
```
pip install --upgrade spark_ai_python
```
）也可以手动复制output.txt的内容手动扔给ai

## 使用
- 配置config.json

     - iat配置项为 讯飞语音**听写**
     - kimi配置项为 Moonshot AI
     - spark配置项为 讯飞星火大模型
    
     ）也可以手动复制文本题目输出喂给ai,只有iat是必填的

将`index.js`加载到`scriptcat`或`tampermonkey`中
- 打开考试界面 `index.js`会等待4秒以等待试卷加载 

    ）如果4秒还不够加载，请直接修改`index.js`代码

- 在题目界面的窗口复制生成的`json`题目数据

    ）如果焦点在考试界面中，也会自动写入剪贴板

- 将复制的数据粘贴到data.json中,
- 执行 `main.py`

    ）相当于 按顺序执行 
    - 执行 `index.py`
    - 执行 `websocket.py`
    - 执行 `dist.py`

- 执行 AI调用 或直接复制`output.txt`的内容手动扔给AI 让ai给答案
    ）你也可以修改dist.py,制作更为详细的prompt
## data.json
data.json的数据结构。与html中的类名基本保持相同（除了加s表示复数
```json
{  //注意：json并不支持注释
  "all_links": [ //所有音频源的链接
    "div1.mp3",
    "yy1.mp3", 
    "yy2.mp3"
  ],
  "data": [
    {
      "test_center_link": "div1.mp3", //听力的主要内容
      "test_hovs": [
        {
          "test_hov_link": "yy1.mp3", // 每一题的题目
          "choices": [
            "A) xxx",
            "B) xxx",
            "C) xxx",
            "D) xxx"
          ]
        },
        {
          "test_hov_link": "yy2.mp3",
          "choices": [
            "A) xxx",
            "B) xxx",
            "C) xxx",
            "D) xxx"
          ]
        }
      ]
    },
    {
        "test_center_link":"...", //第二段听力内容
        "test_hovs":[/**... */]  // 这段内容对应的题目
    }
  ]
}
```
## index.js
[ScriptCat](https://scriptcat.org/zh-CN/script-show-page/1825/)

[GreasyFork](https://greasyfork.org/zh-CN/scripts/494802-welearn-test-ai-helper-%E4%BD%BF%E7%94%A8%E8%AE%AF%E9%A3%9E%E8%AF%AD%E9%9F%B3%E5%90%AC%E5%86%99%E9%85%8D%E5%90%88ai%E8%8E%B7%E5%BE%97welearn%E5%90%AC%E5%8A%9B%E6%B5%8B%E8%AF%95%E7%9A%84%E7%AD%94%E6%A1%88)

已尝试禁用离开考试检测和禁止复制粘贴右键等

>为什么用 user script 不用 python的xxx ?

）因为一开始就想纯用户脚本实现，用python其他解析html的库也是可以的（，再不济可以selenium（
# License
WELearn Test AI Helper licensed under AGPLv3.

Copyright © 2024 by MCitem.