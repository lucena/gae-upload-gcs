import os
import urllib
import webapp2

from google.appengine.api import app_identity
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.api import users


class MainHandler(webapp2.RequestHandler):
  def get(self):
    # Set your GCS Bucket Name here, or it will use your default bucket.
    # Visit https://console.cloud.google.com/appengine/settings?project=<your_app_id>
    # to create a Default Cloud Storage Bucket, if you don't have one.
    gs_bucket_name = app_identity.get_default_gcs_bucket_name()
    upload_url = blobstore.create_upload_url('/upload',
        gs_bucket_name=gs_bucket_name)

    self.response.write('<html>\n<body>\n<h1>GAE Upload to GCS Sample</h1>\n')
    self.response.write('<h2>Upload File to GCS (bucket name: %s):</h2>\n'
        % bucket_name)
    self.response.write('<form action="%s" method="POST" '
        'enctype="multipart/form-data">\n' % upload_url)
    self.response.write('<input type="file" name="file"><br>\n')
    self.response.write('<input type="submit" name="submit" '
        'value="Submit"></form>\n')
    self.response.write('</body>\n</html>\n\n')

class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
  def post(self):
    # 'file' is file upload field in the form
    upload_files = self.get_uploads('file')
    file_infos = self.get_file_infos()
    blob_info = upload_files[0]
    file_info = file_infos[0]

    self.response.write('<html>\n<body>\n<h1>GAE Upload to GCS Sample</h1>\n')
    self.response.write('<h2>File uploaded to GCS:</h2>\n')
    self.response.write('<b>BlobKey:</b> <pre>%s</pre><br>\n'
        % blob_info.key())
    self.response.write('<b>GCS Path:</b> <pre>%s</pre><br>\n'
        % file_info.gs_object_name)
    self.response.write('<b>Serve Object:<b> <a href="/serve/%s">%s</a><br>\n'
        % (blob_info.key(), blob_info.filename))
    self.response.out.write('</body>\n</html>\n')

class ServeHandler(blobstore_handlers.BlobstoreDownloadHandler):
  def get(self, resource):
    blob_key = str(urllib.unquote(resource))
    self.send_blob(blob_key)

app = webapp2.WSGIApplication([('/', MainHandler),
                               ('/upload', UploadHandler),
                               ('/serve/([^/]+)?', ServeHandler)],
                              debug=True)
