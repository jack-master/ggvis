// mongodb://jcRead:JCkj,@103.40.14.93:27023/distributedguided_clinical

use('distributedguided_clinical');

// 搜索的结果返回给数组result
const result = db.getCollection('miseRecordCaseOperate').find({
    $and : [
        {"emr.consultationRecord" : { $ne : null }},
        {"emr.consultationRecord" : { $ne : [] }}
    ]
}).toArray();

const fs = require('fs');
let markdownContent = '';

result.forEach((element,index) => {
    const records = element.emr.consultationRecord;
    markdownContent += `# 第${index+1}条记录：\n`;
    records.forEach((item,index) => {
        let { role, content } = item;
        role = role === "user"? "医生" : "患者";
        markdownContent += `**${role}**： ${content}\n`;
    });
    markdownContent += '\n';
});

fs.writeFileSync(`${result.length}_records.md`, markdownContent);
