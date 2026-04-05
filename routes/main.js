// Create a new router
const fs = require("fs/promises"); // For standard stream
const fsPromise = require("fs").promises // For asyn file operations

// const FormData = require("form-Data");
// const fetch = require("node-fetch");

const openAsBlob = require("node:fs"); // For modern node

const path = require("path")
const express = require("express")
const router = express.Router()
const request = require('request')
const { query, validationResult } = require("express-validator");

const multer = require('multer');
const { blob } = require("node:stream/consumers");
const { type } = require("node:os");
const { json } = require("body-parser");
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

router.get('/about', function (req, res, next) {
    const preview = req.session.documentPreview || {};
    res.render('about.ejs', {
        fileMarkdown: preview.fileMarkdown || null,
        fileName: preview.fileName || null,
    });
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
    //    console.log(req.file.originalname);

    const fileBuffer = await fs.readFile(req.file.path);

    const file = new File([fileBuffer], req.file.originalname, {
        type: req.file.mimetype
    });

    const formData = new FormData();

    formData.append('file', file);
       
    const response = await fetch('http://127.0.0.1:8000/file-processing' , {
        method: 'POST',
        // headers : {'Content-Type': 'application/json'},
        body: formData,
    });

    // const txt = await response.text();
    // const data = JSON.parse(txt);

    const orgResponse = await response.json();

    const data = orgResponse.fileMarkdown;

    const chunks = orgResponse.chunks;

    console.log(data, chunks);

    res.render('about', {ok: true, fileMarkdown: data, fileName: orgResponse.fileName, chunks: chunks});
    //    const fileName = String(req.file.filename);

    await fs.unlink(req.file.path);

    // res.json({message: "File Processed", data: data});

    
    //    const response = await fetch('http://127.0.0.1:8000/file-processing', {
    //     method: 'POST',
    //     headers : {'Content-Type': 'file/pdf'},
    //     body: fileName,
    //    });
    //    const data = await response.json();
    //    console.log(data);
       //  res.json({message: "Process Started",  data: data})
    // }
});

router.get('/about', function (req, res, next) {
    const preview = req.session.documentPreview || {};
    res.render('about.ejs', {
        fileMarkdown: preview.fileMarkdown || null,
        fileName: preview.fileName || null,
    });
});

// Export the router object so index.js can access it
module.exports = router;