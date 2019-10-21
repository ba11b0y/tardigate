const {exec}  = require('child_process')
const redis = require('redis')
const fs = require('fs')
require('dotenv').config()

const client = redis.createClient();

const writeThroughCache = () =>{
    return new Promise((resolve,reject)=>{
        exec("sudo ./nDPI/example/ndpiReader -C test.csv -P 4:8:10:128:25 -i wlo1 -s 10",(err,stdout,stderr)=>{
            console.log("test")
            let i = 0;
            fs.createReadStream("./test.csv")
            .on('data',(d)=>{
                client.xadd("SAURAV","*","csv",d);
            })
            .on('end',()=>{
                resolve("done")
            })
            .on('error',(error)=>reject(err))

                
    })
})
}

const service = ()=>{
    setInterval( ()=>{
        writeThroughCache().then(console.log).catch(console.log)
    },10000)
}
service()