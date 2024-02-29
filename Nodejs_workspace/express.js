const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
    res.send('Hello World')
})

app.get('/dog', (req, res) => {
    res.send({'sound': 'わんわん'})
    //jsonの場合より詳しくするため
    //res.jsonを使った方がいい
})

app.get('/cat', (req, res) => {
    res.send({'sound':'にゃんにゃん'})
})


app.get('/user/:id', (req, res) => {
    //Parmeter Type
    //const param = req.params
    //console.log(param);

    //Query Type
    const query = req.query
    console.log(query.q);
    console.log(query.name);  

    res.send({'userid': query.name});
})



app.listen(port, () => {
    console.log(`linstening on port ${port}`)
})



