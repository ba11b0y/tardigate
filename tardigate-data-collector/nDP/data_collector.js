const {exec}  = require('child_process')
const redis = require('redis')
const fs = require('fs')
require('dotenv').config()

const client = redis.createClient();

const collectAndEncode = () =>{
    setInterval(()=>{
        exec("sudo ./nDPI/example/ndpiReader -C test.csv -P 4:8:10:128:25 -i wlo1 -s 10",(err,stdout,stderr)=>{
            let data = fs.readFileSync("./test.csv")

            client.publish("test", Buffer.from(data).toString('base64'));
            console.log('test');
  
        })
    },3000)


};

collectAndEncode()