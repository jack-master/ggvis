/*******************************

脚本功能：云上妇幼测试题答案，课程快速观看（直接跳转至观看完成）。
作者：ggvis
时间：20240510

*******************************

[rewrite_local]
^http[s]?:\/\/ysfy.bjwch.cn\/wac-api\/online\/mobile\/eduCourseDetail\/getByCourseId url script-response-body https://raw.githubusercontent.com/jack-master/ggvis/main/yunshangfuyou.js

^http[s]?:\/\/ysfy.bjwch.cn\/wac-api\/questionnaire\/mobile\/questionnaire\/getDetailForMobile url script-response-body https://raw.githubusercontent.com/jack-master/ggvis/main/yunshangfuyou.js


[mitm] 
hostname = ysfy.bjwch.cn

*******************************/

if ($response.body && $request.url.includes("wac-api/online/mobile/eduCourseDetail/getByCourseId")) {
var body = $response.body.replace(/studyPoint":"\d+/g,'studyPoint":"99999999');
}

if ($response.body && $request.url.includes("allQuestion/question/chapter")) {
var body = JSON.parse($response.body);
var data = body.data.subjects;
var name = body.data.name;
var questionnaire = ""
for(var i=0; i<data.length; i++){
	var questionAndAnswer = "";
	var questionText = data[i].subjecttext;
	var questionIndex = i + 1;
	var answer = "";
	for(var j=0; j<data[i].options.length; j++){
		if (data[i].options[j].isanswer == 1){
			var answerIndex = data[i].options[j].sortindex;
			answerIndex ++;
			var answerText = data[i].options[j].text;
			answer += answerIndex + "、" + answerText + "\n"
		};
	questionAndAnswer += questionIndex + "、" + questionText + "\n" + answer
	};
};


$notify("答题结果(左滑查看详情)", "排名\t得分\t昵称", questionAndAnswer)
$done({ body });
