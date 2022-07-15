const express = require('express');
const fileUpload = require('express-fileupload');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
const port = process.env.PORT || 8080;

app.use(fileUpload({
  createParentPath: true
}));

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

app.post('/upload', async (req, res) => {
  try {
      if(!req.files) {
          res.send({
              status: false,
              message: 'No file uploaded'
          });
      } else {
          let file = req.files.name;
          file.mv('./uploads/' + file.name);
          //send response
          res.send({
              status: true,
              message: 'File is uploaded',
              data: {
                  name: file.name,
                  mimetype: file.mimetype,
                  size: file.size
              }
          });
      }
  } catch (err) {
      res.status(500).send(err);
  }
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
