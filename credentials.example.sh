# To use:
#   1. Copy this file from `credentials.example.sh` to `credentials.sh`,
#   2. and replace the sample information below with your real credentials and
#      project ID (see link below for details).
#   3. Source the file (`source credentials.sh`).
#
# See this guideline for obtaining and converting the credentials:
#   http://docs.ansible.com/ansible/guide_gce.html#credentials

export GCE_EMAIL="my-project-email@developer.gserviceaccount.com"
export GCE_PROJECT="my-project-id"
export GCE_PEM_FILE_PATH="/path/to/my-project-credentials.json"
