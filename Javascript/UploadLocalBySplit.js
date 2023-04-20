const fs = require('fs')
const path = require('path')
const axios = require('axios')
const FormData = require("form-data");

const uploadLocalBySplit = (
    {
        project_name,
        upload_dir,
        train_split = 0.7,
        valid_split = 0.2,
        api_key,
    }
) => {

    // Read from your directory of images
    fs.readdir(upload_dir, async function (err, files) {
        if (err) return console.log("Unable to scan directory: " + err);

        let numUploaded = 0;

        let split, percentUploaded;

        for (let i = 0; i < files.length; i ++) {
            // We increase numUploaded every time a file is uploaded successfully. Percentage completion is how far through the files we've gone.
            percentUploaded = (numUploaded / (files.length)) * 100;

            const imageFilePath = path.join(upload_dir, files[i]);

            // By default, 70% of files will be 'train', 20% will be 'valid', 10% will be test
            if (percentUploaded < train_split * 100) {
                split = "train"; // while percent uploaded is less than 70%
            } else if (percentUploaded < (train_split + valid_split) * 100) {
                split = "valid"; // while less than 90%
            } else {
                split = "test"; // final 10%
            }

            const filename = path.basename(imageFilePath);
            const formData = new FormData();
            formData.append("name", filename);
            formData.append("file", fs.createReadStream(imageFilePath));
            formData.append("split", split);

            await axios({
                method: "POST",
                url: `https://api.roboflow.com/dataset/${project_name}/upload`,
                params: {
                    api_key: api_key,
                },
                data: formData,
                headers: formData.getHeaders()
            })
            .then(function (response) {
                numUploaded++
                console.log(response.data);
            })
            .catch(function (error) {
                console.log(error.message);
            });
        }

        console.log('Done')
    });
};

uploadLocalBySplit({
    project_name: 'pull_request_test',
    upload_dir: '../uploads',
    api_key: 'KGyYEqDTfFiudxsrxO38'
})

/*
Example usage:

uploadLocalBySplit({
    project_name: 'pull_request_test',
    upload_dir: 'uploads',
    api_key: '12345678'
})

Or optionally provide your own split values:

uploadLocalBySplit({
    project_name: 'pull_request_test',
    upload_dir: 'uploads',
    train_split: 0.6,
    valid_split: 0.2
    api_key: '12345678'
})
*/