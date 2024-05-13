// import crypto from 'crypto';
const crypto  = require('crypto');
function GetwssURL() {
    const APPID = '';
    const APISecret = '';
    const APIKey = '';

    const date = (new Date()).toUTCString();
    const host = 'mcitem.com';

    const signature_origin = `host: ${host}\ndate: ${date}\nGET /v2/iat HTTP/1.1`;
    const signature_sha = crypto.createHmac('sha256', APISecret).update(signature_origin).digest('binary');
    const signature = Buffer.from(signature_sha,'binary').toString('base64');

    const authorization_origin = `api_key="${APIKey}",algorithm="hmac-sha256",headers="host date request-line",signature="${signature}"`;

    const authorization = Buffer.from(authorization_origin).toString('base64');

    const wssURL = `wss://iat-api.xfyun.cn/v2/iat?authorization=${authorization}&date=${encodeURIComponent(date)}&host=${host}`

    return wssURL
}
// GetwssURL()
export default GetwssURL;