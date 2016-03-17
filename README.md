# gae-upload-gcs

A sample Google App Engine (GAE) application that allows you to upload a file to Google Cloud Storage (GCS) and then serve it from App Engine.

## Installation

1. Download this project.
2. Edit the `app.yaml` file and set `application` to your app_id.
3. Edit the `main.py` file and set `gs_bucket_name` to the bucket you want to upload your files to. You can also create a Default Cloud Storage Bucket by visiting the [App Engine Settings](https://console.cloud.google.com/appengine/settings) page.
4. Deploy your app. You can use `appcfg.py update ./gae-upload-gcs` to do this.

## Running the Application
Visit `https://gae-upload-gcs-dot-<your-app-id>.appspot.com/`
