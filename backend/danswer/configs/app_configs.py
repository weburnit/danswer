import os

from danswer.configs.constants import AuthType
from danswer.configs.constants import DocumentIndexType


#####
# App Configs
#####
APP_HOST = "0.0.0.0"
APP_PORT = 8080
# API_PREFIX is used to prepend a base path for all API routes
# generally used if using a reverse proxy which doesn't support stripping the `/api`
# prefix from requests directed towards the API server. In these cases, set this to `/api`
APP_API_PREFIX = os.environ.get("API_PREFIX", "")


#####
# User Facing Features Configs
#####
BLURB_SIZE = 128  # Number Encoder Tokens included in the chunk blurb
GENERATIVE_MODEL_ACCESS_CHECK_FREQ = int(
    os.environ.get("GENERATIVE_MODEL_ACCESS_CHECK_FREQ") or 86400
)  # 1 day
DISABLE_GENERATIVE_AI = os.environ.get("DISABLE_GENERATIVE_AI", "").lower() == "true"


#####
# Web Configs
#####
# WEB_DOMAIN is used to set the redirect_uri after login flows
# NOTE: if you are having problems accessing the Danswer web UI locally (especially
# on Windows, try  setting this to `http://127.0.0.1:3000` instead and see if that
# fixes it)
WEB_DOMAIN = os.environ.get("WEB_DOMAIN") or "http://localhost:3000"


#####
# Auth Configs
#####
AUTH_TYPE = AuthType((os.environ.get("AUTH_TYPE") or AuthType.DISABLED.value).lower())
DISABLE_AUTH = AUTH_TYPE == AuthType.DISABLED

# Turn off mask if admin users should see full credentials for data connectors.
MASK_CREDENTIAL_PREFIX = (
    os.environ.get("MASK_CREDENTIAL_PREFIX", "True").lower() != "false"
)

SECRET = os.environ.get("SECRET", "")
SESSION_EXPIRE_TIME_SECONDS = int(
    os.environ.get("SESSION_EXPIRE_TIME_SECONDS") or 86400 * 7
)  # 7 days

