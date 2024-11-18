/*******************************

脚本功能：网络安全刷课
作者：ggvis
时间：20241118

*******************************

[rewrite_local]
^http[s]?:\/\/playvideo.qcloud.com\/miniprogram\/v1 url script-response-body https://raw.githubusercontent.com/jack-master/ggvis/main/wangluoke.js

[mitm] 
hostname = playvideo.qcloud.com

*******************************/

if ($response.body) {
    var body = $response.body.replace(/Duration":.*?,/g, 'Duration":0,');
    }
$done({ body });
