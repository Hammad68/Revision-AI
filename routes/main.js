// Create a new router
const express = require("express")
const router = express.Router()
const request = require('request')
const { query, validationResult } = require("express-validator");

const multer = require('multer');
const upload = multer({dest: 'uploads/'});

const redirectLogin = (req, res, next) => {
    if (!req.session.userId ) {
      res.redirect('users/login') // redirect to the login page
    } else { 
        next (); // move to the next middleware function
    } 
}

// Handle our routes
router.get('/',function(req, res, next){
    res.render('index.ejs')
});

router.get('/about',function(req, res, next){
    res.render('about.ejs')
});

router.get('/logout', redirectLogin, (req,res) => {
    req.session.destroy(err => {
    if (err) {
        return res.redirect('./')
    }
    res.send('you are now logged out. <a href='+'./'+'>Home</a>');
    })
});

router.post('/upload-file', upload.single("document"), async function(req, res, next){
    // if(err){
    //     return res.send(err.message);
    // }
    // else{
        const filepath = req.file.path;
        res.json({message: "Process Started", file: req.file.filename})
    // }
});

// Export the router object so index.js can access it
module.exports = router