# set `VALID_EMAIL_DOMAINS` to a comma seperated list of domains in order to
# restrict access to Danswer to only users with emails from those domains.
# E.g. `VALID_EMAIL_DOMAINS=example.com,example.org` will restrict Danswer
# signups to users with either an @example.com or an @example.org email.
# NOTE: maintaining `VALID_EMAIL_DOMAIN` to keep backwards compatibility
_VALID_EMAIL_DOMAIN = os.environ.get("VALID_EMAIL_DOMAIN", "")
_VALID_EMAIL_DOMAINS_STR = (
    os.environ.get("VALID_EMAIL_DOMAINS", "") or _VALID_EMAIL_DOMAIN
)
VALID_EMAIL_DOMAINS = (
    [domain.strip() for domain in _VALID_EMAIL_DOMAINS_STR.split(",")]
    if _VALID_EMAIL_DOMAINS_STR
    else []
)
# OAuth Login Flow
# Used for both Google OAuth2 and OIDC flows
OAUTH_CLIENT_ID = (
    os.environ.get("OAUTH_CLIENT_ID", os.environ.get("GOOGLE_OAUTH_CLIENT_ID")) or ""
)
OAUTH_CLIENT_SECRET = (
    os.environ.get("OAUTH_CLIENT_SECRET", os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET"))
    or ""
)

# for basic auth
REQUIRE_EMAIL_VERIFICATION = (
    os.environ.get("REQUIRE_EMAIL_VERIFICATION", "").lower() == "true"
)
SMTP_SERVER = os.environ.get("SMTP_SERVER") or "smtp.gmail.com"
SMTP_PORT = int(os.environ.get("SMTP_PORT") or "587")
SMTP_USER = os.environ.get("SMTP_USER", "your-email@gmail.com")
SMTP_PASS = os.environ.get("SMTP_PASS", "your-gmail-password")
EMAIL_FROM = os.environ.get("EMAIL_FROM") or SMTP_USER


#####
# DB Configs
#####
DOCUMENT_INDEX_NAME = "danswer_index"
# Vespa is now the default document index store for both keyword and vector
DOCUMENT_INDEX_TYPE = os.environ.get(
    "DOCUMENT_INDEX_TYPE", DocumentIndexType.COMBINED.value
)
VESPA_HOST = os.environ.get("VESPA_HOST") or "localhost"
VESPA_PORT = os.environ.get("VESPA_PORT") or "8081"
VESPA_TENANT_PORT = os.environ.get("VESPA_TENANT_PORT") or "19071"
# The default below is for dockerized deployment
VESPA_DEPLOYMENT_ZIP = (
    os.environ.get("VESPA_DEPLOYMENT_ZIP") or "/app/danswer/vespa-app.zip"
)
# Number of documents in a batch during indexing (further batching done by chunks before passing to bi-encoder)
try:
    INDEX_BATCH_SIZE = int(os.environ.get("INDEX_BATCH_SIZE", 16))
except ValueError:
    INDEX_BATCH_SIZE = 16

# Below are intended to match the env variables names used by the official postgres docker image
# https://hub.docker.com/_/postgres
POSTGRES_USER = os.environ.get("POSTGRES_USER") or "postgres"
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD") or "password"
POSTGRES_HOST = os.environ.get("POSTGRES_HOST") or "localhost"
POSTGRES_PORT = os.environ.get("POSTGRES_PORT") or "5432"
POSTGRES_DB = os.environ.get("POSTGRES_DB") or "postgres"
CHUNK_DB_PLATFORM = os.environ.get("CHUNK_DB_PLATFORM") or "vespa"

#####
# Connector Configs
#####
POLL_CONNECTOR_OFFSET = 30  # Minutes overlap between poll windows

# Some calls to get information on expert users are quite costly especially with rate limiting
# Since experts are not used in the actual user experience, currently it is turned off
# for some connectors
ENABLE_EXPENSIVE_EXPERT_CALLS = False

GOOGLE_DRIVE_INCLUDE_SHARED = False
GOOGLE_DRIVE_FOLLOW_SHORTCUTS = False
GOOGLE_DRIVE_ONLY_ORG_PUBLIC = False

FILE_CONNECTOR_TMP_STORAGE_PATH = os.environ.get(
    "FILE_CONNECTOR_TMP_STORAGE_PATH", "/home/file_connector_storage"
)

# TODO these should be available for frontend configuration, via advanced options expandable
WEB_CONNECTOR_IGNORED_CLASSES = os.environ.get(
    "WEB_CONNECTOR_IGNORED_CLASSES", "sidebar,footer"
).split(",")
WEB_CONNECTOR_IGNORED_ELEMENTS = os.environ.get(
    "WEB_CONNECTOR_IGNORED_ELEMENTS", "nav,footer,meta,script,style,symbol,aside"
).split(",")
WEB_CONNECTOR_OAUTH_CLIENT_ID = os.environ.get("WEB_CONNECTOR_OAUTH_CLIENT_ID")
WEB_CONNECTOR_OAUTH_CLIENT_SECRET = os.environ.get("WEB_CONNECTOR_OAUTH_CLIENT_SECRET")
WEB_CONNECTOR_OAUTH_TOKEN_URL = os.environ.get("WEB_CONNECTOR_OAUTH_TOKEN_URL")

NOTION_CONNECTOR_ENABLE_RECURSIVE_PAGE_LOOKUP = (
    os.environ.get("NOTION_CONNECTOR_ENABLE_RECURSIVE_PAGE_LOOKUP", "").lower()
    == "true"
)

CONFLUENCE_CONNECTOR_LABELS_TO_SKIP = [
    ignored_tag
    for ignored_tag in os.environ.get("CONFLUENCE_CONNECTOR_LABELS_TO_SKIP", "").split(
        ","
    )
    if ignored_tag
]

GONG_CONNECTOR_START_TIME = os.environ.get("GONG_CONNECTOR_START_TIME")

GITHUB_CONNECTOR_BASE_URL = os.environ.get("GITHUB_CONNECTOR_BASE_URL") or None

DASK_JOB_CLIENT_ENABLED = (
    os.environ.get("DASK_JOB_CLIENT_ENABLED", "").lower() == "true"
)
EXPERIMENTAL_CHECKPOINTING_ENABLED = (
    os.environ.get("EXPERIMENTAL_CHECKPOINTING_ENABLED", "").lower() == "true"
)


#####
# Indexing Configs
#####
# NOTE: Currently only supported in the Confluence and Google Drive connectors +
# only handles some failures (Confluence = handles API call failures, Google
# Drive = handles failures pulling files / parsing them)
CONTINUE_ON_CONNECTOR_FAILURE = os.environ.get(
    "CONTINUE_ON_CONNECTOR_FAILURE", ""
).lower() not in ["false", ""]
# When swapping to a new embedding model, a secondary index is created in the background, to conserve
# resources, we pause updates on the primary index by default while the secondary index is created
DISABLE_INDEX_UPDATE_ON_SWAP = (
    os.environ.get("DISABLE_INDEX_UPDATE_ON_SWAP", "").lower() == "true"
)
# Controls how many worker processes we spin up to index documents in the
# background. This is useful for speeding up indexing, but does require a
# fairly large amount of memory in order to increase substantially, since
# each worker loads the embedding models into memory.
NUM_INDEXING_WORKERS = int(os.environ.get("NUM_INDEXING_WORKERS") or 1)
CHUNK_OVERLAP = 0
# More accurate results at the expense of indexing speed and index size (stores additional 4 MINI_CHUNK vectors)
ENABLE_MINI_CHUNK = os.environ.get("ENABLE_MINI_CHUNK", "").lower() == "true"
# Finer grained chunking for more detail retention
# Slightly larger since the sentence aware split is a max cutoff so most minichunks will be under MINI_CHUNK_SIZE
# tokens. But we need it to be at least as big as 1/4th chunk size to avoid having a tiny mini-chunk at the end
MINI_CHUNK_SIZE = 150
# Timeout to wait for job's last update before killing it, in hours
CLEANUP_INDEXING_JOBS_TIMEOUT = int(os.environ.get("CLEANUP_INDEXING_JOBS_TIMEOUT", 3))
# If set to true, then will not clean up documents that "no longer exist" when running Load connectors
DISABLE_DOCUMENT_CLEANUP = (
    os.environ.get("DISABLE_DOCUMENT_CLEANUP", "").lower() == "true"
)


#####
# Model Server Configs
#####
# If MODEL_SERVER_HOST is set, the NLP models required for Danswer are offloaded to the server via
# requests. Be sure to include the scheme in the MODEL_SERVER_HOST value.
MODEL_SERVER_HOST = os.environ.get("MODEL_SERVER_HOST") or None
MODEL_SERVER_ALLOWED_HOST = os.environ.get("MODEL_SERVER_HOST") or "0.0.0.0"
MODEL_SERVER_PORT = int(os.environ.get("MODEL_SERVER_PORT") or "9000")

# specify this env variable directly to have a different model server for the background
# indexing job vs the api server so that background indexing does not effect query-time
# performance
INDEXING_MODEL_SERVER_HOST = (
    os.environ.get("INDEXING_MODEL_SERVER_HOST") or MODEL_SERVER_HOST
)


#####
# Miscellaneous
#####
DYNAMIC_CONFIG_STORE = os.environ.get(
    "DYNAMIC_CONFIG_STORE", "FileSystemBackedDynamicConfigStore"
)
DYNAMIC_CONFIG_DIR_PATH = os.environ.get("DYNAMIC_CONFIG_DIR_PATH", "/home/storage")
JOB_TIMEOUT = 60 * 60 * 6  # 6 hours default
# used to allow the background indexing jobs to use a different embedding
# model server than the API server
CURRENT_PROCESS_IS_AN_INDEXING_JOB = (
    os.environ.get("CURRENT_PROCESS_IS_AN_INDEXING_JOB", "").lower() == "true"
)
# Logs every model prompt and output, mostly used for development or exploration purposes
LOG_ALL_MODEL_INTERACTIONS = (
    os.environ.get("LOG_ALL_MODEL_INTERACTIONS", "").lower() == "true"
)
# If set to `true` will enable additional logs about Vespa query performance
# (time spent on finding the right docs + time spent fetching summaries from disk)
LOG_VESPA_TIMING_INFORMATION = (
    os.environ.get("LOG_VESPA_TIMING_INFORMATION", "").lower() == "true"
)
# Anonymous usage telemetry
DISABLE_TELEMETRY = os.environ.get("DISABLE_TELEMETRY", "").lower() == "true"
# notset, debug, info, warning, error, or critical
LOG_LEVEL = os.environ.get("LOG_LEVEL", "info")

PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH=os.environ.get("PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH","/root/.cache/ms-playwright/chromium-1097/chrome-linux/chrome")
