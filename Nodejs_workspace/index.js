const express = require('express')
const app = express()
const port = 5000

const bodyParser = require('body-parser');
const { User } =require("./models/User");

//application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({extended : true}));

//application/ json
app.use(bodyParser.json());

const mongoose = require('mongoose')
mongoose.connect('', {
    useNewUrlParser: true, useUnifiedTopology: true
}).then(() => console.log('MongoDB Connected...'))
  .catch(err => console.log(err))


app.get('/', (req,res) => res.send('Hello World!'))


app.post('/register', (req, res) => {
    //会員加入の時必要な情報をクライアントから持ってくると
    //それをデータベースに入れる
    
    

    const user = new User(req.body)

    user.save((err, userInfo) => {
        if(err) return res.json({ success: false, err})
        return res.status(200).json({
          success : true
      })
    })
})

app.listen(port, () => console.log(`Example app listening on port ${port}!`))