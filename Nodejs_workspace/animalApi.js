const express = require('express')
var cors = require('cors')
const app = express()
const port = 3000

//全ての要請に答えるように設定する
app.use(cors())

app.get('/sound/:name', (req, res) => {
    const { name } = req.params

    if(name == 'dog') {
        res.json({'sound' : 'わんわん'})
    }else if(name == 'cat') {
        res.json({'sound' : 'にゃんにゃん'})
    }else {
        res.json({'sound' : '動物ではありません'})
    }

    //res.send({'what animal?' : animal.name})
})



app.listen(port, () => {
    console.log(`linstening on port ${port}`)
})


