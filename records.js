// mongodb://jcRead:JCkj,@103.40.14.93:27023/distributedguided_clinic

use('distributedguided_clinical');

// 搜索的结果返回给数组result
const result = db.getCollection('miseRecordCaseOperate').find({ $and : [{"emr.consultationRecord" : { $ne : null }}, {"emr.consultationRecord" : { $ne : [] }}] }).toArray();

const fs = require('fs');
let markdownContent = '';

for (i in result) {
    records = result[i].emr.consultationRecord;
    markdownContent += `# 第${i+1}条记录：\n`;;
    for (j in records) {
        let { role, content } = records[j];
        role = role === "user"? "医生" : "患者";
        markdownContent += `**${role}**： ${content}\n`;
        }
    markdownContent += '\n';
    }

fs.writeFileSync('records.md', markdownContent);
