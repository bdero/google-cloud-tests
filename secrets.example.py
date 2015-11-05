# To use:
#   1. Copy this file from `secrets.example.py` to `secrets.py`,
#   2. and replace the sample information below with your real credentials and
#      project ID.
#
# Note: `secrets.py` must be in the Python 2 path to be imported by Ansible,
#       but it should be in the path when executing `ansible-playbook` from
#       within the `playbooks` directory (as a symlink has been placed in that
#       directory).

GCE_PARAMS = (
    'my-project-email@developer.gserviceaccount.com',
    '/path/to/my-project-credentials.json'
)
GCE_KEYWORD_PARAMS = {'project': 'my-project-id'}
